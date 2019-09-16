import socket
import sys, os

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
    
def sendMessage( host, port, BUFFER_SIZE , msg ):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.connect((host, port))
        # We convert str to bytes
        socket_tcp.send( msg.encode('utf-8') )
        data = socket_tcp.recv(BUFFER_SIZE)
 
def monitorPortsInterface(): 
    ipaddress =input("Enter ip address or domain for port scanning:")
    port_init= input("Enter first port: ")
    port_end = input("Enter last port: ")
    monitorPorts( ipaddress, port_init, port_end)
    
def main(argv):
    monitorPortsInterface()
    
if __name__ == '__main__':
    main(sys.argv)