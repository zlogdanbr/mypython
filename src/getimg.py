import requests
import os
import sys
import bs4
from wpega import DownloadfileFromWeb

def getAllImagesLinks( theURL ):
    res = requests.get( theURL )
    res.raise_for_status()
    myhtmlsoup = bs4.BeautifulSoup(res.text,'lxml') 
    myimglinks = myhtmlsoup.select('img')
    
    for im in myimglinks:
        yield im.get( 'src' )


def main(argv):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    

    URL = argv[1]
    URLImg = argv[2]   

    for imlinks in getAllImagesLinks( URL ):
        actualURL = "{}{} ".format( URLImg, imlinks[1:] )
        print( actualURL )
        print( URLImg )
        print( imlinks)
        #DownloadfileFromWeb( actualURL, imlinks, 100000 )

if __name__ == '__main__':
    main(sys.argv)