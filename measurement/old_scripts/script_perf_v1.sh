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

# Create and generate files and directories neededqq
output_generalPerf="$path/perf_data_allVersions.csv"
output_filePerf="$path/temp_perf_data_$version_selected.txt"
touch $output_filePerf

run_perf() {
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

    sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT"  \
        perf stat -M $metrics -e $time -e $energy -e $cpu -e $branch  \
        -e $memory -e $virtual_memory -e $cache -e $io  \
        -o $output_filePerf $command 2>&1
}

# Run perf
echo "Running Perf and program:"
run_perf

# Record perf data in the CSV file with ALL the versions (only once)
echo "    - Recording perf data in the general CSV file: $output_generalFile"
col_names=$(echo '
           CPU_Utilization,
           CPI,
           Retiring,
           Frontend_Bound,
           Bad_Speculation,
           Backend_Bound,
           ILP,
           IPC,
           Kernel_Utilization,
           L1D_Cache_Fill_BW,
           Turbo_Utilization,
           cycles,freq_cycles,
           instructions,insn_per_cycle,
           cpu_clock,no_cpus,
           cpu_cycles,freq_cpu_cycles,
           cpu_migrations,
           ref_cycles,
           bus_cycles,
           task_clock,no_cpus_task_clock,
           cpu_thermal_margin,
           branches,
           branch_misses,percent_branch_misses,
           mem_loads,
           mem_stores,
           page_faults,
           minor_faults,
           major_faults,
           cache_references,
           cache_misses,percent_cache_misses,
           L1_dcache_loads,
           L1_dcache_load_misses,percent_L1_dcache_load_misses,
           LLC_loads,
           LLC_load_misses,percent_LLC_load_misses,
           L1_icache_load_misses,
           dTLB_loads,
           dTLB_load_misses,percent_dTLB_load_misses,
           iTLB_loads,
           iTLB_load_misses,percent_iTLB_load_misses,
           block_rq_issue,
           block_rq_complete
           ' | tr -d " \t\n\r" )
results=$(awk '
              / CPU_Utilization / {CPU_Utilization=$2} \
              / CPI / {CPI=$2} \
              / Retiring / {Retiring=$2} \
              / Frontend_Bound / {Frontend_Bound=$2} \
              / Bad_Speculation / {Bad_Speculation=$2} \
              / Backend_Bound / {Backend_Bound=$2} \
              / ILP / {ILP=$2} \
              / IPC / {IPC=$2} \
              / Kernel_Utilization / {Kernel_Utilization=$2} \
              / L1D_Cache_Fill_BW / {L1D_Cache_Fill_BW=$2} \
              / Turbo_Utilization / {Turbo_Utilization=$2} \
              / cycles / && /GHz/ {cycles=$1; freq_cycles=$4; freq_unit=$5} \
              / instructions / {instructions=$1; insn_per_cycle=$4} \
              / cpu-clock / {cpu_clock=$1; cpu_clock_unit=$2; no_cpus=$5} \
              / cpu-cycles / {cpu_cycles=$1; freq_cpu_cycles=$4; freq_unit_cpu_cycles=$5} \
              / cpu-migrations / {cpu_migrations=$1} \
              / ref-cycles / {ref_cycles=$1} \
              / bus-cycles / {bus_cycles=$1} \
              / task-clock / {task_clock=$1; task_clock_unit=$2; no_cpus_task_clock=$5} \
              /cpu_thermal_margin/ {cpu_thermal_margin=$1; cpu_thermal_margin_unit=$2} \
              /  branches / {branches=$1} \
              / branch-misses / {branch_misses=$1; percent_branch_misses=$4} \
              / mem-loads / {mem_loads=$1} \
              / mem-stores / {mem_stores=$1} \
              / page-faults / {page_faults=$1} \
              / minor-faults / {minor_faults=$1} \
              / major-faults / {major_faults=$1} \
              / cache-references / {cache_references=$1} \
              / cache-misses / {cache_misses=$1; percent_cache_misses=$4} \
              / L1-dcache-loads / {L1_dcache_loads=$1} \
              / L1-dcache-load-misses / {L1_dcache_load_misses=$1; percent_L1_dcache_load_misses=$4} \
              / LLC-loads / {LLC_loads=$1} \
              / LLC-load-misses / {LLC_load_misses=$1; percent_LLC_load_misses=$4} \
              / L1-icache-load-misses / {L1_icache_load_misses=$1} \
              / dTLB-loads / {dTLB_loads=$1} \
              / dTLB-load-misses / {dTLB_load_misses=$1; percent_dTLB_load_misses=$4} \
              / iTLB-loads / {iTLB_loads=$1} \
              / iTLB-load-misses / {iTLB_load_misses=$1; percent_iTLB_load_misses=$4} \
              / block:block_rq_issue / {block_rq_issue=$1} \
              / block:block_rq_complete / {block_rq_complete=$1} \
              END{print( \
                        CPU_Utilization ";" \
                        CPI ";" \
                        Retiring ";" \
                        Frontend_Bound ";" \
                        Bad_Speculation ";" \
                        Backend_Bound ";" \
                        ILP ";" \
                        IPC ";" \
                        Kernel_Utilization ";" \
                        L1D_Cache_Fill_BW ";" \
                        Turbo_Utilization ";" \
                        cycles ";" freq_cycles " " freq_unit ";" \
                        instructions ";" insn_per_cycle ";" \
                        cpu_clock " " cpu_clock_unit ";" no_cpus ";" \
                        cpu_cycles ";" freq_cpu_cycles " " freq_unit_cpu_cycles ";" \
                        cpu_migrations ";" \
                        ref_cycles ";" \
                        bus_cycles ";" \
                        task_clock " " task_clock_unit ";" no_cpus_task_clock ";" \
                        cpu_thermal_margin " " cpu_thermal_margin_unit ";" \
                        branches ";" \
                        branch_misses ";" percent_branch_misses ";" \
                        mem_loads ";" \
                        mem_stores ";" \
                        page_faults ";" \
                        minor_faults ";" \
                        major_faults ";" \
                        cache_references ";" \
                        cache_misses ";" percent_cache_misses ";" \
                        L1_dcache_loads ";" \
                        L1_dcache_load_misses ";" percent_L1_dcache_load_misses ";" \
                        LLC_loads ";" \
                        LLC_load_misses ";" percent_LLC_load_misses ";" \
                        L1_icache_load_misses ";" \
                        dTLB_loads ";" \
                        dTLB_load_misses ";" percent_dTLB_load_misses ";" \
                        iTLB_loads ";" \
                        iTLB_load_misses ";" percent_iTLB_load_misses ";" \
                        block_rq_issue ";" \
                        block_rq_complete \
                        ) \
                 }'\
            $output_filePerf | tr -d ',' | tr ';' ',')
[ -s $output_generalPerf ] || echo version,appplication,$col_names >> $output_generalPerf
echo $confirm_version,$2,$results>> $output_generalPerf