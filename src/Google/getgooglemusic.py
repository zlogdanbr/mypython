from gmusicapi import Musicmanager


class MyCdList:

    mm = None
    library = None

    def authenticatewithgoogle(self,option):

        self.mm = Musicmanager()
        self.mm.login()  # currently named oauth_login for the Mobileclient

        if option == 0:
            self.library = self.mm.get_purchased_songs()
        elif option == 1:
            self.library = self.mm.get_uploaded_songs()

    def getallartist(self):
        donotaddthis = "The 100 Most Essential Pieces of Classical Music"
        artists = []
        artistsset = set()
        [artistsset.add(track['artist']) for track in self.library if track['album'] != donotaddthis ]
        artists = list(artistsset)
        artists.sort()
        return artists

    def getalbumsforartist( self, artist):

        albums = []
        albumsset = set()
        [ albumsset.add(track['album']) for track in self.library if track['artist'] == artist ]
        albums = list(albumsset )
        albums.sort()
        return albums


def bought():
    cdlist = MyCdList()
    cdlist.authenticatewithgoogle(0)
    artists = cdlist.getallartist()
    cnt = 0
    with open('mp3bought.txt', 'wt', encoding='utf-8') as f:

        for a in artists:
            print("Getting albums of {}...".format(a))
            albums = cdlist.getalbumsforartist(a)
            f.write("Artist: {} \n".format(a))
            for alb in albums:
                f.write("\t {} \n".format( alb))
                cnt = cnt + 1
        f.write("Total Number of albums {}\n".format(cnt))


def all():
    cdlist = MyCdList()
    cdlist.authenticatewithgoogle(1)
    artists = None
    artists = cdlist.getallartist()
    cnt = 0

    with open('mp3all.txt', 'wt', encoding='utf-8') as f:

        for a in artists:
            print("Getting albums of {}...".format(a))
            albums = cdlist.getalbumsforartist(a)
            f.write("Artist: {} \n".format(a))
            for alb in albums:
                f.write("\t {} \n".format(alb))
                cnt = cnt + 1
        f.write("Total Number of albums {}\n".format(cnt))


def main():
    all()


if __name__ == "__main__":
    main()






