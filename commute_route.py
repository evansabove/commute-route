import requests
import json
from datetime import datetime, timezone, timedelta

now = (datetime.now(timezone.utc) + timedelta(0, 0, 0, 0, 2)).isoformat()

request = {
  "origin":{
    "address": "34 Cockshutt Road, Sheffield"
  },
  "destination":{
    "address": "73 Sidney Street, Sheffield"
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

response = requests.post('https://routes.googleapis.com/directions/v2:computeRoutes', json.dumps(request), headers= { 'X-Goog-Api-Key': 'AIzaSyBaBnV3R7UQ_xeZUnWE4nH6Bt0g1l5uCXI', 'X-Goog-FieldMask': 'routes.description,routes.duration', 'Content-Type': 'application/json'})

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

print(f'Use {transformDescription(shortest_route['description'])} - {getMinutesFromSecondsSetting(shortest_route['duration'])} mins')