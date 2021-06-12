fname = input("enter file name: ")
try:
    fhand = open(fname)
    for line in fhand:
        line = line.upper()
        print(line.rstrip())
except:
    print("File cannot be opened:", fname)
    quit()
