#!/bin/bash

# Command
python3 nbody.py 50000000 &

pid=$!
echo $pid

# command="python3 nbody.py 50000"

# Run turbostat in the background and redirect output to a temporary file
# sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" turbostat -S $command

# /usr/bin/time -v -p $pid

top -b -n 1 -p $PID

vmstat