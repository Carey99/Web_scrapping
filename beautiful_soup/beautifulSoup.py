#!/usr/bin/python3
"""
    We use Beautiful soup to operate easily with html contents
    for instance Getting specific text from <div> or <p> tags
"""
import requests
from bs4 import BeautifulSoup

#let's make a GET request

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

#Optionally we can log to see if the request was successful
print(r)

#Now let's try Parsing some HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify()) #The prettiffy function when called, returns a Unicoded string

#Instead of printing, this time we shall wrrite it inside a file

try:
    with open('/home/queen/Web_scrapping/pettified.html', 'w', encoding='UTF-8') as f:
        f.write(soup.prettify())
        print('success') #Logging if it was saved
except Exception as e:
    print(e)