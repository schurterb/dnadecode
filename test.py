#Created by: Brandon Schurter 
#Last updated: Sept. 10, 2014
#
#This script just exists to test other python functions

from geneTranslator import readNtranslate

output = readNtranslate('test.txt', 3)

outFile = open('DNAdata/output.txt', 'w')
for x in output:
    outFile.write(str(x) + " ")
    
    
outFile.close()
