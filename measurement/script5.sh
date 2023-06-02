#!/bin/bash

# Example to use this script
# ./script4.sh "nbody.py 50000"
# ./script4.sh "<python_file arguments>"

# Save all Python versions through the pyenv command in a list variable
readarray -t versions < <(pyenv versions | awk '/*/{print $2} FNR>1&&!/*/{print $1}')

# Output file for recording turbostat data in CSV format
program=$(echo $1 | awk -F. '{print $1}')
output_generalFile="performance_data_allVersions_$program.csv"
echo $output_generalFile
temp_file="temp_performance_data.txt"
touch $temp_file
free -h

# Command to execute the Python program in each version
python_command="python ${1}"
echo "            --- Analysing the Python program: $1 ---"

# Analize each Python version
for version in "${versions[@]}"; do
  # Set the version to analyze
  pyenv global $version

  # Verify the Python version
  python_version=$(python --version 2>&1)
  echo 
  echo "    ... Analysing Python $python_version ..."

  # Sleep for 2 mins to allow a cool-down and in turn affect energy measurements (which are suceptible to this)
  # ** CLEAR THE MEMORY
  # sleep 2m

  # Function to run turbostat and record data in temp_file
  run_turbostat() {
    # Run turbostat in the background and redirect output to a temporary file
    sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" turbostat --out $temp_file --Joules --Summary --enable all $python_command
  }

  # Run the turbostat function
  echo "- Running turbostat and Python program"
  run_turbostat
  
  # Convert turbostat output to CSV format
  echo "- Converting turbostat output into CSV formal"
  col_names=$(tail -2 $temp_file | head -n1 | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
  results=$(tail -1 $temp_file | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
  time=$(tail -3 $temp_file | head -n1 | awk '{print $1}')

  # Verify the time elapsed to determine how many samples to measure
  if (( time <= 60 )); then
    for (( i=1; i<=10; i++ )); do
      echo "Loop iteration: $i"
      
      # Create a CSV file for each version

      # Record turbostat data in the NEW CSV file for each version

      

    done
  else
    # Record turbostat data in a CSV file
    echo "- Recording turbostat data in a CSV file"
    [ -s $output_generalFile ] || echo python_version,appplication,time_elapsed,$col_names >> $output_generalFile
    echo $python_version,$1,$time,$results >> $output_generalFile
  fi
done

# Remove the temporary file
rm $temp_file

free -h