# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files #################
# We provide two files for this assignment. One is a sample file where we give you 
# the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1272138.txt (There are 69 values and 
# the sum ends with 393)
# Data Format #################
# The file contains much of the text from the introduction of the textbook except that random 
# numbers are inserted throughout the text. 
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. 
# There can be any number of numbers in each line (including none).
# Handling The Data ############
# The basic outline of this problem is to read the file, look for integers 
# using the re.findall(), looking for a regular expression of '[0-9]+' and 
# then converting the extracted strings to integers and summing up the integers.

# import regular exp library
import re
import traceback
# create empty list to add numbers as Integer
uberlist = list()
fname = input("enter file name: ")
try:
    fhand = open(fname)
    for line in fhand:
        # get all the numbers on a line and add it to list
        numlist = re.findall('[0-9]+', line)
        lengthoflist = len(numlist)
        if (lengthoflist > 0):
            # convert to integer and add to a new list - uberlist
            for x in numlist:
                uberlist.append(int(x))            
        else:
            continue                     
except:
    traceback.print_exc()
    quit()
# sum all the numbers in the list
sumofnumbers = sum(uberlist)
print(sumofnumbers)
