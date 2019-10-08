import os
import sys
import subprocess
import time
import wx

from th import MyThread

class MainPanel(wx.Panel):

    def __init__(self, parent):
    
        #scrolled.ScrolledPanel.__init__(self, parent, style=wx.SUNKEN_BORDER)
        super().__init__(parent)
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

menu1 =  {   #ID                MenuItem            qm              Event
         wx.ID_OPEN:        ['&Open XML file',             1,          "OnLoad", 'icon/document-open.png'],  
         wx.ID_EXIT:        ['&Quit\tCtrl+W',              1,          "OnQuit",'icon/go-down.png']            
         } 

                         
class toolgui(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(toolgui, self).__init__(*args, **kwargs)
        self.InitUI()
                                 
    def CreateMenu( self, options, eventHandler ):
 
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENUBAR))
        themenu = wx.Menu()
    
        
        # iterates over the configure options for the menu
        for id in options:
            qmi = None
                        
            if options[id][1] == 0:
                # this is a simple menu item nothing connected
                # should not be used in the future
                themenu.Append( id, options[id][0] ) 
            else:
                # These are the actual menu items attached with events
                # I need to add some icons
                themenu.AppendSeparator()
                qmi = wx.MenuItem( themenu, id, options[id][0])
                qmi.SetBitmap(wx.Bitmap(options[id][3]))
                themenu.Append(qmi) 

            # Adds event handler to que quit option
            # folder-open.png
            if options[id][1] != 0:
                if qmi != None:
                    self.Bind(wx.EVT_MENU, eventHandler[ options[id][2] ], qmi)
                
        return themenu      
                
    def InitUI(self):
        
        self.mypanel = MainPanel(self)
               
        # Creates the menubar object
        menubar = wx.MenuBar()

        # event handlers are mapped here
        eventHandlerMenu1   =  {
                                  "OnQuit": self.OnQuit,
                                  "OnLoad": self.OnLoad
                                } 

        # creates the first menu item
        fileMenu = self.CreateMenu( menu1, eventHandlerMenu1 )

                            
        # adds the menu to frame
        menubar.Append(fileMenu, '&File')
        
        self.SetIcon(wx.Icon('icon/utilities-terminal.png'))
        self.SetSize( 700, 700 )
        self.SetMenuBar(menubar)
        self.Centre()

    # Event handlers  should be mapped above 
    def OnQuit(self, e):
        self.Close() 
        
    def OnLoad(self, e):
        self.mypanel.on_file_nogui()
       
def main():

    app = wx.App()
    myview = toolgui(None, title='Eglobal API Testing Tool')
    myview.Show()
    app.MainLoop()
 

if __name__ == '__main__':
    main()
