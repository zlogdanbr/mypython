'''
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
_____________________________________________________________________________________________    
'''
# imports the functions---------------------------------------------------------
from fileutilbr import *
# sets the paths----------------------------------------------------------------
CALIBRE_FOLDER = "C:\\Users\\Administrador\\Biblioteca do calibre"
KINDLE_FOLDER = "C:\\Users\\Administrador\\Documents\\My Kindle Content"
OUT_DIR = "C:\\Users\Administrador\\Documents\\tmp"
EPUBOR = "C:\\Users\\Administrador\\AllDRMRemoval"
ONEDRIVE= "C:\\Users\\Administrador\\OneDrive"
MUSIC = "C:\\Users\\Administrador\\Music"
PYBOOKS = "C:\\Users\\Administrador\\OneDrive\\Tutorials And Important Files\\Programming\\Python"
FICBOOKS = "C:\\Users\\Administrador\\OneDrive\\ebooks\\Fiction"
COMICS = "C:\\Users\\Administrador\\OneDrive\\Comics"
ONEDRIVE_IMAGE = "C:\\Users\\Administrador\\OneDrive\\Pictures\\Fotos"
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
EBOOKS_MASK = [EPUBEXT,CBZEXT,PDFEXT]
COMICS_MASK = [CBZEXT,CBREXT]
#main program-------------------------------------------------------------------

# create functions for the menu
def run_option1():
    os.system("cls")
    ext_mask = []
    for ext in getallextensions(ONEDRIVE_IMAGE):
        ext_mask.append(ext)
    listmyfilesfull(ONEDRIVE_IMAGE,ext_mask,OUT_DIR)

def run_option2():
    os.system("cls")
    change_extension(OUT_DIR,ZIPEXT,CBZEXT)

def run_option3():
    os.system("cls")
    get_media(MUSIC,MUSIC_MASK,OUT_DIR,0)
    
def run_option4():
    os.system("cls")
    remove_files(CALIBRE_FOLDER,PDFEXT)
    
def run_option5():
    os.system("cls")
    convert_batch(KINDLE_FOLDER,AZWEXT,AZWEXT3,OUT_DIR)         
    
def run_option6():
    os.system("cls")
    print("Digite a opção:")
    print("[1]Listar documentos one drive")
    print("[2]Listar ebooks one drive")
    print("[3]Listar quadrinhos one drive")

    
    ch = -1
    try:
        ch=int(input("Digite sua opçao:"))
    except:
        ch = -1   

    if   ch == -1:
        print("Opcao invalida.")
    elif ch == 1:
        listmyfilesfull(ONEDRIVE,DOCUMENT_MASK,OUT_DIR)
    elif ch == 2:
        listmyfilesfull(ONEDRIVE,EBOOKS_MASK,OUT_DIR)
    elif ch == 3:
        listmyfilesfull(COMICS,COMICS_MASK,OUT_DIR)        
    else:
        print("Opcao invalida.")
    
def run_option7():
    os.system("cls")
    get_media(FICBOOKS,[EPUBEXT],OUT_DIR,1)    
 
def run_option8():
    os.system("cls")   
    printextensions(ONEDRIVE_IMAGE)
    
def run_option9():
    os.system("cls") 
    ext = input("Extensão:")
    dest= input("Diretório de destino: ")
    copyfiles(ONEDRIVE_IMAGE,ext,dest)
    
def run_option10():
    os.system("cls") 
    ext = input("Extensão:")
    remove_files(ONEDRIVE_IMAGE,ext)    

def DoExit():
    print("Exiting application")
    exit()

def DoDefaultError():
    os.system("cls")
    print("Invalid entry")


# configure the menu using this dictionary
meuoptions = { 
                1:[" Listar todos arquivos de imagem do onedrive", run_option1],
                2:[" Mudar a extensão dos arquivos zip para cbz.", run_option2],
                3:[" Criar lista de mp3s por artista e album.", run_option3],
                4:[" Remover pdfs da biblioteca do Calibre", run_option4],    
                5:[" Remove DRM de arquivos kindle", run_option5],
                6:[" Listar arquivos", run_option6],
                7:[" Criar lista de ebooks", run_option7],  
                8:[" Listar extensões de fotos", run_option8],
                9:[" Copiar arquivos", run_option9],
                10:["Remover arquivos", run_option10],
                # add other calls here
                11:["Exit", DoExit]
              }

def runmenu():
    
    while True:
        os.system("cls")# Linux/unix use "clear"

        print("-------------------------------------------")
        print("Options:")
        print("-------------------------------------------")
        for key,actions in meuoptions.items():
            print("({})      {}".format(key,actions[0]))           
        print("-------------------------------------------")       
        
        ch = -1
        try:
            ch=int(input("Enter your choice: "))
        except:
            ch = -1
        
        if ch in meuoptions:
            f = meuoptions[ch][1]
            f()
        else:
            DoDefaultError()
  
        input("Press enter to continue.")

def main(argv):
    runmenu()
                 
if __name__ == '__main__':
    main(sys.argv)  