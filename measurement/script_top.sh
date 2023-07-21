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
pathTop=$path/top
[ -d $pathTop ] || mkdir $pathTop
output_generalTop="$pathTop/top_data_allVersions.csv"
output_fileTop="$pathTop/temp_top_data_$version_selected.csv"
touch $output_fileTop

run_command() {
    time="duration_time"
    energy="power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/"
    cpu="cycles,instructions,cpu-clock,cpu-cycles,cpu-migrations,ref-cycles,bus-cycles,task-clock,msr/cpu_thermal_margin/"
    branch="branches,branch-misses"
    switch="context-switches"
    memory="mem-loads,mem-stores"
    virtual_memory="page-faults,minor-faults,major-faults"
    cache="cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,LLC-loads,LLC-load-misses,L1-icache-load-misses,dTLB-loads,dTLB-load-misses,iTLB-loads,iTLB-load-misses"
    io="block:block_rq_issue,block:block_rq_complete"
    metrics="CPU_Utilization,CPI,Retiring,Frontend_Bound,Bad_Speculation,Backend_Bound,ILP,IPC,Kernel_Utilization,L1D_Cache_Fill_BW,L2_Cache_Fill_BW,L3_Cache_Fill_BW,Turbo_Utilization"

    $command 2>&1 &
}

# Function to get memory usage of a process by its PID
function get_top_data() {
    pid=$1
    timestamp=$(date +%s)
    results=$(top -b -n 1 | awk -v pid=$pid -v timestamp=$timestamp ' \
        $1==pid{virt=$5; res=$6; shr=$7; percent_cpu=$9; percent_mem=$10; command=$12} \
        /Tasks:/{tasks_total=$2; tasks_running=$4; tasks_sleeping=$6; tasks_stopped=$8; tasks_zombie=$10} \
        /%Cpu/{cpu_us=$2; cpu_sy=$4; cpu_ni=$6; cpu_id=$8; cpu_wa=$10; cpu_hi=$12; cpu_si=$14; cpu_st=$16} \
        /Mem :/{mem_unit=$1; mem_total=$4; mem_free=$6; mem_used=$8; mem_buff_cache=$10} \
        /Swap:/{swap_unit=$1; swap_total=$3; swap_free=$5; swap_used=$7; swap_avail=$9} \
        END{print( \
                    timestamp "," pid "," command \
                    "," virt "," res "," shr "," percent_cpu "," percent_mem \
                    "," tasks_total "," tasks_running "," tasks_sleeping "," tasks_stopped "," tasks_zombie \
                    "," cpu_us "," cpu_sy "," cpu_ni "," cpu_id "," cpu_wa "," cpu_hi "," cpu_si "," cpu_st \
                    "," mem_total " " mem_unit "," mem_free " " mem_unit "," mem_used " " mem_unit "," mem_buff_cache " " mem_unit \
                    "," swap_total " " swap_unit "," swap_free " " swap_unit "," swap_used " " swap_unit "," swap_avail " " swap_unit \
                 ) \
        }')
    echo $results
}

# Run command to monitor it by its PID
echo "Running the program for monitoring using 'top':"
run_command
pid=$!

# Monitor memory usage and other parameters until the Python program ends
echo "Monitoring memory usage of process with PID $pid..."

col_names=$(echo '
        no_measurement,
        timestamp,pid,command,
        virt,res,shr,percent_cpu,percent_mem,
        tasks_total,tasks_running,tasks_sleeping,tasks_stopped,tasks_zombie,
        cpu_us,cpu_sy,cpu_ni,cpu_id,cpu_wa,cpu_hi,cpu_si,cpu_st,
        mem_total,mem_free,mem_used,mem_buff_cache,
        swap_total,swap_free,swap_used,swap_avail,
        ' | tr -d " \t\n\r" )
[ -s $output_fileTop ] || echo version,appplication,$col_names >> $output_fileTop

count=0

while kill -0 $pid 2>/dev/null; do
    new_row=$(get_top_data $pid)
    echo $confirm_version,$2,$count,$new_row >> $output_fileTop
    sleep 1
    ((count++))
done

echo "Python program with PID $pid has ended. Monitoring stopped."