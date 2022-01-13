#!/bin/bash

# Use: ./renameFiles.sh + directoryRoute + newName

error() {
    echo $1
    exit 1
}

if [ $# -ne 2 ]; then
    error "Use: ./renameFiles.sh + directoryRoute + newName"
fi

if [ ! -d $1 ]; then
    error "Error: the directory does not exist"
fi  

((cont = 1))

for file in `ls $1`; do

    absoluteFileRoute="$1/$file"

    if [ -f $absoluteFileRoute ]; then

        fileExtension=${file##*.}

        if [ $cont -lt 10 ]; then
            newAbsoluteFileRoute="$1/$20$cont.$fileExtension"
        else
            newAbsoluteFileRoute="$1/$2$cont.$fileExtension"
        fi

        
        if [ $absoluteFileRoute != $newAbsoluteFileRoute ]; then
           mv $absoluteFileRoute $newAbsoluteFileRoute
        fi

        (( cont = $cont + 1))

    fi

done 

echo "Work done!"