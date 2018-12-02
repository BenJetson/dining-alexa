import httplib2
from bs4 import BeautifulSoup

class Station:

    NAME_MATRIX = {
        "Dessert": "Dessert Bar",
        "Pasta": "Pasta Station",
        "Pizza": "Pizza Station",
        "Salad": "Salad Bar",


        "Local - Deli": "Deli",
        "Local - Grill": "Grill",
        "Local - Pizza": "Pizza Station",
        "Local - Salad Bar": "Salad Bar",
        "Local - Smoothie (Aramark)": "Dessert Bar",
        "Mongolian": "Mongolian Station",
        "Saute": "Saute Station",
        "Soup": "Soup Station",
        "Taste of Home": "Taste of Home Station",
        "Vegetarian": "Vegetarian Station"
    }

    VALUE_MATRIX = {
        "Deli": "deli",
        "Dessert": "dessert",
        "Entree Station": "entree",
        "Grill": "grill",
        "Lite-sy Corner": "litesy",
        "Mongolian Grill": "mongolian",
        "Pasta": "pasta",
        "Pizza": "pizza",
        "Salad": "salad",


        "Fresh Focus": "freshfocus",
        "Local - Deli": "deli",
        "Local - Grill": "grill",
        "Local - Pizza": "pizza",
        "Local - Salad Bar": "salad",
        "Local - Smoothie (Aramark)": "dessert",
        "Mongolian": "mongolian",
        "Saute": "saute",
        "Soup": "soup",
        "Taste of Home": "tasteofhome",
        "Vegetarian": "vegetarian"
    }

    def __init__(self, name, items):
        self.name = self.fix_name(name)
        self.value = Station.VALUE_MATRIX[name.strip()]
        self.items = items

    def fix_name(self, name):
        if name in Station.NAME_MATRIX:
            return Station.NAME_MATRIX[name.strip()]
        
        return name
        

    def speak(self):

        if self.value == "salad" or self.value == "deli":
            return "the {} is available per usual... ".format(self.name)

        output = "the {} is serving ".format(self.name)

        for i in range(0, len(self.items)):
            output += self.items[i]

            if (len(self.items) == 2 and i == 0):
                output += " and "
            elif (i == len(self.items) - 2):
                output += ", and "
            elif (i != len(self.items) - 1):
                output += ", "
        
        output += "... "

        return output

# Static messages
BANNER = "Hi! I can help you find out what's on the menu at campus dining halls."

# {1} dining hall name
CLOSED =  "Sorry, {} dining does not have a menu posted right now. "
CLOSED += "This location may currently be closed."

# {1} station name
STATION_NO_MATCH = "Sorry, I couldn't find a station that matches the name {}"

# URLs for Menus   

CORE        = "https://clemson.campusdish.com/LocationsAndMenus/FreshFoodCompany"
SCHILLETTER = "https://clemson.campusdish.com/LocationsAndMenus/SchilletterDiningHall"
INFILE_CORE = "lunch.html"
INFILE_SCH  = "sch-lunch.html"

# Fetch and parse the webpage, either from the internet or locally if testing

ONLINE = True

if ONLINE: print("[INFO] The application is running in ONLINE mode.")
else: print("[WARN] The application is running in OFFLINE mode.")

def fetch_page(url):
    
    try:
        # Check for HTTP in string, throws exception if not there
        url.index("http")

        http = httplib2.Http()
        status, response = http.request(url)
        return response
    except ValueError:
        # This catches the exception from .index()
        # Usually this happens because in OFFLINE mode
        #   and we open the file from disk instead below.
        return open(url)

def is_open(input):
    page = BeautifulSoup(input, features="lxml")

    status = page.select_one("div.location__status span").get_text()

    return status.casefold() == "Open".casefold()

def parse_stations(input):

    page = BeautifulSoup(input, features="lxml")

    stations_html = page.select("div.menu__station")
    stations = []

    for html in stations_html:
        
        name = html.select_one("h2.location-headers").get_text()

        items_html = html.select("div.menu__category a.viewItem")
        items = []

        for item in items_html:
            items.append(item.get_text())
            
        stations.append(Station(name, items))

    return stations


## print out data for testing purposes

# stations = parse_stations(fetch_page(url))

# for station in stations:
#     print(station.speak())



