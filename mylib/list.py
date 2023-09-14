'''
_____________________________________________________________________________________________
All my python useful functions/classes are here. 

from brlib.fileutilbr import *
from brlib.webscrapbr import *

2023 Daniel Gomes
Use with care ;-)
_____________________________________________________________________________________________
'''

# imports the functions---------------------------------------------------------

from brlib.fileutilbr import *
from brlib.webscrapbr import *

# sets the paths----------------------------------------------------------------

HOME_FOLDER =       "C:\\Users\\Administrador\\"
CALIBRE_FOLDER =    HOME_FOLDER + "Biblioteca do calibre"
KINDLE_FOLDER =     HOME_FOLDER + "My Kindle Content"
OUT_DIR =           HOME_FOLDER + "Documents\\tmp"
EPUBOR =            HOME_FOLDER + "AllDRMRemoval"
ONEDRIVE=           HOME_FOLDER + "OneDrive"
MUSIC =             HOME_FOLDER + "Music"
MUSIC_ONEDRIVE =    ONEDRIVE    + "\\Music"
FICBOOKS =          ONEDRIVE    + "\\ebooks\\Fiction"
COMICS =            ONEDRIVE    + "\\Comics"
ONEDRIVE_IMAGE =    ONEDRIVE    + "\\Pictures\\Fotos"

#main program-------------------------------------------------------------------

# functions for the main menu
def run_option1():
    os.system("cls")
    ext_mask = []
    for ext in getallextensions(ONEDRIVE_IMAGE):
        ext_mask.append(ext)
    listmyfilesfull(ONEDRIVE_IMAGE,ext_mask,OUT_DIR)

def run_option2():
    os.system("cls")
    dir = input("Digite o diretório: ")
    change_extension(dir,ZIPEXT,CBZEXT)

def run_option3():
    os.system("cls")
    get_media(MUSIC,MUSIC_MASK,OUT_DIR,0)
    
def run_option4():
    dir = input("Diretório de origem: ")
    ext = input("Extensão: ")
    remove_files(dir,ext) 
 
def run_option5():
    
    dir = input("Diretório de origem: ")
    dir_out = input("Diretório de saída: ")
    do_all_comics(dir,dir_out)

def run_option7():
    os.system("cls")
    get_media(FICBOOKS,[EPUBEXT],OUT_DIR,1)    
    
def run_option8():
    os.system("cls")
    dir = input("Diretório de origem: ")
    list_book_data_and_rename(dir,"epub")

     
def run_option9():
    os.system("cls") 
    dir = input("Diretório de origem: ")
    ext = input("Extensão: ")
    dest= input("Diretório de destino: ")
    copyfiles(dir,ext,dest)


# functions for the sub menu

def sub_menu_leave():
    return True
    
def run_option_submenu1():
    os.system("cls")
    listmyfilesfull(ONEDRIVE,DOCUMENT_MASK,OUT_DIR)
    return False
        
def run_option_submenu2():
    os.system("cls")
    listmyfilesfull(ONEDRIVE,EBOOKS_MASK,OUT_DIR)
    return False
        
def run_option_submenu3():
    os.system("cls")
    listmyfilesfull(COMICS,COMICS_MASK,OUT_DIR) 
    return False
        
def run_option_submenu4():
    os.system("cls")
    listmyfilesfull(MUSIC_ONEDRIVE,MUSIC_MASK,OUT_DIR) 
    return False
        
def run_option_submenu5():
    os.system("cls")
    path  = input("Digite caminho: ")
    ext   = input("Digite extensao: ") 
    listmyfilesfull(path,[ext],OUT_DIR) 
    return False    
        
def run_option_submenu6():
    os.system("cls")
    path  = input("Digite caminho: ")
    fil   = input("Nome do arquivo: ")
    find_file(path,fil)
    return False
        
def run_option_submenu7():
    os.system("cls")
    try:
        url1  = input("Digite URL: ")   
        getAllImagesFromSite(url1)
    except:
        print("Erro")
        return False
    return False
        
def run_option_submenu8():
    os.system("cls")
    try:
        dir_in = input("Digite diretório de origem: ") 
        ext_in = input("Digite extensão de origem: ") 
        ext_out = input("Digite extensão de saída: ") 
        dir_out = input("Digite diretório de saída: ") 
        convert_batch(dir_in,ext_in,ext_out,dir_out)
    except:
        print("Erro") 
        return False
    return False
    
def run_option_submenu9():
    os.system("cls")
    try:
        url  = input("Digite a URL: ")
        file_name   = input("Nome do arquivo final: ")   
        downloadfile(url,file_name)
    except:
        print("Erro")  
        return False
    return False
        
def run_option_submenu10():
    os.system("cls")
    try:
        arquiv  = input("Caminho arquivo csv: ")
        convert_csv_excel( arquiv ) 
    except:
        print("Erro")
        return False

    return False
    
def DoExit():
    print("Exiting application")
    exit()
    
def run_submenu1():
    
    # configure the menu using this dictionary
    submenuoptions = { 
                1:[" Listar documentos one drive", run_option_submenu1],
                2:[" Listar ebooks one drive", run_option_submenu2],
                3:[" Listar quadrinhos one drive.", run_option_submenu3],
                4:[" Listar mp3s one drive", run_option_submenu4],    
                5:[" Busca customizada", run_option_submenu5],
                6:[" Busca por arquivo", run_option_submenu6],
                7:[" Listar imagens URL", run_option_submenu7],  
                8:[" Converter formatos de ebook", run_option_submenu8], 
                9:[" Download de arquivo", run_option_submenu9],
                10:["Convert csv para excel", run_option_submenu10],
                # add other calls here
                11:["Voltar", sub_menu_leave]
              }   
                
    runmenu(submenuoptions,"Utilidades: ", True)
  

def main(argv):
    
    # configure the menu using this dictionary
    menuoptions = { 
                1:[" Listar todos arquivos de imagem do onedrive", run_option1],
                2:[" Mudar a extensão dos arquivos zip para cbz.", run_option2],
                3:[" Criar lista de mp3s por artista e album.", run_option3],
                4:[" Remover arquivos", run_option4],  
                5:[" Remover DRM comics",run_option5],
                7:[" Criar lista de ebooks", run_option7],  
                8:[" Renomear livros formato epub", run_option8], 
                9:[" Copiar arquivos", run_option9],
                10:["Mais opções", run_submenu1],
                # add other calls here
                11:["Exit", DoExit]
              }
              
    runmenu(menuoptions,"Janela Inicial")
                 
if __name__ == '__main__':
    main(sys.argv)  

################################## END OF FILE ############################################     