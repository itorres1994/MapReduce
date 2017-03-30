from mrjob.job import MRJob
import sys


class MRTemperatureObservations(MRJob):

    def mapper(self, key, line):
        # sys.stderr.write("MAPPER INPUT: ({0},{1})\n".format(key, line))  # displays intermediate values of mapper
        data = line.split(',')  # take the input from the text file and parse it with respect to (',')
        yield data[6], data[7]  # data[6]: year, data[7]: temperature

    def reducer(self, year, data):
        # sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(year, data))  # displays reducer values
        temps = list(data)  # data: generating function -> make it into a list of temperatures
        if len(temps) > 100:  # is the number of temperature readings in a distinct year greater than 100
            yield year, len(temps)  # print to console the distinct year and number of temperature readings

if __name__ == '__main__':
    MRTemperatureObservations.run()
