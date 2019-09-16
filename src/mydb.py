"""
Project validate batch files
author: Daniel V. Gomes/e5030079
March 2019
"""  

import cx_Oracle
import pprint
import binascii
import traceback
import os
import sys

"""
Class that connects to the database and executes query
"""
class mydatabaser:

    resultsobject = []
    rowsproblem   = []
    cur = None
    con = None

    '''
    Connects to the database
    '''
    def Connect( self, database ):
        try:
            print("Trying to connect to the database...")
            self.con = cx_Oracle.connect(database)         
            self.cur = self.con.cursor()
            return 1
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return 0    

    '''
    Gets the result of que query
    '''
    def getLine( self )  :
        return self.resultsobject         
    
    '''
    Verifies database against null values
    '''
    def checkNulls( self, table, ssizeofverify ):
        option = 0
        
        if ssizeofverify == "all":
            option = -1
        else:
            try:
                option = int(ssizeofverify)
                if option < -2 or option == 0:
                    option = 10
            except Exception as e:
                print("Invalid value, testing 1 row...")
                option = 1

        ret = 0
        try:
            query = "select * from {}".format(table)
            self.cur.arraysize = 50
            self.cur.execute(query)
            
            if option == -1:
                print("Fetching data...")
                result = self.cur.fetchall()
            else:
                print("Fetching data...")
                result = self.cur.fetchmany(numRows=option) 

            print("Counting rows with invalid values...")
            for row in result:
                for col in row:
                    if col == None:
                        ret = ret + 1                      
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return ret
        
        return ret
    
    '''
    This is the actual query function
    '''
    def Fetch( self, query, option ):
        try:
            #print(query)
            self.cur.execute(query)            
            if option == 0:                  
                resultuple = self.cur.fetchone()
            else:
                resultuple = self.cur.fetchall()

            if resultuple == None:              
                return -1
            else:       
                self.resultsobject = list(resultuple)      
                return 0
            
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return -1

    def closeconnection( self ):
        print("Closing connection to the database...")
        self.cur.close()
        self.con.close()


# python mydb.py 'eglclrmasqa/eglclrmasqa@10.99.168.30/orcl12' 'select * from EGL_ARBITRO'
def main(argv):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Default it will always execute this fixed query
    if len(argv) < 2:
        print("Wrong usage. Too few parameters")
        return      
    
    # Values must be entered
    database  = argv[1] 
    query     = argv[2]  
    
    db = mydatabaser()
    db.Connect( database )
    if db.Fetch( query, 1 ) >= 0:
        print( db.getLine() )
    else:
        print("Error in query.")
    db.closeconnection()
    
              
if __name__ == '__main__':
    main(sys.argv)
    
"""
End of file
--------------------------------------------------------------------------------------
"""