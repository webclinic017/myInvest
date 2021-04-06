import requests          # pip install requests

url = "http://bit.ly/2JnsHnT"
# url = "http://aron-tr.com/imgs/ShirohigeFalls.png"
myResponse = requests.get(url, stream=True)
print(myResponse.status_code)
print(myResponse.raw)
