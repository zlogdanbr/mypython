import wx
 
# Define the tab content as classes:
class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (20,20))

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


class myapp(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.InitUI()

    menu1 =  {   #ID                MenuItem            qm              Event
                 wx.ID_NEW :        ['&New',              1,          "OnNew", 'icon/document-new.png'],
                 wx.ID_OPEN:        ['&Open',             1,          "OnLoad", 'icon/document-open.png'],
                 wx.ID_SAVE:        ['&Save',             1,          "OnSave", 'icon/document-save.png'],   
                 wx.ID_EXIT:        ['&Quit\tCtrl+W',     1,          "OnQuit",'icon/go-down.png']            
             }
 

    menu2 =  { 
                wx.ID_DEFAULT:      ['&Load',         1,                "OnLoadVid", 'icon/media-playback-start.png'],                     
             }
                                 
    def CreateMenu( self, options, eventHandler ):
 
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

        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Create the tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)
        tab3 = TabThree(nb)
        tab4 = TabFour(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")
        nb.AddPage(tab3, "Tab 3")
        nb.AddPage(tab4, "Tab 4")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        
        # Creates the menubar object
        menubar = wx.MenuBar()

        # event handlers are mapped here
        eventHandlerMenu1   =  {
                                  "OnQuit": self.OnQuit,
                                  "OnSave": self.OnSave,
                                  "OnLoad": self.OnLoad,
                                  "OnNew" : self.OnNew
                                } 
                         
        eventHandlerMenu2   =  {
                                    "OnLoadVid": self.OnLoadVid,
                               }                          
                                    

        # creates the first menu item
        fileMenu = self.CreateMenu(self.menu1, eventHandlerMenu1 )
        
        # creates the first menu item
        actionMenu = self.CreateMenu(self.menu2, eventHandlerMenu2)
                            
        # adds the menu to frame
        menubar.Append(fileMenu, '&File')
        menubar.Append(actionMenu, '&Action')
       
        self.SetMenuBar(menubar)
        self.SetSize((500, 450))
        self.Centre()

    # Event handlers  should be mapped above 
    def OnQuit(self, e):
        self.Close()
            
    def OnSave(self, e):
        print("Should save")    
        
    def OnLoad(self, e):
        print("Should Load")  

    def OnNew(self, e):
        print("Should create new")   
        
    def OnLoadVid(self,e ):
        print( "Should load vid")                 
        
def main():

    app = wx.App()
    myview = myapp(None, title='My Application Skeleton')
    myview.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
