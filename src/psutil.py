import re

"""
Util functions to make queries inside strings
"""
        
"""
This function finds a key value within a string
"""      
def findKey( key, Stringline ):

    if Stringline.find( key ) == -1:
        return False
    else:
        return True    

"""
Looks for key values specified by param1 and param2
It yields the line everytime it finds a match
"""   
def findStuffInLog( FileBufferLoaded, param1, param2, key ):

    # we yield the line that is found to allow
    # external iteration
    for line in FileBufferLoaded:
        if  ( ( findKey( param1, line ) or 
              findKey( param2, line ) ) and 
              findKey( key, line ) ):
            yield  line 

"""
Executes a regex withing a string, likely a line from a txt file
and returns the results based on the group specified by n
"""
def getElementFromLine( myString, n , regex ):

    reg = re.compile( regex )
    regexec = reg.search(myString)
    
    if regexec!= None:
        return regexec.group( n )
    else:
        return None
        
