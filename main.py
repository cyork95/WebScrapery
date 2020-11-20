from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
#print(soup.prettify())

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})
for item in links:
    itemText = item.find("a").text
    itemHref = item.find("a").attrs["href"]
    if itemText and itemHref:

        #directional navigation
        print("Site:", itemText, itemHref)
        print("Parent:", item.find("a").parent)
        print("Summary:", item.find("a").parent.parent.find("p").text)
        children = item.children
        childrenH2 = item.find("h2")
        for child in children:
            print("Child:", child)
            print("Next sibling of the h2:", childrenH2)