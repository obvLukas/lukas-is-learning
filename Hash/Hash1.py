# -*- coding: utf-8 -*-

import timeit



class DictHash():

    def __init__(self):
        self.dict = {}

    def store(self, nyckel, data):
        self.nyckel = nyckel
        self.data = data
        self.dict[self.nyckel] = self.data

    def search(self, key):
        if key in self.dict:
            return self.dict[key]

    def __str__(self):
        return str(self.dict)

#table = DictHash()
#table.store('Test', 75)
#print(table.search('Test'))

def readfile(filename):
    artistDict = DictHash()
    f = open(filename, "r")
    for line in f:
        data = line.strip().split('<SEP>')
        artistDict.store(data[0], data[2])
    return artistDict


def main():

    artistDict = readfile('unique_tracks.txt')
    x = artistDict.search('TRYYKJQ128F92F0F74')
    print(x)

    tid = timeit.timeit(stmt = lambda: artistDict.search('TRYYYVU12903CD01E3'), number = 10000)
    print("Dictionary sökningen tog", round(tid, 4) , "sekunder")









if __name__ == '__main__':
    main()
