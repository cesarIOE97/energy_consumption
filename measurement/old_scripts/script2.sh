#!/bin/bash

# Example of how to run the script
# ./script2.sh 2.7.18 "nbody.py 50000"

# See the Python versions
pyenv versions | awk '/*/{print $2} FNR>1&&!/*/{print $1}'

# Pyenv command
pyenv global $1

# Verify the Python version
python_version=$(python --version)

# Command to execute the Python program
python_command="python ${2}"

# Output file for recording turbostat data in CSV format
output_file="performance_data.csv"
temp_file="temp_performance_data.txt"
touch $temp_file

# Function to run turbostat and record data
run_turbostat() {
  # Run turbostat in the background and redirect output to a temporary file
  sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" turbostat --out $temp_file --Joules --Summary --enable all $python_command
}

# Run the turbostat function
run_turbostat

# Convert turbostat output to CSV format
#awk 'BEGIN{print "Time (sec),Avg_MHz,Busy%,Bzy_MHz,TSC_MHz,IPC,IRQ,SMI,POLL,C1,C1E,C3,C6,C7s,C8,C9,C10,POLL%,C1%,C1E%,C3%,C6%,C7s%,C8%,C9%,C10%,CPU%c1,CPU%c3,CPU%c6,CPU%c7,CoreTmp,PkgTmp,GFX%rc6,GFXMHz,GFXAMHz,Totl%C0,Any%C0,GFX%C0,CPUGFX%,Pkg%pc2,Pkg%pc3,Pkg%pc6,Pkg%pc7,Pkg%pc8,Pkg%pc9,Pk%pc10,CPU%LPI,SYS%LPI,Pkg_J,Cor_J,GFX_J,RAM_J,PKG_%,RAM_%"} {print}' temp_performance_data.txt > "$output_file"
echo "... EXTRACTING ALL INFORMATION ..."
echo $python_version
col_names=$(tail -2 $temp_file | head -n1 | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
results=$(tail -1 $temp_file | awk 'NR==1{time_elapsed=$1} {$1=$1}1' OFS=',')
time=$(tail -3 $temp_file | head -n1 | awk '{print $1}')

echo "Test"
echo $python_version

# Record turbostat data in a CSV file
[ -s $output_file ] || echo python_version,appplication,time_elapsed,$col_names
echo $python_version,$2,$time,$results

# Remove the temporary file
rm temp_performance_data.txt

# NOTES: Add columns such as filename, interpreter version, 
# Add sleep mode in each testing
# Fix the other version 
# Add the last last versions
# Compare energy consumption 
# Create a script to generate a table and plots
# Select the application 


# One idea is to generate 10 samples of each testing with an interval of resting; thus we create a file with those records for each version and another file computing the average of each version
# Check the idle status to determine the time for sleeping
