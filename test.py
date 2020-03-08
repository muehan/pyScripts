# importing the requests library 
import requests 

print('hello welt')

URL = "https://api.predic8.de/shop/products/"

response = requests.get(url = URL)
data = response.json() 

print(data)