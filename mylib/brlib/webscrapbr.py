import sys, os, requests
import bs4
import lxml
from pathlib import Path
import ntpath

def getInput(argv):

    if len(argv) > 1:
        # Get address from command line.
        address = argv[1]
        address2 = argv[2]
    return address,address2

def getHtmlPage( url ):

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml' )
    return soup
    
def getAllImages( soup ):
    cnt = 0
    pElems = soup.select('img')
    for myimgtag in pElems:
        cnt = cnt + 1
        yield myimgtag.get('src')
        
        
def getFolderFromRelpath( pathsstring ):
    return Path(pathsstring).parent
    
def getNameofFile( wholepath ):
    return ntpath.basename(wholepath)
        
def downloadfile( url, name ):
    res = requests.get(url)
    print("Downloading {} from {} ".format(name,url))
    if res.status_code == requests.codes.ok:
        thefile = open( name , 'wb')
        for chunk in res.iter_content(100000):
            thefile.write(chunk)
        thefile.close()
    else:
        print( "Error {} while downloading {} ".format( res.status_code , url ))
        
def createImageFolder( imgfldr ):
    mypath = os.getcwd()
    folder =  getFolderFromRelpath( imgfldr )
    ftocreate = "{}{}".format(mypath,folder)
    return ftocreate
 
def getAllImagesFromSite( url, urlimages ): 

    soup = getHtmlPage( url)
    cnt = 0
 
    for images in getAllImages( soup ):
        nodostuff = images[0:4]
        ftocreate = ""
        if nodostuff != "http":
            ftocreate  = createImageFolder( images )
            if cnt == 0:               
                if not os.path.exists(ftocreate):
                    os.makedirs(ftocreate)
                cnt = 300
            fn = getNameofFile( "{}{}".format(urlimages,images[1:]))
            #print( "{}/{}".format(urlimages, fn ))
            downloadfile( "{}/{}".format(urlimages, fn ), "{}/{}".format(ftocreate, fn))

def getFullPage( url, name  ):
    downloadfile( url, name )
 
# python getstuff.py https://automatetheboringstuff.com/chapter2/ https://automatetheboringstuff.com/images
def main(argv):
    os.system('clear')
    url,urlimage = getInput(argv)
    getAllImagesFromSite(url,urlimage)
    getFullPage( url, "chapter2.html" )
    
if __name__ == '__main__':
    main(sys.argv)

