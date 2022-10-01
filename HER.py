import requests
import json

def getHerJson():
    startTime = "2022-09-29T00:00"
    endTime = "2022-10-01T00:00"
    herJson = requests.get("https://www.lmsal.com/hek/her?cosec=2&cmd=search&type=column&event_type=**&event_starttime="+ startTime +"&event_endtime="+ endTime +"&event_coordsys=helioprojective&x1=-1200&x2=1200&y1=-1200&y2=1200")
    

getHerJson()