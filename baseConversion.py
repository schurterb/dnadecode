#Created by: Brandon Schurter 
#Last updated: Sept. 10, 2014
#
#Purpose: Convert any number from one counting base to another, as long as each counting base has 10 or fewer symbols

import math

def convert2Base10(number, base):   #Converts a number from the specified base to base 10
    result = 0
    temp = number   #store a backup of the original number
    
    if base != 10:  #If the number is already in base10, just return the original number
        ii = 0
        while temp > 0:
            result += temp%10 * pow(base, ii)
            temp = temp//10 #Use floor division, we do not want any decimals
            ii += 1
            
    else:
        result = number
    
    return result
    
def convertFromBase10(number, base):    #Converts a number from base 10 to the specified base
    result = 0
    temp = number   #store a backup of the original number
    
    if base != 10:  #If the base to be converted to is base10, just return the original number
        ii = 0
        while temp > 0:
            result += temp%base * pow(10, ii)
            temp = temp//base #Use floor division, we do not want any decimals
            ii += 1
            
    else:
        result = number
            
    return result

def convert(number, base1, base2):   #It is assumed that the number entered is in base1 and being converted to base2
    
    #Convert the number to base 10
    base10_num = convert2Base10(number, base1)  
    
    #Now, convert the base10 number to the desired base
    result = convertFromBase10(base10_num, base2)
            
    return result
    
    

    