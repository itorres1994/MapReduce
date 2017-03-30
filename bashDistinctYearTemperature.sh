#!/bin/bash

# To run this program simply give the bash script some files as command line arguments
# e.g. ./bashDistinctYearTemperatureData.sh tempdata.txt tempdata2.txt tempdata3.txt tempdata4.txt

echo "" > outputDistinctYearTemperature.txt
echo "Cleared outputDistinctYearTemperature.txt"
echo ""
for i in "$@" # run through all of the command line arguments
do
echo "" >> outputDistinctYearTemperature.txt
echo "$i"
echo "$i" >> outputDistinctYearTemperature.txt
python MRTemperatureObservations.py $i >> outputDistinctYearTemperature.txt #use the command line arguments and give it as an argument for the python script
echo ""
done # finish looping
echo ""
echo ""
echo ""
echo "This is the contents of the outputDistinctYearTemperature.txt file..."
echo ""
cat outputDistinctYearTemperature.txt
