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

HOME_FOLDER =       str(Path.home())+"\\"
OUT_DIR =           HOME_FOLDER + "Documents\\tmp"
MUSIC =             HOME_FOLDER + "Music"


#main program-------------------------------------------------------------------

# functions for the main menu


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
    dir = input("Diretório de origem: ")
    get_media(dir,[EPUBEXT],OUT_DIR,1)    
    
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
        
def run_option_submenu3():
    
    os.system("cls")
    dir = input("Diretório de origem: ")
    listmyfilesfull(dir,COMICS_MASK,OUT_DIR) 
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
                9:[" Busca customizada", run_option_submenu5],
                10:["Busca por arquivo", run_option_submenu6],
                11:["Listar imagens URL", run_option_submenu7],  
                12:["Converter formatos de ebook", run_option_submenu8], 
                13:["Download de arquivo", run_option_submenu9],
                14:["Convert csv para excel", run_option_submenu10],
                15:["Listar HQs em um diretório",run_option_submenu3],
                # add other calls here
                21:["Voltar", sub_menu_leave]
              }   
                
    runmenu(submenuoptions,"Utilidades: ", True)
  

def main(argv):
    
    # configure the menu using this dictionary
    menuoptions = { 
                1:[" Mudar a extensão dos arquivos zip para cbz.", run_option2],
                2:[" Criar lista de mp3s por artista e album.", run_option3],
                3:[" Remover arquivos", run_option4],  
                4:[" Remover DRM comics",run_option5],
                5:[" Criar lista de ebooks", run_option7],  
                6:[" Renomear livros formato epub", run_option8], 
                7:[" Copiar arquivos", run_option9],
                8:[" Mais opções", run_submenu1],
                # add other calls here
                11:["Exit", DoExit]
              }
              
    runmenu(menuoptions,"Janela Inicial")
                 
if __name__ == '__main__':
    main(sys.argv)  

################################## END OF FILE ############################################     