#!/bin/bash

# To run this program simply give the bash script some files as command line arguments
# e.g. ./bashInvertedIndex.sh sample.txt sample2.txt sample3.txt (and so on)
# it will work with however many files you give it (with a minimum of one file of course)

echo "" > outputInvertedIndex.txt # clear all contents of the output.txt file
echo "Cleared outputInvertedIndex.txt contents..."
echo ""
for i in "$@" # run through all of the command line arguments
do
echo "" >> outputInvertedIndex.txt
echo "$i" >> outputInvertedIndex.txt
python MRInvertedIndex.py $i >> outputInvertedIndex.txt # use the command line arguments and give it as an argument for the python script
echo ""
done # finish looping
echo ""
echo ""
echo ""
echo "This is the contents of the outputInvertedIndex.txt file..."
echo ""
cat outputInvertedIndex.txt
