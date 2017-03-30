from mrjob.job import MRJob
import sys


class MRTemperatureObservations2(MRJob):

    def mapper(self, key, line):
        # sys.stderr.write("MAPPER INPUT: ({0},{1})\n".format(key, line))  # displays intermediate values of mapper
        data = line.split(',')  # take the input from the text file and parse it with respect to (',')
        # print 'This is data[7] -> ', data[7]
        yield (data[3], data[6]), data[7]  # (data[3]: continent, data[6]: year), data[7]: temperature

    def reducer(self, continent_year, data):
        # sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(continent_year, data))  # displays reducer values
        temps = list(data)  # data: generating function -> make it into a list of temperatures
        data_list = list(continent_year)
        continent = data_list[0]
        year = data_list[1]
        total = 0
        # print 'continent -> ', continent
        # print 'year -> ', year
        for d in range(len(temps)):
            total += float(temps[d])
        if len(temps) > 50:  # is the number of temperature readings in a distinct year greater than 100
            yield (continent, year), round((total/len(temps)), 2)  # print to console the distinct continent and
            #  year coupled with the average temperature readings

if __name__ == '__main__':
    MRTemperatureObservations2.run()
