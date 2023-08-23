#!/bin/bash

# Example to use this script
# ./script_menuVersions.sh "python" "nbody.py 50000000" "nbody_50000000"
# ./script_menuVersions.sh "<file arguments>" "<path or folder or directory>"

# Arguments:
# $1 -> programming language    e.g. python
# $2 -> file <arguments>        e.g. nbody.py 50000
# $3 -> folder to save data     e.g. nbody_50000

# Extract all versions according to the programming language
if [ $1 == 'c' ] ; then
    readarray -t versions_list < <(compgen -A command gcc | grep -wv -e gcc-nm -e gcc-ranlib -e gcc-ar | sort -u | grep gcc-)
elif [ $1 == 'c++' ] ; then
    readarray -t versions_list < <(compgen -A command g++ | sort -V | uniq| grep g++-)
elif [ $1 == 'python' ] ; then
    readarray -t versions_list < <(pyenv versions | awk '/*/{print $2} FNR>1&&!/*/{print $1}')
elif [ $1 == 'java' ] ; then
    readarray -t versions_list < <(sudo update-alternatives --display java | awk '/priority/{print $1}' | grep -oP '/usr/lib/jvm/\K\java-\K\d+|jdk-\K\d+' | sort -V)
elif [ $1 == 'js' ] ; then
    source /u/13/olverac1/unix/.nvm/nvm.sh
    readarray -t versions_list < <(nvm ls | awk '{print $2}' | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+')
fi

# MENU
echo ""
echo "Available $1 versions are the next ones:"
for version in "${versions_list[@]}"; do
    echo "  - $version"
done
echo -n "  - all

 *** Type the version (for example '$versions_list', or 'all' to measure all $1 versions): "
read version_selected

# Extract information from the arguments ($2 = file <arguments>)
filename_program=$(echo $2 | awk '{print $1}')
filename_program_woExtension=$(echo $2 | awk -F. '{print $1}')
arguments=$(echo $2 | awk '{ for (i = 2; i <= NF; i++) print $i }')

# Path to save all data according to the programming language and program
path=$1/$3
[ -d $path ] || mkdir $path

# Selection of the versions
if [ $version_selected == 'all' ] || [ $version_selected == 'All' ] || [ $version_selected == 'ALL' ]; then

    flag=0

    echo -n "
    *** Run for 'all' versions or starting FROM a specific version (for example '$versions_list', or 'all' to measure all $1 versions): "
    read from_version

    # Analize each version of the selected programming language (running, measuring, )
    for version_selected in "${versions_list[@]}"; do
        if [ $from_version == $version_selected ]; then
            flag=1
        elif [ $from_version == 'all' ] || [ $from_version == 'All' ] || [ $from_version == 'ALL' ]; then
            flag=1
        fi
        if [ $flag -eq 1 ]; then
            # echo "CHECKING VERSIONS"
            . ./script_versionSelected.sh
        fi
    done

else
    . ./script_versionSelected.sh
fi

# Python script
pyenv global 3.11.3
python3 analysis.py $1 "$2" $3
python3 analysis_general.py