Ian Torres



12/12/2016



CICS 345

Homework 11: Extra Credit



I have prepared the MapReduce implementation as specified by the Extra Credit instructions.


The following shell scripts run the python implementations of problems 1(a), 2(a), and 2(b) respectively:



problem 1(a): These sample text files contain only words and no symbols
 the following output is the mapping of the text file's name 
              along with
 the distinct words that are contained within it as a list



Command to run in Bash Terminal (must be in the MapReduce project file):
	
              ./bashInvertedIndex.sh sample.txt sample2.txt sample3.txt



Transcript of the output:
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.120000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.120000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.120000...

No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.397000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.397000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.397000...

No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.653000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.653000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRInvertedIndex.Ian Torres.20161212.210834.653000...




This is the contents of the outputInvertedIndex.txt file...



sample.txt
"a"     ["www.yellowhelloworld.com", "www.worldhello.com", "www.helloworld.com"]
"are"   ["www.lastbutnotleast.com"]
"by"    ["www.lastbutnotleast.com"]
"come"  ["www.lastbutnotleast.com"]
"different"     ["www.yellowhelloworld.com"]
"file"  ["www.worldhello.com", "www.helloworld.com"]
"good"  ["www.yellowhelloworld.com", "www.lastbutnotleast.com"]
"hard"  ["www.lastbutnotleast.com"]
"hello" ["www.helloworld.com"]
"is"    ["www.yellowhelloworld.com", "www.worldhello.com", "www.helloworld.com"]
"text"  ["www.yellowhelloworld.com"]
"the"   ["www.worldhello.com"]
"thing" ["www.yellowhelloworld.com"]
"things"        ["www.lastbutnotleast.com"]
"this"  ["www.worldhello.com", "www.helloworld.com"]
"to"    ["www.lastbutnotleast.com", "www.worldhello.com"]
"world" ["www.worldhello.com", "www.helloworld.com"]

sample2.txt
"friend"        ["www.thisisanotherwebsite.com"]
"from"  ["www.thisisanotherwebsite.com"]
"fun"   ["www.wowawebsite.com"]
"good"  ["www.thisisanotherwebsite.com"]
"is"    ["www.wowawebsite.com", "www.thisisawebsite.com"]
"more"  ["www.thisisawebsite.com"]
"our"   ["www.thisisanotherwebsite.com"]
"python"        ["www.wowawebsite.com", "www.thisisanotherwebsite.com"]
"sample"        ["www.thisisawebsite.com"]
"text"  ["www.wowawebsite.com", "www.thisisawebsite.com"]
"this"  ["www.wowawebsite.com", "www.thisisawebsite.com"]

sample3.txt
"another"       ["www.morewebsites.com"]
"bash"  ["www.onwardtovictory.com"]
"can"   ["www.runningoutofnames.com"]
"example"       ["www.morewebsites.com"]
"files" ["www.onwardtovictory.com"]
"for"   ["www.morewebsites.com"]
"is"    ["www.morewebsites.com"]
"it"    ["www.runningoutofnames.com"]
"map"   ["www.morewebsites.com"]
"multiple"      ["www.onwardtovictory.com"]
"on"    ["www.onwardtovictory.com"]
"program"       ["www.runningoutofnames.com"]
"python"        ["www.runningoutofnames.com"]
"reduce"        ["www.runningoutofnames.com"]
"scripting"     ["www.onwardtovictory.com"]
"show"  ["www.runningoutofnames.com"]
"that"  ["www.runningoutofnames.com"]
"the"   ["www.morewebsites.com"]
"this"  ["www.morewebsites.com"]
"to"    ["www.runningoutofnames.com"]
"using" ["www.onwardtovictory.com"]
"work"  ["www.runningoutofnames.com"]
"yet"   ["www.morewebsites.com"]


//////////////////////////////////////////////////////////


problem 2(a): These sample text files contain temperature readings that consist of the problems input structure
	      (line-number, longitude, latitude, continent, month, day, year, temp)

Command to run in Bash Terminal (must be in the MapReduce project file):
	      ./bashDistinctYearTemperature.sh tempdata.txt tempdata2.txt tempdata3.txt

Transcript of the output:
Cleared outputDistinctYearTemperature.txt

