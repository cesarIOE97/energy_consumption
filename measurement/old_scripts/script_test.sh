#!/bin/bash

# Command to measure
YOUR_COMMAND=$1

# Function to measure CPU usage
measure_cpu() {
    top -b -d 1 -n 1 | grep "%Cpu" | awk '{print "CPU Usage: " 100-$8 "%"}'
}

# Function to measure memory usage
measure_memory() {
    echo "Memory Usage:"
    ps -p $1 -o rss=
}

# Function to measure energy consumption
measure_energy() {
    echo "Energy Consumption:"
    sudo powertop --csv | awk -F',' '{print "Energy: " $11 " mW"}'
}

# Execute the command in the background
$YOUR_COMMAND &
COMMAND_PID=$!

# Measure performance metrics
measure_cpu
measure_memory $COMMAND_PID
measure_energy

# Terminate the command
kill $COMMAND_PID
