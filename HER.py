import requests
import json

def getHerJson():
    startTime = "2022-09-29T00:00"
    endTime = "2022-10-01T00:00"
    queryEvents = "SS, FL"
    herJson = requests.get("https://www.lmsal.com/hek/her?cosec=2&cmd=search&type=column&event_type="+queryEvents+"&event_starttime="+ startTime +"&event_endtime="+ endTime +"&event_coordsys=helioprojective&x1=-1200&x2=1200&y1=-1200&y2=1200&return=event_type,Event_Coord1,Event_Coord2")
    herJson = herJson.json()
    return herJson

def genorateEventList(data):
    events = data[""]

print(getHerJson())