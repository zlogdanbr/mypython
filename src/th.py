import random
import time
import wx

from threading import Thread
from apic import ProcessXml
from requests.exceptions import ConnectionError

class MyThread(Thread):
    """
    A threading example
    """
    def __init__(self, xml, webservice, output):
        """Initialize the thread"""
        Thread.__init__(self)
        self.xml  = xml
        self.webservice  = webservice
        self.output  = output

    def run(self):
        """Run the thread"""
        try:
            self.output.write("Sending {} to {} \n".format(self.xml,self.webservice ))       
            resp = ProcessXml(self.webservice, self.xml)
            self.output.write(resp)
            time.sleep(3)
        except ConnectionError as e:
            self.output.write(str(e))
        finally:
            self.output.write("Unkown Error")
            
