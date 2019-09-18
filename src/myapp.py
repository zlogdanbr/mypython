
import wx


class myapp(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(myapp, self).__init__(*args, **kwargs)
        self.InitUI()

    menu1 =  { 
                 wx.ID_NEW :  ['&New', 0],
                 wx.ID_OPEN:  ['&Open', 0],
                 wx.ID_SAVE:  ['&Save', 0],   
                 wx.ID_EXIT:  ['&Quit\tCtrl+W',1]            
             }
             
    menu2 =  { 
                wx.ID_NEW: ['&Load Video',0],                    
                wx.ID_OPEN: ['&Start Processing',0],               
                wx.ID_SAVE: ['&Stop video',0]   
             }
             
                      
    def CreateMenu( self, options ):
        
        themenu = wx.Menu()
        qmiadd = []
        
        for id in options:
        
            if options[id][1] == 0:
                themenu.Append( id, options[id][0] ) 
            else:
                themenu.AppendSeparator()
                qmi = wx.MenuItem( themenu, id, options[id][0])
                themenu.Append(qmi) 
                qmiadd.append( qmi )
                
        return themenu, qmiadd       

    def InitUI(self):

        # Creates the menubar object
        menubar = wx.MenuBar()

        # creates the first menu item
        fileMenu, qmi = self.CreateMenu(self.menu1)

        # Adds event handler to que quit option
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi[0])
        
        # creates the first menu item
        actionMenu, qmi2 = self.CreateMenu(self.menu2)


        # adds the menu to frame
        menubar.Append(fileMenu, '&File')
        menubar.Append(actionMenu, '&Action')

        
        self.SetMenuBar(menubar)
        self.SetSize((500, 450))
        self.SetTitle('Image Tool')
        self.Centre()

    def OnQuit(self, e):
        self.Close()
        
def main():

    app = wx.App()
    myview = myapp(None, title='Image Camera tools')
    myview.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()