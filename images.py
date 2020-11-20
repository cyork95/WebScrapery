from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("Enter image search term:")
    params = {"q": search}
    dirName = search.replace(" ", "_").lower()
    if not os.path.isdir(dirName):
        os.makedirs(dirName)
    r = requests.get("https://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    for item in links:
        try:
            imageUrl = requests.get(item.attrs["href"])
            print("Getting:", item.attrs["href"] )
            title = item.attrs["href"].split("/")[-1]
            try:
                image = Image.open(BytesIO(imageUrl.content))
                image.save("./" + dirName + "/" + title, image.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request image.")
    StartSearch()

StartSearch()