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
    return songlist


def main():
    filename = 'unique_tracks.txt'
    songlist = readfile(filename)




if __name__ == '__main__':
    main()
