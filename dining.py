import httplib2
from bs4 import BeautifulSoup

class Station:

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def speak(self):

        output = "Today, the {} is serving ".format(self.name)

        for i in range(0, len(self.items)):
            output += self.items[i]

            if (i != len(self.items) - 1):
                output += ", "
        
        return output

        

CORE = "https://clemson.campusdish.com/LocationsAndMenus/FreshFoodCompany"

web = False

page = None

if web:
    http = httplib2.Http()
    status, response = http.request(CORE)

    page = BeautifulSoup(response, features="lxml")
else:
    with open("lunch.html") as response:
        page = BeautifulSoup(response, features="lxml")


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

## print out data for testing purposes
for station in stations:
    print(station.speak())



