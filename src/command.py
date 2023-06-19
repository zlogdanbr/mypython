import sys
import os
import subprocess

        
def run_win_cmd(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, encoding='UTF-8')
    
    if len(result.stderr) > 0:   
        print(result.stderr)
    else:
        print(result.stdout)
    
        
        
def main(argv):

    if len(argv) <= 1:
        print("Error: no command has been passed. ")
        return 
        
    try:
        run_win_cmd(argv[1])
    except:
        print("Error running script")

      

if __name__ == '__main__':
    main(sys.argv)