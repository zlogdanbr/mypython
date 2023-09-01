'''
Removing DRM

Step 1 Download calibre         https://calibre-ebook.com

Step 2 Install DRM plugins      https://www.epubor.com/calibre-drm-removal-plugins.html

Step 3 Set the paths below:

CALIBRE_FOLDER = "C:\\Users\\Administrador\\Biblioteca do calibre"
KINDLE_FOLDER = "C:\\Users\\Administrador\\Documents\\My Kindle Content"
OUT_DIR = "C:\\Users\Administrador\\Documents\\tmp"

Step 4 Add the desired action to main, ex:

    copyfiles(CALIBRE_FOLDER,AZWEXT)
    convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT)
    change_extension(OUT_DIR,ZIPEXT,CBZEXT)
    remove_files(OUT_DIR,EPUBEXT)
    
For comics:    
I usually copy  copyfiles(KINDLE_FOLDER,AZWEXT)  
Then I manually add them to calibre ( drag and drop )

Calibre will create a decent folder structure at  CALIBRE_FOLDER
I call convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT) and all zip files will be placed at
OUT_DIR


Then change_extension(OUT_DIR,ZIPEXT,CBZEXT) will simply rename the zip files to cbz
allowing any reader to open them.
'''

from utildvg import *
 
CALIBRE_FOLDER = "C:\\Users\\Administrador\\Biblioteca do calibre"
KINDLE_FOLDER = "C:\\Users\\Administrador\\Documents\\My Kindle Content"
OUT_DIR = "C:\\Users\Administrador\\Documents\\tmp"
EPUBOR = "C:\\Users\\Administrador\\AllDRMRemoval"

ZIPEXT = "zip"
CBZEXT = "cbz"
AZWEXT = "azw"
AZWEXT3 = "azw3"
EPUBEXT = "epub"
PDFEXT = "pdf"

def main(argv):
    #copyfiles(CALIBRE_FOLDER,AZWEXT,OUT_DIR)
    #convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT)
    #change_extension(OUT_DIR,ZIPEXT,CBZEXT)
    #remove_files(OUT_DIR,EPUBEXT)  
    listmyfilesfull("C:\\Users\\Administrador\\OneDrive",[EPUBEXT,CBZEXT,PDFEXT])
    #convert_batch(KINDLE_FOLDER,AZWEXT,AZWEXT3,OUT_DIR)
    #remove_files(CALIBRE_FOLDER,PDFEXT)
    #convert_batch(OUT_DIR,AZWEXT,PDFEXT,OUT_DIR)
    #convert_batch(OUT_DIR,AZWEXT3,PDFEXT,OUT_DIR)
    pass

if __name__ == '__main__':

    main(sys.argv)
