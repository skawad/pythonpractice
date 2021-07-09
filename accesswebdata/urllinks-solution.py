# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

##### Following Links in Python #####
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
# We provide two files for this assignment. One is a sample file where we give you the name for your 
# testing and the other is the actual data you need to process for the assignment
#### Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. 
# Repeat this process 4 times. 
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
#### Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jamal.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: N
#### Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to
#  make it difficult for you to do the assignment without writing a Python program. But frankly with a 
# little effort and patience you can overcome these attempts to make it a little harder to complete 
# the assignment without writing a Python program. But that is not the point. 
# The point is to write a clever Python program to solve the program.

from typing import List
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

visitedList = list()
# number of URLs to open
todoList = list()
# which link position to follow in the opened URL
visitedList = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
todoList.append(url)
# gives number of times to loop through the process of opening the URL indicated by "position"
count = int(input('Enter count:'))
# position in list of URL to open and then read
position = int(input('Enter position:'))

while len(todoList) > 0 and count > 0:  
    print("====== To Retrieve:", count, "Queue Length:", len(todoList))
    url = todoList.pop()
    count = count - 1

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    soup = BeautifulSoup(html, 'html.parser')

     # Retrieve all of the anchor tags
    tags = soup('a')    
    # retrieve the position - subtract 1 in order to retrieve the correct position
    tag = tags.pop(position-1)
    url = tag.get('href', None)
    print('Contents:', tag.contents[0])
    todoList.append(url)


