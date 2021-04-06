import requests          # pip install requests
from PIL import Image    # pip install pillow

url = "http://bit.ly/2JnsHnT"
myResponse = requests.get(url, stream=True)
print(myResponse.status_code)
rawImage = myResponse.raw

img = Image.open(rawImage)
img.show()
img.save("d:\sda1\src.png")
print(img.get_format_mimetype)