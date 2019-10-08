#
#  @file apic.py
#  @brief This file contains util functions to send xml requests
#  to a xmlrpc web service
#  @author Daniel V. Gomes

import os
import sys
import requests
import xml.dom.minidom
from jinja2 import Template
import pprint
import xml.etree.ElementTree as ET


'''
This should be used with Jinja to fill in multiple parameters in an xml template
''' 
class Container:
    key = ""
    value = ""
    type = ""

    def __init__(self, key, value, type ): 
        self.key = key
        self.value = value
        self.value = type
    

'''
Copies a xml file to a string
'''
def readXMLfiletostring( xmlfile ):
    xmlObject = xml.dom.minidom.parse(xmlfile)
    return xmlObject.toxml()
    

'''
It uses Jinja2 to create a xml file based on a template
'''    
def createXMLQuery( 
                    key,
                    keyvalue,
                    xmltmpl):

    t = Template(xmltmpl)
    xmlmsg = t.render(
                        key=key,
                        keyvalue=keyvalue)
    return xmlmsg
    
'''
It uses Jinja2 to create a xml file based on a template
Should one day accept multiple fields
'''      
def createXMLQueryX( 
                    tableName,
                    keys,
                    xmltmpl):

    t = Template(xmltmpl)
    xmlmsg = t.render(  tableName=tableName,
                        keys=keys)
    return xmlmsg 
    

'''
This is the actual call to post method
'''
def callApiQuery( serverIP, xmlmsg ):
    headers = {
    'Content-Type': 'text/xml',
    }
    response = requests.post(serverIP, headers=headers, data=xmlmsg)
    return response
    

'''
Parses a string containing a xml file converted to a string
Needs some adaptions
'''
def parseXMLOut( xmlresponse, opt  ):
    root = None
    register = {}
    
    if opt == 0: # reads from a string
        root = ET.fromstring(xmlresponse)
    else: # reads from a file
        tree = ET.parse(xmlresponse)
        root = tree.getroot()
        
    for m1l in root.iter('member'):
          
        field  = m1l.find('name').text
        name   = m1l.find('value/string')
        
        if name != None:
            if name.text != None:
                print( "{} - {}".format(field, name.text ))
                register[field] = name.text
            else:
                print( "{} - Empty field".format(field) )
                register[field] = "Empty field"
        else:
            name = m1l.find('value/i4')
            if name != None:
                print( "{} - {}".format( field, name.text ))
                register[field] = name.text
            else:
                name = m1l.find('value/i8')
                if ( name != None ):
                    print( "{} - {}".format( field, name.text ))
                    register[field] = name.text 
                else:                   
                    print( "{} - Not parsed".format(field) )    
                    register[field] = "Not parsed"
                
    return register

'''
This does the call to post using a fixed xml file
'''
def ProcessXml( URLserver, xfilename ):
    xmlqueried = readXMLfiletostring(xfilename)
    res = callApiQuery( URLserver, xmlqueried )   
    print(res.text)    
    print("Status RESP- {}".format(res))
    
    if res.status_code == requests.codes.ok:
        return res.text
        #return parseXMLOut(res.text,0)
    else:
        return ""
    
'''
This does the call to post using a filled xml file
'''    
def ProcessTempl( URLserver, xfilenametmp, key, key_value ):
    xmltemplate = readXMLfiletostring(xfilenametmp)
    q = createXMLQuery(  key, key_value, xmltemplate )
    res = callApiQuery( URLserver, q )        
    print(res.text)
    print("Status RESP- {}".format(res))
    
    if res.status_code == requests.codes.ok:
        return parseXMLOut(res.text,0)
   

# program main function just input data
# JURL=http://10.99.168.81:9080/api/xmlrpc ----> JAVA
# XURL=http://10.99.168.81:8084/fcgi-bin/xmlrpc_server.cgi ---> XML API
# python apic.py $XURL ../xml/add_fees.xml
# python apic.py $XURL ../xml/query_fees.xml

def main(argv):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Default parameters not allowed
    if len(argv) <= 2 :
        print("Error. Too few parameters.")
        return      
        
    elif len(argv) == 5:
        # Values must be entered
        URLserver = argv[1]             # URL of the server  
        xfilename = argv[2]             # name of the xml with the template
        key       = argv[3]             # which key will be used to search
        value     = argv[4]             # the value of the the key
        
        if ( os.path.exists(xfilename)):
            ProcessTempl(URLserver,xfilename,key,value)
        else:
            print("Xml template file does not exist.")
            
    elif len(argv) == 3:
        # XML file is executed as is
        URLserver = argv[1]             # URL of the server  
        xfilename = argv[2]             # name of the xml with the template
        
        if ( os.path.exists(xfilename)):
            ProcessXml(URLserver,xfilename)
        else:
            print("Xml template file does not exist.")    
    else:
        print("Error, wrong parameter usage.")
        return          
    
# main function              
if __name__ == '__main__':
    main(sys.argv)

# end

