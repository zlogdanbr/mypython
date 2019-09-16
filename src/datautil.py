"""

author: Daniel V. Gomes/e5030079
March 2019
"""  

import os
import binascii
import pprint
from datetime import datetime


"""
Creates a csv file that can be used by Machine learning algorithms
"""
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
        
        
"""
Application error log
"""
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
        
"""
Split file into smaller chuncks
"""
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
 
"""
This class is used to open a file, read its lines and return
a list with all the lines
"""
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
            

"""
End of file
--------------------------------------------------------------------------------------
"""