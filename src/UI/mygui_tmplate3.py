import os
import sys
import subprocess
import time
import wx

from th import MyThread

# Define the tab content as classes:
class TabOne(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.create_ui()
        self.SetSizer(self.main_sizer)
        self.threadrunning = False
        
    def create_ui( self ):
    
        # first row in the layout
        row_sizer = wx.BoxSizer()
        lblxml = wx.StaticText(self, label='Load XML Configuration:')
        row_sizer.Add(lblxml, 0, wx.ALL | wx.CENTER, 5)
        
        self.xmfilecrtl = wx.TextCtrl(self, style=wx.TE_READONLY)
        row_sizer.Add(self.xmfilecrtl, 1, wx.ALL | wx.EXPAND, 5)
        open_dir_btn = wx.Button(self, label='Choose File')
        open_dir_btn.Bind(wx.EVT_BUTTON, self.on_choose_folder)
        row_sizer.Add(open_dir_btn, 0, wx.ALL, 5)
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)
        
        # second row
        row_sizer = wx.BoxSizer()
        lblurl = wx.StaticText(self, label='Web service URL:')
        row_sizer.Add(lblurl, 0, wx.ALL | wx.CENTER, 5)
        
        #self.webservice = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.urlnames = ['http://10.99.168.81:8084/fcgi-bin/xmlrpc_server.cgi',
                        'http://10.99.168.81:9080/api/xmlrpc']
                        
        self.webCbo = wx.ComboBox(self, value="", choices=self.urlnames )
        self.webCbo.Bind(wx.EVT_COMBOBOX, self.loadServices)
        
        #row_sizer.Add(self.webservice, 1, wx.ALL | wx.EXPAND, 5)
        row_sizer.Add(self.webCbo, 1, wx.ALL | wx.EXPAND, 5)
        
        sendmsg = wx.Button(self, label='Send')
        sendmsg.Bind(wx.EVT_BUTTON, self.on_send_msg)
        row_sizer.Add(sendmsg, 0, wx.ALL, 5)     
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)  
        
        # third row
        row_sizer = wx.BoxSizer()       
        self.output = wx.TextCtrl(self, size = (200,500), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
        row_sizer.Add(self.output, 1, wx.ALL | wx.EXPAND, 5)    
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND) 
 
        # fourth row
        row_sizer = wx.BoxSizer()       
        self.btn_clear = wx.Button(self, label='Clear Text')
        self.btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)
        row_sizer.Add(self.btn_clear, 0, wx.ALL, 5)   
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)       

    def loadServices( self, event):
        self.webservice  = event.GetString()
        self.output.write("Option {} selected \n".format(self.webservice))
        
    def on_clear( self, event ):
        if self.threadrunning == False:
            self.output.Clear()     
                          
    def on_choose_folder( self, event ):
        self.on_file_nogui()
    
    def on_file_nogui(self):
        wildcard = "JPEG files (*.xml)|*.xml"
        with wx.FileDialog(None, "Choose a file",
                            wildcard=wildcard,
                            style=wx.ID_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.xmfilecrtl.SetValue(dialog.GetPath())
                    
    def on_send_msg( self, event ): 
        if self.xmfilecrtl.IsEmpty() == False and self.webservice != "":
            self.threadrunning = True
            xml = self.xmfilecrtl.GetValue()
            #webservice = self.webservice.GetValue()
            my_thread = MyThread( xml, self.webservice, self.output )
            my_thread.start()
            self.output.Refresh()
            self.threadrunning = False
        else:
            style = wx.OK|wx.CENTER|wx.ICON_INFORMATION
            result = wx.MessageBox(     "XML file not correctly configured \n or web service not entered",
                                        "Error",
                                        style)


class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20,20))

class TabThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20,20))

class TabFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="My template app")

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Create the tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)
        tab3 = TabThree(nb)
        tab4 = TabFour(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Send")
        nb.AddPage(tab2, "Process")
        nb.AddPage(tab3, "Acquire")
        nb.AddPage(tab4, "Evaluate")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
