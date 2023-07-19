#!/bin/bash

# Example to use this script
# ./index.sh "nbody.py 50000000" "nbody_50000000"
# ./index.sh "<file arguments>" "<path or folder or directory>"

# Arguments:
# $1 -> file <arguments>        e.g. nbody.py 50000
# $2 -> folder to save data     e.g. nbody_50000

# Show Aalto logo
./logo.sh

# MENU
echo "Available programming languages are the next ones:"
echo "  - python"
echo "  - c++"
echo "  - c"
echo -n "
 *** Type the version (for example 'python' or 'c++'): "
read language

# Selection of programming language
if [ $language == 'python' ] || [ $language == 'PYTHON' ] || [ $language == 'Python' ] ; then
    ./script_menuVersions.sh "python" "$1" "$2"
elif [ $language == 'c++' ] || [ $language == 'C++' ] ; then
    ./script_menuVersions.sh "c++" "$1" "$2"
elif [ $language == 'c' ] || [ $language == 'C' ] ; then
    ./script_menuVersions.sh "c" "$1" "$2"
fi
