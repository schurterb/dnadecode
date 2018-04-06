#Created by: Brandon Schurter 
#Last updated: Sept. 10, 2014
#
#This script just exists to test other python functions

from baseConversion import convert, convert2Base10, convertFromBase10

val = [3, 10, 42, 256, 1, 0, 2, 26, 12, 8]
out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
out2 = out

#val = [1024]
#out = [0]
#out2 = [0]

print "Converting from base10 to base2"
ii = 0
for x in val:
    out[ii] = convertFromBase10(x, 2)
    print str(x) + " converts to " + str(out[ii])
    ii += 1

print "\n and back from base2 to base 10"
ii = 0
for x in out:
    out2[ii] = convert2Base10(x, 2)
    print str(x) + " converts to " + str(out2[ii])
    ii += 1

val = [3, 10, 42, 256, 1, 0, 2, 26, 12, 8]
out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
out2 = out

print "\n\nConverting from base10 to base4"
ii = 0
for x in val:
    out[ii] = convertFromBase10(x, 4)
    print str(x) + " converts to " + str(out[ii])
    ii += 1

print "\n and back from base4 to base 10"
ii = 0
for x in out:
    out2[ii] = convert2Base10(x, 4)
    print str(x) + " converts to " + str(out2[ii])
    ii += 1