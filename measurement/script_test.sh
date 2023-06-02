#!/bin/bash

time=60

if (( time <= 60 )); then
    for (( i=1; i<=10; i++ )); do
      echo "Loop iteration: $i"
    done
else
    echo "bye"
fi