'''
_____________________________________________________________________________________________
All my python useful functions/classes are here. 

https://pandas.pydata.org
https://pypi.org/project/ebookmeta/
https://pypi.org/project/music-tag/
https://openpyxl.readthedocs.io/en/stable/

pip install music_tag
pip install ebookmeta
pip install pandas
pip install openpyxl
pip install pillow


from brlib.fileutilbr import *


2023 Daniel Gomes
Use with care ;-)

_____________________________________________________________________________________________

'''
import sys
import os
import pathlib
from pathlib import Path
import shutil
import subprocess
import socket
import sys, os
import pprint
import binascii
import traceback
from datetime import datetime
import music_tag
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import FLAC
import ebookmeta
import pandas as pd
from PIL import Image

#extensions for files-----------------------------------------------------------

ZIPEXT = "zip"
CBZEXT = "cbz"
CBREXT = "cbr"
AZWEXT = "azw"
AZWEXT3 = "azw3"
EPUBEXT = "epub"
PDFEXT = "pdf"
DOCEXT = "doc"
RTFEXT = "rtf"

#masks for multiple file processing---------------------------------------------

DOCUMENT_MASK = [EPUBEXT,CBZEXT,PDFEXT,DOCEXT,RTFEXT]
IMAGES_MASK   = ["gif","jpg", "bmp", "tiff", "png"]
MUSIC_MASK   = ["mp3","flac", "ogg", "MP3","FLAC","OGG"]
EBOOKS_MASK = [EPUBEXT,CBZEXT,PDFEXT,AZWEXT3]
COMICS_MASK = [CBZEXT,CBREXT]


################################## HANDLE FILES ############################################

'''
Creates a csv file that can be used by Machine learning algorithms
'''
class mycsvfile:
    file = None
    
    def __init__(self,name):
         
        if self.file == None:
            self.file = open( name, 'wt')
            
    def getname():
        print(self.myfilename)
        
    def writefield(self,field,endline):
        if endline == False:
            self.file.write("{},".format(field))
        else:
            self.file.write(field)
    
    def closethis(self):
         if self.file != None:
            self.file.close()       
        
        
'''
Application error log
'''
class errorlog:
    
    filename = ""
    myerrorfile = None
    def __init__( self ):
        now = datetime.now() # current date and time
        date_time = now.strftime("%m_%d_%Y_%H_%M_%S.log")
        self.filename = "../log/errlog." + date_time
        
    def getname( self ):
        return self.filename
    
    def getstamp( self ):
        now = datetime.now() # current date and time
        return  now.strftime("%m/%d/%Y %H:%M:%S - ")       
        
    def writeto( self, msg ):      
        if self.myerrorfile == None:
            self.myerrorfile = open( self.filename, 'wt')
        outmsg = msg + "\n"
        self.myerrorfile.write( outmsg  )

    def writestuff( self, stuff ):      
        if self.myerrorfile == None:
            self.myerrorfile = open( self.filename, 'wt')
        self.myerrorfile.write( stuff  )
        
    def writetorow( self, row ):      
        #self.myerrorfile.write( self.getStamp() ) 
        for field in row:
            tobewriten = " {} ".format( field )
            self.myerrorfile.write( tobewriten )
        self.myerrorfile.write("\n")
        
    def writetofull( self, stuff ):      
        self.myerrorfile.write( self.getStamp() ) 
        self.myerrorfile.write( stuff )
          
    def endLog( self ):
        if self.myerrorfile != None:
            self.myerrorfile.close()
        
