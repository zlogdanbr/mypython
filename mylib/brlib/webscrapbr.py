import sys, os, requests
import bs4
import lxml
from pathlib import Path


def getHtmlPage( url ):

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml' )
    return soup
    
def getAllImages( soup ):

    pElems = soup.select('img')
    for myimgtag in pElems:
        yield myimgtag.get('src')
                
def downloadfile( url, file_name ):
    
    res = requests.get(url)
    print("Downloading {} from {} ".format(file_name,url))
    if res.status_code == requests.codes.ok:
        thefile = open( file_name , 'wb')
        for chunk in res.iter_content(100000):
            thefile.write(chunk)
        thefile.close()
    else:
        print( "Error {} while downloading {} ".format( res.status_code , url ))        
 
def getAllImagesFromSite( url ): 

    soup = getHtmlPage(url)
 
    for images in getAllImages( soup ):
        print(images)



