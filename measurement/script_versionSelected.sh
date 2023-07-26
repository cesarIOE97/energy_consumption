#!/bin/bash

# NOTE: Needs the Bash script `script_menuVersions.sh`

# Arguments (from `script_menuVersions.sh`):
# $1 -> programming language    e.g. python
# $2 -> file <arguments>        e.g. nbody.py 50000
# $3 -> folder to save data     e.g. nbody_50000

# Change and verify the version of the programming language
if [ $1 == 'c' ] ; then
    confirm_version=$($version_selected --version | awk 'NR==1' | awk '{print $1, $4}')
elif [ $1 == 'c++' ] ; then
    confirm_version=$($version_selected --version | awk 'NR==1' | awk '{print $1, $4}')
elif [ $1 == 'python' ] ; then
    pyenv global $version_selected
    confirm_version=$(python --version 2>&1)
fi
echo
echo "        ... Analysing $confirm_version ..."

# Run commands turbostat, time,
if [ $1 == 'c' ] ; then
    # gcc-11 c++/nbody.c -o c++/test/nbody_g++-11     
    $version_selected $1/$filename_program -o $path/${filename_program_woExtension}_$version_selected
    command="./${path}/${filename_program_woExtension}_$version_selected $arguments"
elif [ $1 == 'c++' ] ; then
    # g++-11 c++/nbody.c -o c++/test/nbody_g++-11
    $version_selected $1/$filename_program -o $path/${filename_program_woExtension}_$version_selected
    command="./$path/${filename_program_woExtension}_$version_selected $arguments"
elif [ $1 == 'python' ] ; then
    # python nbody.py 50000
    command="python $1/$2"
fi

# Sleep for 2 mins to allow a cool-down and in turn affect energy measurements (which are suceptible to this)
# ** CLEAR THE MEMORY COMMAND **
# sleep 2m

# Run measurement tools
sleep 2m
. ./script_turbostat.sh
sleep 2m
. ./script_perf.sh 
sleep 2m
. ./script_top.sh
# . ./script_valgrind.sh 
