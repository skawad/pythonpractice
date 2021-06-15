# Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines 
# as the person who sent the mail. The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("enter file name: ")
# create empty dictionary
counts = dict()
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith("From "):
            temp_list = line.split()
            email = temp_list[1]
            #add email and count of email to dictionary
            counts[email] = counts.get(email,0) + 1            
        else:
            continue                
except:
    print("File cannot be opened:", fname)
    quit()
# find the email with the highest number in the dictionary
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)



