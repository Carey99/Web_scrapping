#!/usr/bin/python3

"""
    making a simple get request to a website
"""

import requests

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

print(r) #should return a 200 status code indicating success