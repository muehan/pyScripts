# importing the requests library 
import requests 
import sys

URL = sys.argv[1]
print(f"see reponse from {URL}")

response = requests.get(URL)

def pretty_print_GET(response):
    print(f"-------------START-----------\n{response.method}\r\n{response.url}\r\n\r\n{response.conent}")
'''    '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()), '''

pretty_print_GET(response)