'''
Split file into smaller chuncks
'''
class filespliter:
    f = None
    filename = None
    maxfiles = 0
    listofiles = []
    
    #constructor
    def __init__( self, filename ):
        self.filename = filename   
        
    def getsize(self):
        st = os.stat(self.filename)
        return (st.st_size)

    def getfilelists( self ):
        return self.listofiles

    def deletealltmpfiles( self ):
        for file in self.listofiles:
            #print( "Removing {}".format( file ))
            os.remove( file)

    def createfile( self, chunk, n ):
        nameof = "split_" + str(n ) + "_" + self.filename
        tmpfile = open( nameof, 'wb')
        print( "Creating {}".format( nameof ) )
        self.listofiles.append(nameof)
        tmpfile.write( chunk )
        tmpfile.close()

    def splitfile( self, maxcrit ):
        filescnt = 0
        
        if os.path.exists(self.filename):
            self.f = open(self.filename, 'rb')
            self.maxfiles = self.getSize()/maxcrit
            print(self.maxfiles)
            while ( filescnt <= self.maxfiles ):
                chunk = self.f.read(maxcrit)
                self.createfile( chunk, filescnt  )   
                filescnt = filescnt + 1
            self.f.close()
        else:
            return None     
 
'''
This class is used to open a file, read its lines and return
a list with all the lines
'''
class FileOpener:

    f = None
    filename = None
    allow = False
    
    #constructor
    def __init__( self, filename ):
        self.filename = filename
    
    def close( self ):
        self.f.close()
        
    def openfile(self):       
        if os.path.exists(self.filename):
            self.f = open(self.filename, 'rt', errors='ignore')
            self.allow = True
            return self.f
        else:
            return None   
    
    def readallfile( self ):
        if self.allow == True:
            data = self.f.read()
            return data

'''
copy  all files under the directory dir ( including subfolders ) who extension is ext
O(n^2) be carefull
''' 
def copyfiles(dir,ext,dir_dest):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            full = "{}\{}".format(root,name)
            if ( fext == ext):
                print("copying {}".format(full))
                copy( full,dir_dest)
 
'''
Removes all files under the directory dir ( including subfolders ) who extension is not ext
O(n^2) be carefull
''' 
def remove_files(dir,ext):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            full = "{}\{}".format(root,name)
            if ( fext == ext):                
                if os.path.isfile(full):
                    print("removing {}".format(full))
                    os.remove(full)

'''
copy a file src to dst
dst can be a new file name or a directory
O(n^2) be carefull
'''
def copy(src,dst):

    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copyfile(src, dst)
    
def move(src,dst):

    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.move(src, dst)   

def create_folder( dir_root, name ):
    
    full_path = dir_root + "\\" + name
    if os.path.exists(full_path) == False:
        os.mkdir(full_path)
    else:
        return ""
    return full_path

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
    
'''
List files with extensions ext under folder
'''    
def listmyfiles(folder,ext):
    for file in file_ext_iterator(folder,ext):
        print(file)
        
def get_image_info( file ):
    im = Image.open(file)
    return im.format, im.size, im.mode
    
'''
List files with extensions ext under folder
'''    
def listmyfilesfull(folder,ext,path, isimage= True):
    full_path = path + "\\tmp.txt"
    with open(full_path, 'w', encoding='utf-16') as fl: 
        for file in file_ext_iterator(folder,ext,True):            
            if file != "":
                if isimage == False:
                    print(file)  
                    fl.write(file)
                    fl.write("\n")
                else:
                    try:
                        format, size, mode = get_image_info(file)
                        print(file)  
                        fl.write("{} {} {} {}".format(file , format, size, mode))
                        fl.write("\n")   
                    except:
                        pass
    


'''
changes the extension all files under the directory dir ( including subfolders ) 
from ext to myextfinal
O(n^2) be carefull
'''
def change_extension(dir,ext,myextfinal):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            if ( fext == ext):
                print("Changing {}/{}".format(root,name))
                changeExt(root + "/" + name,myextfinal) 
                

'''
gets all extensions of files in a directory
'''
def getallextensions(dir):
    extentions = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            if fext not in extentions:
                extentions.append(fext)
                yield fext

'''
Prints all extensions
'''
def printextensions(dir):
    for ext in getallextensions(dir):
        print("extension: {}".format(ext))
    
################################## HANDLE NETWORKING ############################################

'''
 Just check if ports are open or closed in the range
'''
def monitorPorts( ipaddress, port_init, port_end  ):

    portInfo = {}
    for port in range(int(port_init), int(port_end)+1):
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ipaddress,port))
        if result == 0:
            portInfo[ port ] = "Open"
        else:
            portInfo[ port ] = "Closed"
        sock.close()
     
    return portInfo
    
