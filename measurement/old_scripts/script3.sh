#!/bin/bash

# Define the Python script to be analyzed
python_script="nbody.py"

# Function to calculate memory usage in MB
get_memory_usage() {
    pid=$1
    memory_usage=$(pmap -x "$pid" | tail -1 | awk '{print $4}')
    #memory_usage_mb=$((memory_usage / 1024))
    echo "$memory_usage"
}

# Run the Python script in the background
python3 "$python_script" 500000 &
pid=$!

# Monitor memory usage while the script is running
while ps -p "$pid" > /dev/null; do
    memory_usage=$(get_memory_usage "$pid")
    echo "$(date +%H:%M:%S) Memory Usage: $memory_usage MB"
    sleep 1
done

# Wait for the Python script to finish
wait "$pid"

# Get the final memory usage
memory_usage=$(get_memory_usage "$pid")
echo "Final Memory Usage: $memory_usage MB"
