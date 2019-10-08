import random
import time
import wx

from threading import Thread
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
            print("Executing something")
            time.sleep(3)
        except ConnectionError as e:
            self.output.write(str(e))
        finally:
            self.output.write("Unkown Error")
            
