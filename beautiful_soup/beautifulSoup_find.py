#!/usr/bin/python3
"""
    Extract useful content inside some div class
"""
import requests
from bs4 import BeautifulSoup

#Make a request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

#lets parse the html
soup = BeautifulSoup(r.content, 'html.parser')

#let's find some content inside a  div class
s = soup.find('div', class_='entry-content')
content = soup.find_all('p')

#Let's write that content inside some file


try:
    with open('/home/queen/Web_scrapping/ps.html', 'w', encoding='UTF-8') as f:
        for paragraph in content:
            f.write(str(paragraph)) #Since content is a Resultset, it wont be automatically be written into a file a f.write() expects a string
            f.write('\n')
        print('success') #log to indicate success
except Exception as e:
    print(e)