import requests
import json
from datetime import datetime, timezone, timedelta
import secrets
import screen_writer

now = (datetime.now(timezone.utc) + timedelta(0, 0, 0, 0, 2)).isoformat()

request = {
  "origin":{
    "address": secrets.route_from
  },
  "destination":{
    "address": secrets.route_to
  },
  "travelMode": "DRIVE",
  "routingPreference": "TRAFFIC_AWARE",
  "departureTime": now,
  "computeAlternativeRoutes": "true",
  "routeModifiers": {
    "avoidTolls": "false",
    "avoidHighways": "false",
    "avoidFerries": "false"
  },
  "languageCode": "en-GB",
  "units": "IMPERIAL"
}

response = requests.post('https://routes.googleapis.com/directions/v2:computeRoutes', json.dumps(request), headers= { 'X-Goog-Api-Key': secrets.api_key, 'X-Goog-FieldMask': 'routes.description,routes.duration', 'Content-Type': 'application/json'})

routes = response.json()

def getMinutesFromSecondsSetting(str):
    seconds = int(str.strip('s')) / 60
    return round(seconds)

def transformDescription(description):
    match description:
        case "A61": return "Woodseats / Chesterfield Road"
        case "Abbeydale Rd/A621": return "Abbeydale Road / London Road"
        case "Abbey Ln/B6068": return "Abbey Lane / Ecclesall Road"
        case _: return description

shortest_route = min(routes['routes'], key=lambda x: x['duration'])

str = f'Use {transformDescription(shortest_route['description'])} - {getMinutesFromSecondsSetting(shortest_route['duration'])} mins'
print(str)

writer = screen_writer.ScreenWriter()
writer.show_route(str)