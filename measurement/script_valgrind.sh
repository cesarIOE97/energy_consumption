#!/bin/bash

# NOTE: Needs the Bash script `script_menuVersions.sh` and `script_versionSelected.sh`
# Arguments (from `script_menuVersions.sh`):
# $1 -> programming language    e.g. python
# $2 -> file <arguments>        e.g. nbody.py 50000
# $3 -> folder to save data     e.g. nbody_50000

# Other attempts using the command valgrin and heaptrack, but it didn't work
# with the command python (due to it didn't change the version)

# temp_file
# command
# path
# version_selected
# $2 -> file <arguments>
# output_generalFile


# Create and generate files and directories needed
output_generalFileMemory="$path/valgrind_memory_data_allVersions.csv"
output_fileValgrind="$path/temp_valgrind_memory_data_$version_selected.txt"
touch $output_fileValgrind

run_valgrind() {
    sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" valgrind -s --leak-check=full --show-leak-kinds=all --log-file=$output_fileValgrind $command
}

# Run valgrind
echo "Running Valgrind and program:"
run_valgrind

# Record valgrind data in the CSV file with ALL the versions (only once)
echo "    - Recording valgrind data in the general CSV file: $output_generalFile"
col_names='allocs,frees,bytes_allocated,bytes_used_at_exit,total_blocks,
            bytes_definitelyLost,#blocks_definitelyLost,
            bytes_indirectlyLost,#locks_indirectlyLost,
            bytes_possiblyLost,#blocks_possiblyLost,
            bytes_reachable,#blocks_reachable,
            bytes_suppressed,#blocks_suppressed'
results=$(awk '/total heap usage/{allocs=$5; frees=$7; bytes_allocated=$9} \
            /in use at exit/{bytes_used_at_exit=$6; no_blocks_used_at_exit=$9} \
            /definitely lost/{bytes_definitely=$4; no_blocks_definitely=$7} \
            /indirectly lost/{bytes_indirectly=$4; no_blocks_indirectly=$7} \
            /possibly lost/{bytes_possibly=$4; no_blocks_possibly=$7} \
            /still reachable/{bytes_reachable=$4; no_blocks_reachable=$7} \
            /suppressed/ && /bytes/{bytes_suppressed=$3; no_blocks_suppressed=$6} \
            END{print(allocs ";" frees ";" bytes_allocated ";" bytes_used_at_exit ";" no_blocks_used_at_exit ";" bytes_definitely ";" no_blocks_definitely ";" bytes_indirectly ";" no_blocks_indirectly ";" bytes_possibly ";" no_blocks_possibly ";" bytes_reachable ";" no_blocks_reachable ";" bytes_suppressed ";" no_blocks_suppressed)}' \
            $output_fileValgrind | tr -d ',' | tr ';' ',')
echo $results
[ -s $output_generalFileMemory ] || echo version,appplication,$col_names >> $output_generalFileMemory
echo $confirm_version,$2,$results>> $output_generalFileMemory