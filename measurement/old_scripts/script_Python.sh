#!/bin/bash

# Example to use this script
# ./script_Python.sh "nbody.py 50000000" "nbody_50000"
# ./script_Python.sh "<python_file arguments>" "<path or folder or directory>"

# Show Aalto logo
./logo.sh

# Save all Python versions through the pyenv command in a list variable
readarray -t versions < <(pyenv versions | awk '/*/{print $2} FNR>1&&!/*/{print $1}')

# MENU
echo "Available Python versions are the next ones:"
for version in "${versions[@]}"; do
  echo "  - $version"
done
echo -n "  - all

 *** Type the version (for example '3.11.3', or 'all' to measure all Python versions): "
read version

# CONDITION
if [ $version == 'all' ] || [ $version == 'All' ] || [ $version == 'ALL' ]; then
  ./script5.sh "$1" "$2"
else
  # Output file for recording turbostat data in CSV format
  program=$(echo $1 | awk -F. '{print $1}')
  path=$2
  [ -d $path ] || mkdir $path

  output_generalFile="$path/performance_data_allVersions_$program.csv"
  temp_file="$path/temp_performance_data.txt"
  touch $temp_file

  # Command to execute the Python program in each version
  python_command="python ${1}"
  echo
  echo "  *** Analysing the Python program: $1 ---"
  echo "  *** Recording the measurenments in the CSV file: $output_generalFile ..."

  pyenv global $version

  # Verify the Python version
  python_version=$(python --version 2>&1)
  echo
  echo "        ... Analysing Python $python_version ..."

  # Sleep for 2 mins to allow a cool-down and in turn affect energy measurements (which are suceptible to this)
  # ** CLEAR THE MEMORY
  #sleep 2m

  # Function to run turbostat and record data in temp_file
  run_turbostat() {
    # Run turbostat in the background and redirect output to a temporary file
    sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" turbostat --out $temp_file --Joules --Summary --enable all $python_command
  }

  # Run the turbostat function
  echo "Running Turbostat and program:"
  run_turbostat
    
  # Convert turbostat output to CSV format
  col_names=$(tail -2 $temp_file | head -n1 | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
  results=$(tail -1 $temp_file | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',' | awk '{gsub(/,$/,""); print}')
  time=$(tail -3 $temp_file | head -n1 | awk '{print $1}')

  # Verify the time elapsed to determine how many samples to measure
  echo "    - Time of the 1st running: $time"
  if [ $(echo "$time <= 60" | bc -l) -eq 1 ]; then
    # Create a CSV file for each version
    output_versionFile="$path/performance_data_${program}_$version.csv"
    touch $output_versionFile

    # Record the first measurement
    echo "    - Recording #1 turbostat data in a CSV file: $output_versionFile"
    [ -s $output_versionFile ] || echo test,python_version,appplication,time_elapsed,$col_names >> $output_versionFile
    echo "1,$python_version,$1,$time,$results" >> $output_versionFile

    for (( i=2; i<=10; i++ )); do
      # Run the turbostat function
      echo "Running Turbostat and program:"
      run_turbostat

      # Convert turbostat output to CSV format
      col_names=$(tail -2 $temp_file | head -n1 | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
      results=$(tail -1 $temp_file | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',' | awk '{gsub(/,$/,""); print}')
      time=$(tail -3 $temp_file | head -n1 | awk '{print $1}')

      # Record turbostat data in the NEW CSV file for each version
      echo "    - Recording #$i turbostat data in a CSV file: $output_versionFile"
      echo $i,$python_version,$1,$time,$results >> $output_versionFile
    done
  
    # Compute the average of each column
    avg_time=$(awk -F ',' -v col=4 'NR>1 {sum+=$col} END {print sum/(NR-1)}' "$output_versionFile")
    avg_usec=$(awk -F ',' -v col=5 'NR>1 {sum+=$col} END {print sum/(NR-1)}' "$output_versionFile")
    day=$(tail -1 $output_versionFile | awk -F ',' '{print $6}')
    avg_cols=$(awk -F',' 'NR>1{for(i=7;i<=NF;i++){sum[i-6]+=$i; count[i-6]++}} END{for(i=1;i<=NF-6;i++) printf (count[i]>0 ? "%.2f," : "NaN,"), (count[i]>0 ? sum[i]/count[i] : 0)}' "$output_versionFile" | awk '{gsub(/,$/,""); print}')

    # Record average turbostat data in the CSV file with ALL the versions
    echo "    - Recording AVG turbostat data in the general CSV file: $output_generalFile"
    col_names=$(head -1 $output_versionFile | awk -F',' '{for(i=2;i<=NF;i++) printf "%s%s", $i, (i==NF?"\n":",")}')
    [ -s $output_generalFile ] || echo $col_names >> $output_generalFile
    echo $python_version,$1,$avg_time,$avg_usec,$day,$avg_cols >> $output_generalFile

  else
    # Record turbostat data in the CSV file with ALL the versions (only once)
    echo "    - Recording AVG turbostat data in the general CSV file: $output_generalFile"
    [ -s $output_generalFile ] || echo python_version,appplication,time_elapsed,$col_names >> $output_generalFile
    echo $python_version,$1,$time,$results>> $output_generalFile
  fi

  # Remove the temporary file
  rm $temp_file

fi


# Parameters for energy, memory, cpu
# Algorithm -> Fibonnacci
# Script for analysis
# 

# NOTES: Add columns such as filename, interpreter version, 
# Add sleep mode in each testing
# Fix the other version 
# Add the last last versions
# Compare energy consumption 
# Create a script to generate a table and plots
# Select the application 


# One idea is to generate 10 samples of each testing with an interval of resting; thus we create a file with those records for each version and another file computing the average of each version
# Check the idle status to determine the time for sleeping
# Reduce the script in order to easily adapt for other programming languages


# “We only considered peak memory and not total memory, as we wish to focus on optimizing the limited resources a programmer may have: battery, time, and memory space.” 
# ([Pereira et al., 2021, p. 38](zotero://select/library/items/RH4JK86T)) ([pdf](zotero://open-pdf/library/items/S3MJQHCG?page=38&annotation=J4BGCCV6))