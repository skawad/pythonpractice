#import module
#import traceback

fname = input("enter file name: ")
num = 0.0
count = 0.0

try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            pos = line.find('0')
            count = count + 1
            #print("count", count, " before num addition:", float(line[pos:]))                        
            num = float(line[pos:]) + num
            #print("after num addition:", num)
        else:
            continue                
except:
    print("File cannot be opened:", fname)
    #traceback.print_exc()
    quit()

print ("Average spam confidence:", num/count)