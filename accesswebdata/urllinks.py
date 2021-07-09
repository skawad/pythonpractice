# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from typing import List
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

uberlist = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #print('TAG:',tag)
    #print('Contents:',tag.contents[0])
    # get the content of "span" tag and extract the number within the tag
    uberlist.append(int(tag.contents[0]))

#sum all the number in the list  
print(sum(uberlist))