tempdata.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.390000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.390000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.390000...

tempdata2.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.656000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.656000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.656000...

tempdata3.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.933000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.933000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations.Ian Torres.20161212.182455.933000...




This is the contents of the outputDistinctYearTemperature.txt file...



tempdata.txt
" 2014 "        101
" 2016 "        101

tempdata2.txt
" 2015 "        150

tempdata3.txt

//////////////////////////////////////////////////////////

problem 2(b): These sample text files contain temperature readings that consist of the problems input structure
	      (line-number, longitude, latitude, continent, month, day, year, temp)

Command to run in Bash Terminal (must be in the MapReduce project file):
	      ./bashAverageContinentTemperature.sh tempdataAvg.txt tempdataAvg2.txt tempdataAvg3.txt

Transcript of the output:
Cleared outputAverageContinentTemperature.txt...

tempdataAvg.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.238000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.238000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.238000...

tempdataAvg2.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.503000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.503000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.503000...

tempdataAvg3.txt
No configs found; falling back on auto-configuration
Creating temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.780000
Running step 1 of 1...
Streaming final output from c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.780000\output...
Removing temp directory c:\users\iantor~1\appdata\local\temp\MRTemperatureObservations2.Ian Torres.20161212.182919.780000...




This is the contents of the outputAverageContinentTemperature.txt file...



tempdataAvg.txt
["Europe", "2014"]      9.04
["Europe", "2015"]      12.52
["Europe", "2016"]      10.96
["North America", "2014"]       8.3
["North America", "2015"]       8.54
["North America", "2016"]       10.11
["South America", "2014"]       10.24
["South America", "2015"]       10.36

tempdataAvg2.txt
["Europe", "2014"]      10.47
["Europe", "2016"]      10.88
["North America", "2014"]       9.08
["North America", "2015"]       9.79
["North America", "2016"]       12.31
["South America", "2015"]       6.85
["South America", "2016"]       7.98

tempdataAvg3.txt
["Europe", "2014"]      12.09
["Europe", "2015"]      12.38
["Europe", "2016"]      9.79
["North America", "2014"]       9.78
["North America", "2015"]       8.71
["North America", "2016"]       9.85
["South America", "2015"]       8.27
["South America", "2016"]       8.39




To make grading easier here is the individual counts:

tempdataAvg.txt
Count of 2016 -> 162, Count of 2015 -> 180, Count of 2014 -> 158

Count of North America(2016) -> 66
Count of South America(2016) -> 43
Count of Europe(2016) -> 53

Count of North America(2015) -> 57
Count of South America(2015) -> 61
Count of Europe(2015) -> 62

Count of North America(2014) -> 56
Count of South America(2014) -> 51
Count of Europe(2014) -> 51

tempdataAvg2.txt
Count of 2016 -> 185, Count of 2015 -> 153, Count of 2014 -> 162

Count of North America(2016) -> 59
Count of South America(2016) -> 57
Count of Europe(2016) -> 69

Count of North America(2015) -> 53
Count of South America(2015) -> 53
Count of Europe(2015) -> 47

Count of North America(2014) -> 60
Count of South America(2014) -> 49
Count of Europe(2014) -> 53

tempdataAvg3.txt
Count of 2016 -> 175, Count of 2015 -> 171, Count of 2014 -> 154

Count of North America(2016) -> 62
Count of South America(2016) -> 57
Count of Europe(2016) -> 56

Count of North America(2015) -> 59
Count of South America(2015) -> 51
Count of Europe(2015) -> 61

Count of North America(2014) -> 51
Count of South America(2014) -> 48
Count of Europe(2014) -> 55

**********************************************************************

Files used:

Problem 1(a): bashInvertedIndex.sh, sample.txt, sample2.txt, sample3.txt, MRInvertedIndex.py

Problem 2(a): bashDistinctYearTemperature.sh, tempdata.txt, tempdata2.txt, tempdata3.txt, tempdata4.txt, MRTemperatureObservations.py

Problem 2(b): bashAverageContinentTemperature.sh, tempdataAvg.txt, tempdataAvg2.txt, tempdataAvg3.txt, MRTemperatureObservations2.py

