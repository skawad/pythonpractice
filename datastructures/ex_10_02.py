# Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull the hour 
# out from the 'From ' line by finding the time and then splitting the 
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
# In the above line, find "09"
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below..
# Desired output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
fname = input("enter file name: ")
# create empty dictionary
counts = dict()
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith("From "):
            temp_list = line.split()
            # following line gives the time as follows: 09:14:16
            time_value = temp_list[5]
            #print(time_value)
            # next step is to split the line using colon and extract the hour ex: 09
            time_value_hour_list = time_value.split(":")
            time_value_hour = time_value_hour_list[0]
            #add hour and count of hour to dictionary
            counts[time_value_hour] = counts.get(time_value_hour,0) + 1            
        else:
            continue                
except:
    print("File cannot be opened:", fname)
    quit()

# this converts dictionary "counts" and creates tuples and then sorts them 
counts = sorted(counts.items())
# then print key value pairsof counts
for (k,v) in counts:
    print(k, v)


