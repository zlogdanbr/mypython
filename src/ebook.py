import sys
import os
import pathlib
from pathlib import Path

mydir = "C:\\Users\\Administrador\\Biblioteca do calibre"
myext = "zip"
myextfinal = ".cbz"

def list_files(dir):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            if ( fext[1:] == myext):
                print("Changing {}/{}".format(root,name))
                changeExt(root + "/" + name,myextfinal) 
                

def getextension(file):

    return pathlib.Path(file).suffix

def changeExt( file, ext2 ):

    pre, ext = os.path.splitext(file)
    os.rename( file, pre + ext2 )

def main(argv):

    list_files(mydir)
      

if __name__ == '__main__':
    main(sys.argv)