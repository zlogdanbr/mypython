'''
_____________________________________________________________________________________________
All my python useful functions/classes are here. 
I only use this for hobby purposes.
I am a c++ programmer by profession but python is my favorite language.

- HANDLE FILES
- HANDLE NETWORKING
- HANDLE THREADS/PROCESS/OS
- HANDLE FILE ITERATORS
- HANDLE EBOOKS AND COMICS
- HANDLE DIGITAL MEDIA 

Required libs:

pip install music_tag

All you have to do is to include the file fileutilbr.py
or 
from fileutilbr import *


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
        
    def getName( self ):
        return self.filename
    
    def getStamp( self ):
        now = datetime.now() # current date and time
        return  now.strftime("%m/%d/%Y %H:%M:%S - ")       
        
    def writeTo( self, msg ):      
        if self.myerrorfile == None:
            self.myerrorfile = open( self.filename, 'wt')
        outmsg = msg + "\n"
        self.myerrorfile.write( outmsg  )

    def writeStuff( self, stuff ):      
        if self.myerrorfile == None:
            self.myerrorfile = open( self.filename, 'wt')
        self.myerrorfile.write( stuff  )
        
    def writeToRow( self, row ):      
        #self.myerrorfile.write( self.getStamp() ) 
        for field in row:
            tobewriten = " {} ".format( field )
            self.myerrorfile.write( tobewriten )
        self.myerrorfile.write("\n")
        
    def writeToFull( self, stuff ):      
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
        
    def getSize(self):
        st = os.stat(self.filename)
        return (st.st_size)

    def getFileLists( self ):
        return self.listofiles

    def deleteAllTmpFiles( self ):
        for file in self.listofiles:
            #print( "Removing {}".format( file ))
            os.remove( file)

    def createFile( self, chunk, n ):
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
                self.createFile( chunk, filescnt  )   
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
    
    def Close( self ):
        self.f.close()
        
    def OpenFile(self):       
        if os.path.exists(self.filename):
            self.f = open(self.filename, 'rt', errors='ignore')
            self.allow = True
            return self.f
        else:
            return None   
    
    def ReadAllFile( self ):
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
            if ( fext != ext):                
                if os.path.isfile(full):
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
        
'''
List files with extensions ext under folder
'''    
def listmyfilesfull(folder,ext):
    for file in file_ext_iterator(folder,ext,True):
        print(file)      

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
    

################################## HANDLE THREADS/PROCESS/OS ############################################   
'''
executes a commmand line cmd 
'''
def run_win_cmd(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, encoding='UTF-8')
    
    if len(result.stderr) > 0:   
        print(result.stderr)
    else:
        print(result.stdout)    


################################## HANDLE FILE ITERATORS ############################################

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
                if full_path:
                    if i > 0:
                        i = 0;
                        break;
                    i = i + 1                
                    yield root + "\\" + file_name + t,fext
                else:
                    yield file_name,fext
 
################################## HANDLE EBOOKS AND COMICS ############################################ 
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
def getalbums(folder,ext,out_dir):
    
    prev_album = ""
    prev_artist = ""
    cnt = 1
    
    with open(out_dir+"\\music_list.txt", 'w') as fl:   
        
        for file,ext in file_ext_iterator2(folder,ext,True):
            info = ""
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
            
            if len(artist) == 0:
                continue    

                
            album = f['album']
            
            if prev_album == str(f['album']):
                cnt = cnt + 1
            else:
                cnt = 1
             
            if prev_artist != str(f['artist']):
                fl.write("__________________________________________________________________________________")
                fl.write('\n\n') 
                fl.write("[ {} ]".format(str(f['artist'])))
                fl.write('\n') 
                fl.write("__________________________________________________________________________________")
                fl.write('\n\n') 
                        
            prev_album = str(f['album'])
            prev_artist = str(f['artist'])
                
            line = "\t{}-'{}' disc#{} filetype[{} - {}]".format(artist,album,cnt,ext,info)               
            fl.write(line)
            fl.write('\n')
            

################################## END OF FILE ############################################          
                

            
             