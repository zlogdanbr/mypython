_____________________________________________________________________________________________
Removing DRM
_____________________________________________________________________________________________

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
    
_____________________________________________________________________________________________
Removing DRM comics: 
_____________________________________________________________________________________________
   
I usually copy  copyfiles(KINDLE_FOLDER,AZWEXT)  
Then I manually add them to calibre ( drag and drop )

Calibre will create a decent folder structure at  CALIBRE_FOLDER
I call convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT) and all zip files will be placed at
OUT_DIR


Then change_extension(OUT_DIR,ZIPEXT,CBZEXT) will simply rename the zip files to cbz
allowing any reader to open them.
_____________________________________________________________________________________________
Usual usage
_____________________________________________________________________________________________
copyfiles(CALIBRE_FOLDER,AZWEXT,OUT_DIR) # copy files with extension AZWEXT to out dir
convert_batch(CALIBRE_FOLDER,AZWEXT3,ZIPEXT)# convert AZWEXT3 ( NO DRM ) to zip
change_extension(OUT_DIR,ZIPEXT,CBZEXT)
remove_files(OUT_DIR,EPUBEXT)  
listmyfilesfull(ONEDRIVE,IMAGES_MASK)
convert_batch(KINDLE_FOLDER,AZWEXT,AZWEXT3,OUT_DIR)
remove_files(CALIBRE_FOLDER,PDFEXT)
convert_batch(OUT_DIR,AZWEXT,PDFEXT,OUT_DIR)
convert_batch(OUT_DIR,AZWEXT3,PDFEXT,OUT_DIR)
_____________________________________________________________________________________________
Creates a list of your audio files from the MASK and folder
_____________________________________________________________________________________________
Creates a list of audio files 
MUSIC_MASK   = ["mp3","flac", "ogg"]
getalbums(MUSIC,MUSIC_MASK,OUT_DIR)
