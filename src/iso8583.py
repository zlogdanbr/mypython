import binascii

class ParseIsobitmap:
    
    def __init__( self, bitmapAsString ):
        self.binString = format( int( bitmapAsString , 0 ), "b" )
        self.numOfBits   = len( self.binString )
        self.hasSecondBitMap = self.checkIfSecondaryBitmap( self.binString )
        
    def checkIfSecondaryBitmap( self, bitmap_binstring ):
        if bitmap_binstring == '0':
            return False
        return True
        
    def getBitMapstring( self ):
        return self.binString 
        
    def getNumOfBits( self ):
        return self.numOfBits
    
    def hasSecondbitMap( self ):
        return self.hasSecondBitMap
        
    def getBitsSet( self ):
        cnt = 0
        for bit in self.binString:
            if cnt != 0:
                if bit != '0':
                    yield cnt
            cnt = cnt + 1
    
    # todo this should convert string value to the iso8583 values
    # 
    def convertStrToType( str, type ):
        pass
    
def main():
    bitmapstring = "0xB220000000100000"
    b = ParseIsobitmap( bitmapstring )
    print( "{} {}  {} ".format( b.getNumOfBits(), b.getBitMapstring(), b.hasSecondbitMap() ))
    
    for des in b.getBitsSet():
        print( des )
    
if __name__ == '__main__':
    main()