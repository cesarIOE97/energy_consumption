#!/bin/bash

# Define the events to measure (replace with your desired events)
events="power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/"
energy=",cycles,instructions"

# Define the command to execute for the coding test (replace with your test command)
test_command="python3 my_script.py"

# Define the command to execute for the performance analysis
perf_command="perf stat -e "$events""$energy" "$test_command""

# Run the perf command and capture the output
perf_output=$(eval "$perf_command" 2>&1)

echo $perf_output

# Parse the relevant data from the perf output
time_elapsed=$(echo "$perf_output" | grep "time elapsed" | awk '{print $1}')
# Energy data
energy_cores=$(echo "$perf_output" | grep "energy-cores" | awk '{print $1}')
energy_ram=$(echo "$perf_output" | grep "energy-ram" | awk '{print $1}')
energy_gpu=$(echo "$perf_output" | grep "energy-gpu" | awk '{print $1}')
energy_pkg=$(echo "$perf_output" | grep "energy-pkg" | awk '{print $1}')
energy_psys=$(echo "$perf_output" | grep "energy-psys" | awk '{print $1}')
# CPU

# Memory


# cycles=$(echo "$perf_output" | grep "cycles" | awk '{print $1}')
# instructions=$(echo "$perf_output" | grep "instructions" | awk '{print $1}')

# # Define the output CSV file path
echo "time_elapsed (secs), energy_cores (Joules), energy_ram (Joules), energy_gpu (Joules), energy_pkg (Joules), energy_psys (Joules)"
echo $time_elapsed, $energy_cores, $energy_ram, $energy_gpu, $energy_pkg, $energy_psys
# output_file="perf_analysis.csv"

# Create the CSV file and write the data
# echo "Cycles,Instructions" > "$output_file"
# echo "$cycles,$instructions" >> "$output_file"

# echo "Performance analysis data written to $output_file"
