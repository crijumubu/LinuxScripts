#!/bin/bash

# Use: ./createFiles.sh + fileName + extension + number + directoryRoute

error() {
    echo $1
    exit 1
}

if [ $# -ne 4 ]; then
    error "Use: ./createFiles.sh + fileName + extension + number + directoryRoute"
fi

if [ ! -d $4 ]; then
    error "Error: the directory does not exist"
fi

if [ $3 -lt 1 ]; then
    error "Error: the number of files can not be lower than 1"
fi

for (( i = 1; i <= $3; i++ )); do

    name="$4/$1$i.$2"

    if [ $i -lt 10 ]; then
        name="$4/$10$i.$2"
    else
        name="$4/$1$i.$2"
    fi

    touch $name

done

echo "Work done!"

#   NOTE: THIS CODE WAS ORIGINALLY CREATED BY ANTONIO SAROSI IN THE LINUX COURSE BUT I'VE MODIFIED IT SOME DETAILS