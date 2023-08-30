import sys
import os
import pathlib
from pathlib import Path
import shutil
import subprocess


CALIBRE_FOLDER = "C:\\Users\\Administrador\\Biblioteca do calibre"
KINDLE_FOLDER = "C:\\Users\\Administrador\\Documents\\My Kindle Content"
OUT_DIR = "C:\\Users\Administrador\\Documents\\tmp"

ZIPEXT = "zip"
CBZEXT = ".cbz"
AZWEXT = "azw"

'''
executes a commmand line cmd 
'''
def run_win_cmd(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, encoding='UTF-8')
    
    if len(result.stderr) > 0:   
        print(result.stderr)
    else:
        print(result.stdout)

'''
rename all files under the directory dir ( including subfolders ) and changes the extensions
from ext to myextfinal
'''
def renamefiles(dir,ext,myextfinal):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            if ( fext == ext):
                print("Changing {}/{}".format(root,name))
                changeExt(root + "/" + name,myextfinal) 
 
'''
copy  all files under the directory dir ( including subfolders ) who extension is ext
''' 
def copyfiles(dir,ext):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            full = "{}\{}".format(root,name)
            if ( fext == ext):
                print("copying {}".format(full))
                copy( full,outdir)
 
'''
Removes all files under the directory dir ( including subfolders ) who extension is not ext
''' 
def remove_files(dir, ext):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            full = "{}\{}".format(root,name)
            if ( fext != ext):                
                if os.path.isfile(full):
                    os.remove(full)

'''
copy a file src to dst
dst can be a new file name or a directory
'''
def copy(src, dst):

    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copyfile(src, dst)

'''
Gets the extension of a file
'''
def getextension(file):

    return pathlib.Path(file).suffix[1:]

'''
Changes the extension of a file to ext
'''
def changeExt( file, ext ):

    pre, fext = os.path.splitext(file)
    os.rename( file, pre + ext )

def main(argv):

    renamefiles(CALIBRE_FOLDER,ZIPEXT,CBZEXT)


if __name__ == '__main__':

    main(sys.argv)
