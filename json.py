# importing the requests library 
import requests 
import sys

URL = sys.argv[1]
print(f"load json from {URL}")

response = requests.get(URL)
data = response.json() 

print(data)
