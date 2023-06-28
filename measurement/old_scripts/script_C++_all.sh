#!/bin/bash

# Example to use this script
# ./script_C++_all.sh "nbody.py 50000000" "nbody_50000000"
# ./script_C++_all.sh "<c++_file arguments>" "<path or folder or directory>"

# Save all GCC versions through the pyenv command in a list variable
readarray -t versions < <(compgen -A command gcc | grep -wv -e gcc-nm -e gcc-ranlib -e gcc-ar | sort -u | grep gcc-)
echo "Running script_C++_all.sh $1 $2"

# Output file for recording turbostat data in CSV format
program=$(echo $1 | awk -F. '{print $1}')
path="c++/$2"
[ -d $path ] || mkdir $path
output_generalFile="$path/performance_data_allVersions_$program.csv"
temp_file="$path/temp_performance_data.txt"

# Command to execute the C++ program in each version
echo
echo "  *** Analysing the C++ program: $1 ***"
echo "  *** Recording the measurenments in the CSV file: $output_generalFile ..."

# Analize each Python version
for version in "${versions[@]}"; do
  echo $version

  # Remove the temporary file
  # rm $temp_file
done