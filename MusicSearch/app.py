import timeit
from bintreeFile import Bintree

class Song():

    def __init__(self, trackid, songid, artist, songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.songtitle = songtitle

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        else:
            return False

    def __str__(self):
        return self.trackid + "\n" + self.songid + "\n" + self.artist + "\n" + self.songtitle


def readfile(filename):
    songlist = []
    songdict = {}

    f = open(filename, "r")
    for line in f:
        data = line.strip().split('<SEP>')
        newsong = Song(data[0],data[1],data[2],data[3])
        songlist.append(newsong)
        songdict[str(data[2])] = Song(data[0],data[1],data[2],data[3])
    return songlist, songdict


def linsok(songlist, artist):
    artistExist = False
    for row in songlist:
        if row.artist == artist:
            artistExist = True
    return artistExist

def binbygg(songlist):
    bintree = Bintree()
    for row in songlist:
        artist = row.artist
        bintree.put(str(artist))
    return bintree


def binsok(artist, bintree):
    artistExist = False
    if str(artist) in bintree:
        artistExist = True

def dictsok(artist, dict):
    artistExist = False
    if str(artist) in dict:
        artistExist = True





def main():
    filename = 'unique_tracks.txt'

    print("-" * 50)
    print("Initialiserar...")
    lista, dictionary = readfile(filename)
    tree = binbygg(lista)


    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    print("-" * 50)
    print("Gör linjärsökning...")
    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 1)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    print("-" * 50)
    print("Sorterar lista till binärt sökträd...")
    linjtid = timeit.timeit(stmt = lambda: binbygg(lista), number = 1)
    print("Sortering i binärt sökträd tog", round(linjtid, 4) , "sekunder")

    print("-" * 50)
    print("Gör sökning i binärt sökträd...")
    linjtid = timeit.timeit(stmt = lambda: binsok(testartist, tree), number = 1000)
    print("Binärsökningen tog", round(linjtid, 4) , "sekunder")

    print("-" * 50)
    print("Gör sökning i osorterad dictionary...")
    linjtid = timeit.timeit(stmt = lambda: dictsok(testartist, dictionary), number = 10000)
    print("Dictionary sökningen tog", round(linjtid, 4) , "sekunder")



    # VID 10 KÖRNINGAR:
    # Linjärsökning: 3.4563 sekunder
    # Binärträd sortering: 112.9745 sekunder
    # Sökning i binärt sökträd: 0.0001 sekunder
    # Sökning i dictionart: <0.0001 sekunder


if __name__ == '__main__':
    main()
