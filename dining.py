import httplib2
from bs4 import BeautifulSoup

class Station:

    NAME_MATRIX = {
        "Dessert": "Dessert Bar",
        "Pasta": "Pasta Station",
        "Pizza": "Pizza Station",
        "Salad": "Salad Bar",
        "Regional 1": "Regional Station 1",
        "Regional 2": "Regional Station 2",
        "Regional 3": "Regional Station 3",


        "Local - Deli": "Deli",
        "Local - Grill": "Grill",
        "Local - Pizza": "Pizza Station",
        "Local - Salad Bar": "Salad Bar",
        "Local - Smoothie (Aramark)": "Dessert Bar",
        "Mongolian": "Mongolian Station",
        "Saute": "Saute Station",
        "Soup": "Soup Station",
        "Taste of Home": "Taste of Home Station",
        "Vegetarian": "Vegetarian Station",
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
        "Regional 1": "regional1",
        "Regional 2": "regional2",
        "Regional 3": "regional3",
        "Theme Meal": "theme"


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

    def fnd_value(self, name):
        if name in Station.VALUE_MATRIX:
            return Station.VALUE_MATRIX[name.strip()]
        
        print("[WARN] Station with name \"{}\" cound not be found".format(name),
              "in VALUE_MATRIX. Has a new station been added?")

        return name.strip().casefold()

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

CORE          = "https://clemson.campusdish.com/LocationsAndMenus/FreshFoodCompany"
SCHILLETTER   = "https://clemson.campusdish.com/LocationsAndMenus/SchilletterDiningHall"
INFILE_CORE   = "lunch-core.html"
INFILE_SCH    = "lunch-schilletter.html"
INFILE_CLOSED = "closed-schilletter.html"

# Fetch and parse the webpage, either from the internet or locally if testing

ONLINE = True

if ONLINE: print("[INFO] The application is running in ONLINE mode.")
else: print("[WARN] The application is running in OFFLINE mode.")

def get_url(dining_hall):

    print("[INFO] Dining hall value is: {}".format(dining_hall))

    url = ""

    if dining_hall == "core":
        url = CORE if ONLINE else INFILE_CORE
    elif dining_hall == "schilletter":
        url = SCHILLETTER if ONLINE else INFILE_SCH
    
    if url == "": print ("[WARN] Could not get URL for dining hall!")
    else: print("[INFO] URL is:", url)

    return url

def fetch_page(url):
    
    print("[INFO] Fetching page at url:", url)

    try:
        # Check for HTTP in string, throws exception if not there
        url.index("http")

        http = httplib2.Http()
        status, response = http.request(url)

        print("[INFO] Fetching page from the web returned status code", status)

        return response
    except ValueError:
        # This catches the exception from .index()
        # This is expected to happen in OFFLINE mode since file urls don't
        #   contain https and we open the file from disk instead below.
        return open(url).read()

def is_open(input):
    print("[INFO] Attempting to detect if this dining location is open...")

    page = BeautifulSoup(input, features="lxml")

    status = page.select_one("div.location__status span").get_text() == "Open"

    if status: print("[INFO] Detected that this dining location is OPEN.")
    else: print("[INFO] Detected that this dining location is CLOSED.")

    return status

def parse_stations(input):

    print("[INFO] Parsing stations.")

    page = BeautifulSoup(input, features="lxml")

    print("[INFO] BS4 object was created.")

    stations_html = page.select("div.menu__station")
    print("[INFO] Found", len(stations_html), "station sections on the page.")

    stations = []

    for html in stations_html:
        
        name = html.select_one("h2.location-headers").get_text()

        items_html = html.select("div.menu__category a.viewItem")
        items = []

        for item in items_html:
            items.append(item.get_text())

        stations.append(Station(name, items))

        print("[INFO] Station \"{}\"".format(stations[len(stations)-1].name),
              "is serving", items)

    print("[INFO] Parsed", len(stations), "station(s).")

    return stations


## print out data for testing purposes

# stations = parse_stations(fetch_page(url))

# for station in stations:
#     print(station.speak())