'''
 Sends a message using a socket
'''
def sendMessage( host, port, BUFFER_SIZE , msg ):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.connect((host, port))
        # We convert str to bytes
        socket_tcp.send( msg.encode('utf-8') )
        data = socket_tcp.recv(BUFFER_SIZE)

'''
Help function for monitorPorts
'''
def monitorPortsInterface(): 
    ipaddress =input("Enter ip address or domain for port scanning:")
    port_init= input("Enter first port: ")
    port_end = input("Enter last port: ")
    monitorPorts( ipaddress, port_init, port_end)
    

################################## HANDLE APPs CONSOLE############################################  

'''
Handles the default error for a menu
'''
def DoDefaultError(errmsg="Invalid entry"):
    
    os.system("cls")
    print(errmsg) 

'''
Creates a menu using a dictionary 
if submenu is True, it will create a submenu, eg,
it will leave the submenu and go back to the main menu    
'''
def runmenu(menuoptions,header_str="Options:",submenu=False):
    
    while True:
        os.system("cls")# Linux/unix use "clear"

        print("-------------------------------------------")
        print(header_str)
        print("-------------------------------------------")
        for key,actions in menuoptions.items():
            print("({})      {}".format(key,actions[0]))           
        print("-------------------------------------------")       
        
        ch = -1
        try:
            ch=int(input("Enter your choice: "))
        except:
            ch = -1
        
        if ch in menuoptions:
            function_from_menu = menuoptions[ch][1]
            if submenu == False:                
                function_from_menu()                
            else:
                ret = function_from_menu()
                if ret == True:
                    return
        else:
            DoDefaultError()
  
        input("Press enter to continue.")
        
################################## HANDLE THREADS/PROCESS/OS ############################################  

'''
executes a commmand line cmd 
'''
def run_win_cmd(cmd, tokenize=False):
    
    result = ""
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, encoding='UTF-8')
    except:
        return None
    
    if len(result.stderr) > 0:   
        print(result.stderr)
    else:
        if tokenize == False:
            print(result.stdout) 
            return None
        else:
            if result.stdout == None:
                return None
            return result.stdout.split("\n")



################################## HANDLE FILE ITERATORS ############################################

'''
looks for a file within a dir 
'''
def find_file( dir, filename ):
    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            file_name, t = os.path.splitext(name)
            if filename == file_name + t:
                print(root + "\\" + file_name + t)
                return
    
    print( filename + " not found" )
                
            
'''
Iterates over directory dir and lists all files with extension ext , by default
the fullpath is not returned
Ex:
    for pdf in file_ext_iterator("D:\\Documentos\\Technical\\Physics","pdf"):
        print(pdf)
O(n^2) be carefull
'''
def file_ext_iterator( dir, ext, full_path = False ):
    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            file_name, t= os.path.splitext(name)
            
            if fext in ext:
                if full_path:
                    yield root + "\\" + file_name + t
                else:
                    yield file_name
            else:
                yield ""
 
'''
Iterates over directory dir and lists the first mp3 or media file contained in the mask
ext
O(n^2) be carefull
''' 
def file_ext_iterator2( dir, ext, full_path = False ):
    for root, dirs, files in os.walk(dir):
        i = 0
        for name in files:
               
            fext = getextension(name)
            file_name, t= os.path.splitext(name)
            
            if fext in ext:
                #Only need the first file to get meta info
                #works for audio files and epub
                if full_path:
                    if i > 0:
                        i = 0;
                        break;
                    i = i + 1                
                    yield root + "\\" + file_name + t,fext
                else:
                    yield file_name,fext
 
################################## HANDLE EBOOKS,DOCUMENTS AND COMICS ############################################ 

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
Using calibre executable to convert all files that match the original ext ext_orig 
to ext_final

