import sys
import os

# create functions for the menu
def run_option1():
    os.system("cls")
    print("Do 1")

def run_option2():
    os.system("cls")
    print("Do 2")

def DoExit():
    print("Exiting application")
    exit()

def DoDefaultError():
    os.system("cls")
    print("Invalid entry")


# configure the menu using this dictionary
meuoptions = { 
                1:["Call function 1", run_option1],
                2:["Call function 2", run_option2],
                # add other calls here
                8:["Exit", DoExit]
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