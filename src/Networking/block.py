import sys
import os
import subprocess
import re
import pprint
import socket
import time
from threading import Thread



def monitorPorts( ipaddress, port, repeat_for=1):
    
    print( "Connecting to {} at port {}".format(ipaddress,port))
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)    
    result = sock.connect_ex((ipaddress,port))    
    
    while True:
        time.sleep(60)
        
        if repeat_for == 0:
            break
        repeat_for = repeat_for - 1    
        pass
        
    sock.close()
    print( "Disconnecting from  {} at port {}".format(ipaddress,port))
 

def make_range_busy( ips, port ):

    mythreads = []
    
    for ip in ips:
    
        myargs = (ip,port,5)
        new_thread = Thread(target=monitorPorts,args=myargs)
        new_thread.start()
        mythreads.append(new_thread)
        
    
    for t in mythreads:
        t.join()
        
def main(argv):
    
    ips = [ "0.0.0.0"]
    port = 0


    make_range_busy(ips,port)
    

if __name__ == '__main__':
    main(sys.argv)    