O(n^2) be carefull
'''        
def convert_batch( dir, ext_orig, ext_final,outdir):

    for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            file_name, t= os.path.splitext(name)
            if ( fext == ext_orig):
                final = "{}.{}".format(file_name, ext_final)
                convert_files(root+"\\"+name,outdir+"\\"+final)
                
'''
obtains ebook medata data
'''
def getebookmetadata(file):
    
    meta = ebookmeta.get_metadata(file)     
    return meta.author_list[0],meta.title
 

def do_all_comics( dir,outdir ):
    
    convert_batch(dir,AZWEXT,EPUBEXT,outdir)
    list_book_data_and_rename( outdir, EPUBEXT )
    convert_batch(outdir,EPUBEXT,ZIPEXT,outdir)
    change_extension(outdir,ZIPEXT,CBZEXT)
    
def list_book_data_and_rename(dir,ext):

     for root, dirs, files in os.walk(dir):
        for name in files:
            fext = getextension(name)
            file_name, t= os.path.splitext(name)
            if fext in ext:
                autor, title = getebookmetadata(root+"\\"+name)   
                print("autor {} titulo '{}'".format(autor,title))
                title_final_tmp = autor+"_"+title+"."+fext
                title_final = title_final_tmp.replace(" ","_")
                title_final = title_final.replace(":","")
                os.rename(root+"\\"+name, root+"\\"+title_final)
    
'''
converts a csv file to xlsx
'''    
def convert_csv_excel(excel_filename_csv):
    
    file_name, t = os.path.splitext(excel_filename_csv)
    read_file_product = pd.read_csv(excel_filename_csv)
    read_file_product.to_excel (file_name + ".xlsx", index = None, header=True)    

 
################################## HANDLE DIGITAL MEDIA ############################################ 



def get_file_info( musicfile, ext ):
    
        f = None
        if ext == "mp3":
            f = MP3(musicfile)
        elif ext == "ogg":
            f = OggVorbis(musicfile)
        elif ext == "flac":
            f = FLAC(musicfile)
            
        info = "bit rate[{}]".format( (f.info.bitrate/1000))
        
        return info
    
'''
List albums and artists from your cd collection at the path folder
extension mask ext and saves the outputfile to out_dir
'''    
def get_media(folder,ext,out_dir,type = 0):
    
    prev_t = ""
    prev_a = ""
    cnt = 1
    
    path = 0
    if type == 0:
        path = out_dir+"\\music_list.txt"
    else:
        path = out_dir+"\\ebooks.txt"
    
    with open(path, 'w', encoding='utf-16') as fl:   
        
        for file,ext in file_ext_iterator2(folder,ext,True):
            
            print("processing {} ...".format(file))
            
            info = ""
                        
            if type == 0:
                try:
                    f = music_tag.load_file(file)                
                except:   
                    print("Error reading {}".format(file))
                    continue
                
                try:
                    info = str(get_file_info(file,ext))
                except:
                    info = "N/A"
                    
                artist = str(f['artist'])
                album = str(f['album'])
                
                if len(artist) == 0:
                    continue    
                                    
                if prev_t== album:
                    cnt = cnt + 1
                else:
                    cnt = 1
                 
                if prev_a != artist:
                    fl.write("__________________________________________________________________________________")
                    fl.write('\n\n') 
                    fl.write("[ {} ]".format(artist))
                    fl.write('\n') 
                    fl.write("__________________________________________________________________________________")
                    fl.write('\n\n') 
                            
                prev_t = album
                prev_a = artist
                    
                line = "'{}' disc#{} filetype[{} - {}]".format(album,cnt,ext,info)               
                fl.write(line)
                fl.write('\n')
                
            elif type == 1:
                                        
                try:                  
                    author, title = getebookmetadata(file) 
                except:
                    print("Error reading: {}".format(file))
                    continue
                    
                if len(author) == 0:
                    continue                        
                
                if prev_t == title:
                    cnt = cnt + 1
                else:
                    cnt = 1
                 
                if prev_a != author:
                    fl.write("__________________________________________________________________________________")
                    fl.write('\n\n') 
                    fl.write("[ {} ]".format(author))
                    fl.write('\n') 
                    fl.write("__________________________________________________________________________________")
                    fl.write('\n\n') 
                            
                prev_t = title
                prev_a = author
                    
                line = "'{}'".format(title)               
                fl.write(line)
                fl.write('\n')               
            else:
                print("Error")
        
 

################################## END OF FILE ############################################          
                

            
             