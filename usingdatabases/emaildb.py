import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    #split the line that starts with From:
    pieces = line.split()
    #print(pieces)
    # the second item in the list gives the email address
    email = pieces[1]
    #print("email", email)
    # split the email address so we can get the org ex: iupui.edu
    org = email.split("@")
    #print("org", org[1])
    #check to see if org found in db by extracting second item in org list 
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[1],))
    row = cur.fetchone()
    #if row not found, insert into db, else update count
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org[1],))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org[1],))

#commit records to db   
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
