import requests
import shutil

image_url = "https://www.justonecookbook.com/wp-content/uploads/2020/01/Sushi-Rolls-Maki-Sushi-%E2%80%93-Hosomaki-1106-II.jpg"
filename = image_url.split("/")[-1]
r = requests.get(image_url, stream = True)
r.raw.decode_content = True
with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
