import requests
import time
import datetime

def getHerJson():
    epochTime = time.time()
    epochTimetakeDay = epochTime - 86400
    startTime = time.strftime("%Y-%m-%dT%H:%M", time.localtime(epochTimetakeDay))
    endTime = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
    print(endTime)
    print(startTime)
    queryEvents = "SS, FL"
    herJson = requests.get("https://www.lmsal.com/hek/her?cosec=2&cmd=search&type=column&event_type="+queryEvents+"&event_starttime="+ startTime +"&event_endtime="+ endTime +"&event_coordsys=helioprojective&x1=-1200&x2=1200&y1=-1200&y2=1200&return=event_type,Event_Coord1,Event_Coord2,Event_Coord3,Area_Raw,Area_AtDiskCenter,FL_GOESCls")
    herJson = herJson.json()
    print(herJson)
    return herJson

def getEventArea(event):
    if "area_raw" in event:
        return event["area_raw"]
    elif "area_atdiskcenter" in event:
        return event["area_atdiskcenter"]
    else:
        return None

def genorateEventList(data):
    events = data["result"]
    currentEvents = []
    for event in events:
        currentEvent = []
        currentEvent.append(event["event_type"])
        currentEvent.append(event["event_coord1"])
        currentEvent.append(event["event_coord2"])
        currentEvent.append(getEventArea(event))
        currentEvents.append(currentEvent)
        print(currentEvent)

    return currentEvents



def getHerData():
    herData  = []
    return herData

json = getHerJson()
genorateEventList(json)