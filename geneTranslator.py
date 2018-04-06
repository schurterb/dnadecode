#Created by: Brandon Schurter 
#Last updated: Oct. 3, 2014
#
#Purpose: Read a file containing only DNA code. Convert the code to base4 (since it has only 4 symbols).
#         When converting, the number of symbols that can be used to constitute a number must be specified.
#           For example, 2213 consists of four symbols.
#         This limits the maximum possible number of symbols that may be used.

from array import array
from math import ceil

def readNtranslate( filename, skipCount):
    
    f = open(filename,'r')  #Open and read the file containing DNA code
    fileOutput = f.read()   #Read the entire file as a string
    letterDNA = list(fileOutput)  # and convert it into a list
    f.close()                
    
    #print fileOutput
        #Convert the array of letters to an array of digits according to the following cipher:
        # T = 0
        # A = 1
        # G = 2
        # C = 3
    numDNA = array('i')
    for x in letterDNA:
        if x == 'T' or x== 't':
            numDNA.append(0)
        if x == 'A' or x == 'a':
            numDNA.append(1)  
        if x == 'G' or x == 'g':
            numDNA.append(2)
        if x == 'C' or x == 'c':
            numDNA.append(3)
    
    
    #print numDNA
        #Convert the array of digits into an array of numbers 
    data = array('i') 
    for ii in range(0, len(numDNA)/skipCount +1):   #In this array, the number of values is the number of digits divided by the skipCount
        temp = 0
        
        for jj in range(0, skipCount):        #The skipCount determines how many digits are converted into 
            if ((ii*skipCount) + jj) < len(numDNA):
                temp += numDNA[(ii*skipCount) + jj] * pow(10, (skipCount -(jj +1)))
                 #If we are at the end of the array, do nothing more to the number, just append the number as it stands to data and be done.
                 
        if (ii < len(numDNA)/skipCount):
            #print temp
            data.append(temp)
            
        elif (ii < len(numDNA)/skipCount +1):
            extra_bits = len(numDNA) - (ii*skipCount)
            #print extra_bits
            #print skipCount
            if (extra_bits < skipCount) and (extra_bits > 0):
                temp = int(temp / pow(10, skipCount - extra_bits))
                #print temp
                data.append(temp)

        
        
    #print data
        
    return data
