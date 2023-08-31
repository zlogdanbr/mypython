'''
Removing DRM

Step 1 Download calibre         https://calibre-ebook.com
Step 2 Install DRM plugins      https://www.epubor.com/calibre-drm-removal-plugins.html
Step 3 Set the paths below
CALIBRE_FOLDER = "C:\\Users\\Administrador\\Biblioteca do calibre"
KINDLE_FOLDER = "C:\\Users\\Administrador\\Documents\\My Kindle Content"
OUT_DIR = "C:\\Users\Administrador\\Documents\\tmp"
Step 4 Add the desired action to main
    4.1 copyfiles(CALIBRE_FOLDER,AZWEXT)
    4.2 convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT)
    4.3 change_extension(OUT_DIR,ZIPEXT,CBZEXT)
    4.4 remove_files(OUT_DIR,EPUBEXT)
    
For comics:    
I usually copy  copyfiles(KINDLE_FOLDER,AZWEXT)  
Then I manually add them to calibre ( drag and drop )

Calibre will create a decent folder structure at  CALIBRE_FOLDER
I call convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT) and all zip files will be placed at
OUT_DIR


Then change_extension(OUT_DIR,ZIPEXT,CBZEXT) will simply rename the zip files to cbz
allowing any reader to open 
'''

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
CBZEXT = "cbz"
AZWEXT = "azw"
AZWEXT3 = "azw3"
EPUBEXT = "epub"

'''
calls ebook-convert.exe to convert myfile.input_format to myfile.output_format
'''
def convert_files( orig, dest ):

    print("Running ebook-convert for "+orig+" "+dest)
    cmd = []
    cmd.append("ebook-convert")
    cmd.append(orig)
    cmd.append(dest)
    run_win_cmd(cmd)

'''
executes a commmand line cmd 
'''
def run_win_cmd(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, encoding='UTF-8')
    
    if len(result.stderr) > 0:   
        print(result.stderr)
    else:
        print(result.stdout)
        
def convert_batch( dir, ext_orig, ext_final):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            file_name, t= os.path.splitext(name)
            if ( fext == ext_orig):
                final = "{}.{}".format(file_name, ext_final)
                convert_files(root+"\\"+name,OUT_DIR+"\\"+final)

'''
changes the extension all files under the directory dir ( including subfolders ) 
from ext to myextfinal
'''
def change_extension(dir,ext,myextfinal):

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
                copy( full,OUT_DIR)
 
'''
Removes all files under the directory dir ( including subfolders ) who extension is not ext
''' 
def remove_files(dir,ext):

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
def copy(src,dst):

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
    os.rename( file, pre + "." + ext )

def main(argv):
    #copyfiles(CALIBRE_FOLDER,AZWEXT)
    #convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT)
    #change_extension(OUT_DIR,ZIPEXT,CBZEXT)
    #remove_files(OUT_DIR,EPUBEXT)
    pass

if __name__ == '__main__':

    main(sys.argv)
