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
    herJson = requests.get("https://www.lmsal.com/hek/her?cosec=2&cmd=search&type=column&event_type="+queryEvents+"&event_starttime="+ startTime +"&event_endtime="+ endTime +"&event_coordsys=UTC-HGS-TOPO&x1=-90&x2=90&y1=-90&y2=90&return=event_type,Event_Coord1,Event_Coord2,Area_Raw,Area_AtDiskCenter,FL_GOESCls")
    herJson = herJson.json()
    return herJson


def genorateEventList(data):
    events = data["result"]
    currentEvents = []
    for event in events:
        currentEvent = []
        currentEvent.append(event["event_type"])
        currentEvent.append(event["Event_Coord1"])
        currentEvent.append(event["Event_Coord2"])



    return currentEvents



def getHerData():
    herData  = []
    return herData

json = getHerJson()
print(genorateEventList(json))