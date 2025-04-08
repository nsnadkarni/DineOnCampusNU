import json

# Update these with necessary stations
allisonBreakfast = ['Comfort 1', 'Comfort 2', 'Soup', 'Rooted 1', 'Flame 3', 'Bakery-Dessert']
allisonLunch = ['Comfort 1', 'Comfort 2', 'Soup', 'Rooted 1', 'Rooted 2', 'Pure Eats 1', 'Pure Eats 2', 'Flame 3', '500 Degrees 1', 'Bakery-Dessert']
allisonDinner = ['Comfort 1', 'Comfort 2', 'Soup', 'Rooted 1', 'Rooted 2', 'Pure Eats 1', 'Pure Eats 2', 'Flame 3', '500 Degrees 1', 'Bakery-Dessert']

sargentBreakfast = []
sargentLunch = []
sargentDinner = []

plexEastBreakfast = []
plexEastLunch = []
plexEastDinner = []

elderBreakfast = []
elderLunch = []
elderDinner = []

plexWestBreakfast = []
plexWestLunch = []
plexWestDinner = []

locations = [
    ('Allison Dining Commons', allisonBreakfast, allisonLunch, allisonDinner),
    ('Sargent Dining Commons', sargentBreakfast, sargentLunch, sargentDinner),
    ('Foster Walker Plex East', plexEastBreakfast, plexEastLunch, plexEastDinner),
    ('Elder Dining Commons', elderBreakfast, elderLunch, elderDinner),
    ('Foster Walker Plex West & Market', plexWestBreakfast, plexWestLunch, plexWestDinner),
]

meals = ['N/A', 'Breakfast', 'Lunch', 'Dinner']

def sanitizeData():
    file_path = 'PATH_TO_OUTPUT_FROM_capture_response'

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for location in data['locations']:
                locationsArrID = -1
                for x, locationPaired in enumerate(locations):
                    if location['name'] == locationPaired[0]:
                        locationsArrID = x
                for period in location.get('periods', [])[:5]:
                    if(locationsArrID == -1):
                        continue
                    periodArrID = (lambda: meals.index(period['name']))() if period['name'] in meals else -1
                    for station in period.get('stations', []):
                        if(periodArrID == -1):
                            continue

                        if station['name'] not in locations[locationsArrID][periodArrID]:
                            continue
                        print(f"\033[91mLocation {location['name']} -- Period {period['name']} -- Station {station['name']}\033[0m")
                        for item in station.get('items', []):
                            print(item['name'])

            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Invalid JSON format")

sanitizeData()
