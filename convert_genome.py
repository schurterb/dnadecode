#Created by: Brandon Schurter
#Last updated: Feb 24, 2017

#Purpose: Use geneTranslator and baseConversion to convert DNA files into 
#       base-4 equivelents and then into base-10 equivelents for statistical 
#       analysis and interpretation

from baseConversion import convert
from geneTranslator import readNtranslate

#DNA data files to process
datafolder = "/home/ubuntu/workspace/DNAdecode/data/"
outputfolder = "/home/ubuntu/workspace/DNAdecode/output/"
input_files = ["5'LacZ.1", "5'LacZ.2", "Car20ZT.2"]
skip_count = 3

for input_file in input_files:
    #Read the DNA sequence into an array, tranlating it to base-4, and grouping 
    # the characters according to skip_count
    input_file_name = datafolder + input_file + ".txt"
    DNA_vals = readNtranslate(input_file_name, skip_count)
    DNA_vals_1 = DNA_vals[0::]
    DNA_vals_2 = DNA_vals_1[1::]
    DNA_vals_2.append(DNA_vals_1[0])
    DNA_vals_3 = DNA_vals_2[1::]
    DNA_vals_3.append(DNA_vals_2[0])
    
    print "Data read & translated"
    
    output_vals_1 = DNA_vals_1
    output_vals_2 = DNA_vals_2
    output_vals_3 = DNA_vals_3
    for i in range(0, len(DNA_vals)):
        DNA_vals_1[i] = convert(DNA_vals_1[i], 4, 10) #Iterate through each element in DNA_vals, converting it to a base-10 number
        DNA_vals_2[i] = convert(DNA_vals_2[i], 4, 10) #Iterate through each element in DNA_vals, converting it to a base-10 number
        DNA_vals_3[i] = convert(DNA_vals_3[i], 4, 10) #Iterate through each element in DNA_vals, converting it to a base-10 number
    print "Data converted to base10"
          
    output_file_name_1 = outputfolder + input_file + "_output_1.txt"  #Create the filename to which to write the results of 1st conversion
    output_file_1 = open(output_file_name_1, 'w')     #Open said files
    for x in DNA_vals_1:  
        output_file_1.write(str(x) + ",")    #Write each element in the array to the output file
    output_file_1.close()                                 #Close the output file
    
    output_file_name_2 =  outputfolder + input_file + "_output_2.txt"  #Create the filename to which to write the results of 1st conversion
    output_file_2 = open(output_file_name_2, 'w')     #Open said files
    for x in DNA_vals_2:  
        output_file_2.write(str(x) + ",")    #Write each element in the array to the output file
    output_file_2.close()                                 #Close the output file
    
    output_file_name_3 = outputfolder + input_file + "_output_3.txt"  #Create the filename to which to write the results of 1st conversion
    output_file_3 = open(output_file_name_3, 'w')     #Open said files
    for x in DNA_vals_3:  
        output_file_3.write(str(x) + ",")    #Write each element in the array to the output file
    output_file_3.close()                                 #Close the output file
    print "Data printed to files"
        
        