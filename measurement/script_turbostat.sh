#!/bin/bash

# NOTE: Needs the Bash script `script_menuVersions.sh` and `script_versionSelected.sh`
# Arguments (from `script_menuVersions.sh`):
# $1 -> programming language    e.g. python
# $2 -> file <arguments>        e.g. nbody.py 50000
# $3 -> folder to save data     e.g. nbody_50000

# temp_file
# command
# path
# version_selected
# $2 -> file <arguments>
# output_generalFile

# Create and generate files and directories needed
pathTurbostat=$path/turbostat
[ -d $pathTurbostat ] || mkdir $pathTurbostat
output_generalFile="$pathTurbostat/turbostat_performance_data_allVersions.csv"
temp_file="$pathTurbostat/temp_turbostat_performance_data.txt"
touch $temp_file

run_turbostat() {
    sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" turbostat --out $temp_file --Joules --Summary --enable all $command
}

# Run turbostat
echo "Running Turbostat and program:"
run_turbostat

# Convert turbostat output to CSV format
col_names=$(tail -2 $temp_file | head -n1 | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
results=$(tail -1 $temp_file | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',' | awk '{gsub(/,$/,""); print}')
time=$(tail -3 $temp_file | head -n1 | awk '{print $1}')

# Verify the time elapsed to determine how many samples to measure
echo
echo "    - Time of the 1st running: $time"
if [ $(echo "$time <= 60" | bc -l) -eq 1 ]; then
    # Create a CSV file for each version
    output_versionFile="$pathTurbostat/turbostat_performance_data_$version_selected.csv"
    touch $output_versionFile

    # Record the first measurement
    echo "    - Recording #1 turbostat data in a CSV file: $output_versionFile"
    [ -s $output_versionFile ] || echo test,version,appplication,time_elapsed,$col_names >> $output_versionFile
    echo "1,$confirm_version,$2,$time,$results" >> $output_versionFile

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
        echo $i,$confirm_version,$2,$time,$results >> $output_versionFile
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
    echo $confirm_version,$2,$avg_time,$avg_usec,$day,$avg_cols >> $output_generalFile

else
    # Record turbostat data in the CSV file with ALL the versions (only once)
    echo "    - Recording turbostat data in the general CSV file: $output_generalFile"
    [ -s $output_generalFile ] || echo version,appplication,time_elapsed,$col_names >> $output_generalFile
    echo $confirm_version,$2,$time,$results>> $output_generalFile
fi

# Remove the temporary file
rm $temp_file