from mrjob.job import MRJob
import sys


class MRInvertedIndex(MRJob):

    def mapper(self, key, line):
        # sys.stderr.write("MAPPER INPUT: ({0},{1})\n".format(key, line))  # displays intermediate values of mapper
        # with map reduce so I hope this will suffice
        lists = line.split(',')  # split the line according to comma delimiting
        url = lists[0]  # grab the url
        words = lists[1]  # grab the words
        # print 'This is the URL -> ', url
        # print 'This is the list of words -> ', words
        for word in words.split():  # iterate through the words delimiting by ' '
            yield word, url  # emit the intermediate values

    def reducer(self, word, url):
        urllist = list(set(url))  # make the url list into a set to avoid repeats
        # sys.stderr.write("REDUCER INPUT: ({0},{1})\n".format(word, urllist))  # displays reducer values
        yield word, urllist

if __name__ == '__main__':
    MRInvertedIndex.run()
