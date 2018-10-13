import urllib
from bs4 import BeautifulSoup

class Station:

    def __init__(self, name, items):
        self.name = name
        self.items = items

with open("lunch.html") as webpage:
    page = BeautifulSoup(webpage, features="lxml")


stations_html = page.select("div.menu__station")
stations = []


for i in range(0, len(stations_html)):
    
    html = stations_html[i]

    name = html.select_one("h2.location-headers").get_text()

    items_html = html.select("div.menu__category a.viewItem")
    items = []

    for item in items_html:
        items.append(item.get_text())
        
    stations.append(Station(name, items))

## print out data
for station in stations:
    print("\n---- Station {} ----".format(station.name))
    for item in station.items:
        print(" + ", item)

