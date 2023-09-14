'''
_____________________________________________________________________________________________
All my python useful functions/classes are here. 


https://pypi.org/project/beautifulsoup4/
pip install bs4

from brlib.webscrapbr import *

2023 Daniel Gomes
Use with care ;-)
_____________________________________________________________________________________________

'''

import sys, os, requests
import bs4
import lxml
from pathlib import Path


'''
Obtains the text of a remote HTML page refered by URL
'''
def getHtmlPage( url ):

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml' )
    return soup
 
'''
Obtains the URIs for all images from a soup object
''' 
def getAllImages( soup ):

    pElems = soup.select('img')
    for myimgtag in pElems:
        yield myimgtag.get('src')
 
'''
Download a file from the URL and renames it to file_name
'''  
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
 
'''
Downloads all images from their especific URIs
TODO: finish this function
'''
def getAllImagesFromSite( url ): 

    soup = getHtmlPage(url)
 
    for images in getAllImages( soup ):
        print(images)

################################## END OF FILE ############################################  

