#!/bin/bash
if [ $# -eq 0 ]
    then
    echo "usage: cachesim filename"
    exit 1
fi

python3 cachesim.py $1 1048576 64 16
