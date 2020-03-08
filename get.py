# importing the requests library 
import requests 
import sys

print('http get to')
print(sys.argv[1])

URL = sys.argv[1]

response = requests.get(url = URL)
data = response.json() 

print(data)