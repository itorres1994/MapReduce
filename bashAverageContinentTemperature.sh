#!/bin/bash

# To run this program simply give the bash script some files as command line arguments
# e.g. ./bashAverageContinentTemperature.sh tempdataAvg.txt tempdataAvg2.txt tempdataAvg3.txt tempdataAvg4.txt
# it will work with however many files you give it (with a minimum of one file of course)

echo "" > outputAverageContinentTemperature.txt # clear all contents of the output file
echo "Cleared outputAverageContinentTemperature.txt..."
echo ""
for i in "$@" # run through all of the command line arguments
do
echo "" >> outputAverageContinentTemperature.txt
echo "$i"
echo "$i" >> outputAverageContinentTemperature.txt
python MRTemperatureObservations2.py $i >> outputAverageContinentTemperature.txt # use the command line arguments and give it as an argument for the python script
echo ""
done # finish looping
echo ""
echo ""
echo ""
echo "This is the contents of the outputAverageContinentTemperature.txt file..."
echo ""
cat outputAverageContinentTemperature.txt
