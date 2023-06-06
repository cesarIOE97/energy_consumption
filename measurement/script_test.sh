#!/bin/bash

output_generalFile="nbody/performance_data_allVersions_TEST_nbody.csv"
output_versionFile="nbody/performance_data_nbody_2.5.6.csv"
python_version="HOLA"

# Compute the average of each column
avg_time=$(awk -F ',' -v col=4 'NR>1 {sum+=$col} END {print sum/(NR-1)}' "$output_versionFile")
avg_usec=$(awk -F ',' -v col=5 'NR>1 {sum+=$col} END {print sum/(NR-1)}' "$output_versionFile")
day=$(tail -1 $output_versionFile | awk -F ',' '{print $6}')
avg=$(awk -F',' 'NR>1{for(i=5;i<=NF;i++){sum[i-4]+=$i; count[i-4]++}} END{for(i=1;i<=NF-4;i++) printf (count[i]>0 ? "%.2f," : "NaN,"), (count[i]>0 ? sum[i]/count[i] : 0)}' "$output_versionFile")

# Record average turbostat data in the CSV file with ALL the versions
echo "- Recording turbostat data in a CSV file"
col_names=$(head -1 $output_versionFile | awk -F',' '{for(i=7;i<=NF;i++) printf "%s%s", $i, (i==NF?"\n":",")}')
[ -s $output_generalFile ] || echo python_version,appplication,time_elapsed,$col_names >> $output_generalFile
echo $python_version,GGEG,$avg_time,$avg_usec,$day,$avg >> $output_generalFile