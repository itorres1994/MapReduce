import random

line_number = 0
longitude = [42.1015, 22.9068, 51.5074]  # each one of these relates to a continent
# North America, South America, etc...
latitude = [72.5898, 43.1729, 0.1278]  # each one of these relates to a continent
# North America, South America, etc...
continent = ['North America', 'South America', 'Europe']
randoms = [40, 50, 500]  # These are the sizes of the temperature readings for the years (2016, 2015, 2014)
years = ['2016', '2015', '2014']
ranYear = 0
ranMonth = 0
ranDay = 0
ranContinent = 0
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = [[1, 31], [1, 28], [1, 30]]
count2016 = 0
count2015 = 0
count2014 = 0
countNorthAmerica = [0, 0, 0]
countSouthAmerica = [0, 0, 0]
countEurope = [0, 0, 0]
fp = open('tempdataAvg3.txt', 'w')
fp.write('')
fp.close()
fp = open('tempdataAvg3.txt', 'a')

for i in range(0, randoms[2], 1):
    ranContinent = random.randint(0, 2)
    ranYear = random.randint(0, 2)
    if ranYear == 0 and ranContinent == 0:
        count2016 += 1
        countNorthAmerica[0] += 1  # 2016 count
    elif ranYear == 0 and ranContinent == 1:
        count2016 += 1
        countSouthAmerica[0] += 1  # 2015 count
    elif ranYear == 0 and ranContinent == 2:
        count2016 += 1
        countEurope[0] += 1  # 2014 count
    if ranYear == 1 and ranContinent == 0:
        count2015 += 1
        countNorthAmerica[1] += 1
    elif ranYear == 1 and ranContinent == 1:
        count2015 += 1
        countSouthAmerica[1] += 1
    elif ranYear == 1 and ranContinent == 2:
        count2015 += 1
        countEurope[1] += 1
    elif ranYear == 2 and ranContinent == 0:
        count2014 += 1
        countNorthAmerica[2] += 1
    elif ranYear == 2 and ranContinent == 1:
        count2014 += 1
        countSouthAmerica[2] += 1
    elif ranYear == 2 and ranContinent == 2:
        count2014 += 1
        countEurope[2] += 1
    ranMonth = random.randint(0, 11)
    if ranMonth == 0 or ranMonth == 2 or ranMonth == 4 or ranMonth == 6 or ranMonth == 8 or ranMonth == 10:
        ranDay = random.randint(days[0][0], days[0][1])
    elif ranMonth == 1:
        ranDay = random.randint(days[1][0], days[1][1])
    else:
        ranDay = random.randint(days[2][0], days[2][1])
    string ='%d,%f,%f,%s,%s,%d,%s,%d\n' %(line_number, longitude[0], latitude[0], continent[
        ranContinent], months[ranMonth], ranDay, years[ranYear], random.randint(-10, 30))
    fp.write(string)
    line_number += 1

print 'Count of 2016 -> ', count2016, ' , ', 'Count of 2015 -> ', count2015, ' , ', 'Count of 2014 -> ', count2014
print 'Count of North America(2016) -> ', countNorthAmerica[0], '\n', 'Count of South America(2016) -> ', \
    countSouthAmerica[0], '\n', 'Count of Europe(2016) -> ', countEurope[0]
print 'Count of North America(2015) -> ', countNorthAmerica[1], '\n', 'Count of South America(2015) -> ', \
    countSouthAmerica[1], '\n', 'Count of Europe(2015) -> ', countEurope[1]
print 'Count of North America(2014) -> ', countNorthAmerica[2], '\n', 'Count of South America(2014) -> ', \
    countSouthAmerica[2], '\n', 'Count of Europe(2014) -> ', countEurope[2]
