import requests
import os
import sys
import bs4


def DownloadfileFromWeb( URL, nameofile , CHUNCK_SZE ):
    print("Downloading file please wait...")
    res = requests.get(URL)
    
    if res.status_code == requests.codes.ok:
        res.raise_for_status()
        thefile = open(nameofile, 'wb')
        for chunk in res.iter_content(CHUNCK_SZE):
            thefile.write(chunk)
        thefile.close()
        return 0
    else:
        return 1
        
def main(argv):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Default parameters not allowed
    if len(argv) <= 2 :
        print("Error. Too few parameters.")
        return      

    URL = argv[1]              
    nameofile = argv[2] 
    CHUNCK_SZE = int(argv[3]) 
    
    try:
        if DownloadfileFromWeb(URL, nameofile, CHUNCK_SZE ) == 0:
            print("File {} downloaded correctly".format(nameofile))
        else:
            print(" URL {} does not exist or is not active".format(URL))
    except:
        print("Error while downloading...")
    
#python wpega.py https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf  a-whirlwind-tour-of-python.pdf 100000
if __name__ == '__main__':
    main(sys.argv)