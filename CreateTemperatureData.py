import random

# This is a very lazy generating program, but I did not want to make too elaborate of a program
# Running the program is like thus: ./CreateTemperatureData.py > tempdataN.txt (N in this case is 1,2,3,etc...)

line_number = 0
longitude = [42.1015, 22.9068, 51.5074]  # each one of these relates to a continent
# North America, South America, etc...
latitude = [72.5898, 43.1729, 0.1278]  # each one of these relates to a continent
# North America, South America, etc...
continent = ['North America', 'South America', 'Europe']
randoms = [101, 101, 101]  # These are the sizes of the temperature readings for the years (2016, 2015, 2014)

for i in range(1, randoms[0] + 1, 1):
    if i <= 31:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'Jan', ',', i, ',', '2016', ',', random.randint(-10, 30)
    elif i > 31 and i <= 69:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'Feb', ',', (i - 31), ',', '2016', ',', random.randint(0, 50)
    elif i > 69 and i <= 100:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'Mar', ',', (i - 69), ',', '2016', ',', random.randint(10, 50)
    elif i > 100 and i <= 130:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'Apr', ',', (i - 100), ',', '2016', ',', random.randint(30, 50)
    elif i > 130 and i <= 161:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'May', ',', (
        i - 130), ',', '2016', ',', random.randint(50, 60)
    elif i > 161 and i <= 191:
        print line_number, ',', longitude[0], ',', latitude[0], ',', continent[0], ',', 'Jun', ',', (
        i - 161), ',', '2016', ',', random.randint(30, 50)
    line_number += 1

for i in range(1, randoms[1] + 1, 1):
    if i <= 31:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'Jan', ',', i, ',', '2015', ',', random.randint(70, 100)
    elif i > 31 and i <= 69:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'Feb', ',', (i - 31), ',', '2015', ',', random.randint(70, 100)
    elif i > 69 and i <= 100:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'Mar', ',', (i - 69), ',', '2015', ',', random.randint(70, 100)
    elif i > 100 and i <= 130:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'Apr', ',', (i - 100), ',', '2015', ',', random.randint(70, 100)
    elif i > 130 and i <= 161:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'May', ',', (
            i - 130), ',', '2015', ',', random.randint(50, 60)
    elif i > 161 and i <= 191:
        print line_number, ',', longitude[1], ',', latitude[1], ',', continent[1], ',', 'Jun', ',', (
            i - 161), ',', '2015', ',', random.randint(30, 50)
    line_number += 1

for i in range(1, randoms[2] + 1, 1):
    if i <= 31:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'Jan', ',', i, ',', '2014', ',', random.randint(70, 100)
    elif i > 31 and i <= 69:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'Feb', ',', (i - 31), ',', '2014', ',', random.randint(70, 100)
    elif i > 69 and i <= 100:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'Mar', ',', (i - 69), ',', '2014', ',', random.randint(70, 100)
    elif i > 100 and i <= 130:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'Apr', ',', (i - 100), ',', '2014', ',', random.randint(70, 100)
    elif i > 130 and i <= 161:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'May', ',', (
            i - 130), ',', '2014', ',', random.randint(50, 60)
    elif i > 161 and i <= 191:
        print line_number, ',', longitude[2], ',', latitude[2], ',', continent[2], ',', 'Jun', ',', (
            i - 161), ',', '2014', ',', random.randint(30, 50)
    line_number += 1
