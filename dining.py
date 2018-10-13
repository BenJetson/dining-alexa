import httplib2
from bs4 import BeautifulSoup

class Station:

    NAME_MATRIX = {
        "Dessert": "Dessert Bar",
        "Pasta": "Pasta Station",
        "Pizza": "Pizza Station",
        "Salad": "Salad Bar",
        "Soup": "Soup Station"
    }

    def __init__(self, name, items):
        self.name = self.fix_name(name)
        self.items = items

    def fix_name(self, name):
        if name in Station.NAME_MATRIX:
            return Station.NAME_MATRIX[name]
        
        return name
        

    def speak(self):

        output = "Today, the {} is serving ".format(self.name)

        for i in range(0, len(self.items)):
            output += self.items[i]

            if (len(self.items) == 2 and i == 0):
                output += " and "
            elif (i == len(self.items) - 2):
                output += ", and "
            elif (i != len(self.items) - 1):
                output += ", "
        
        output += "."

        return output

# URLs for Menus   

CORE        = "https://clemson.campusdish.com/LocationsAndMenus/FreshFoodCompany"
SCHILLETTER = "https://clemson.campusdish.com/LocationsAndMenus/SchilletterDiningHall"

# Fetch and parse the webpage, either from the internet or locally if testing

web = False

page = None

if web:
    http = httplib2.Http()
    status, response = http.request(CORE)

    page = BeautifulSoup(response, features="lxml")
else:
    with open("lunch.html") as response:
        page = BeautifulSoup(response, features="lxml")


# Create Station objects

stations_html = page.select("div.menu__station")
stations = []


for html in stations_html:
    
    name = html.select_one("h2.location-headers").get_text()

    items_html = html.select("div.menu__category a.viewItem")
    items = []

    for item in items_html:
        items.append(item.get_text())
        
    stations.append(Station(name, items))

## print out data for testing purposes

for station in stations:
    print(station.speak())



