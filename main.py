#fb-info-parser
import json
from datetime import datetime

#opens file and turns json into dict
def getJson(filepath):
    with open(filepath, 'r') as f:
        jsondict = json.load(f)
    return jsondict
#returns dict of other persons messages
def getOther(jsondict):
    messagelist = []
    fullname = jsondict['participants'][0]['name']
    for item in jsondict['messages']:
        if item['sender_name'] == fullname:
            messagelist.append(item)
    return messagelist
#returns messages i sent
    messagelist = []
    for item in jsondict['messages']:
        if item['sender_name'] == 'Michael Woon':
            messagelist.append(item)
    return messagelist
#count messages for a person for all time
def countMessages(jsondict):
    fullname = jsondict['participants'][0]['name']
    other = 0
    for item in jsondict['messages']:
        if item['sender_name'] == fullname:
            other+=1
    return other
#count messages i sent to someone for all time
def countMW(jsondict):
    mw = 0
    for item in jsondict['messages']:
        if item['sender_name'] == 'Michael Woon':
            mw+=1
    return mw

def getPercentThem(mw,other):
    return other/float(mw+other)

#https://docs.python.org/3/library/datetime.html
#number of messages in a given month
def numInMonth(jsondict,monthInt):
    count = 0
    for item in jsondict['messages']:
        ts = int(item['timestamp_ms']/1000)
        date = datetime.fromtimestamp(ts)
        if date.month == monthInt:
            count+=1
    return count
#num on a specific weekday, monday is 0 sunday is 6
def numInWeekday(jsondict,weekdayInt):
    count = 0
    for item in jsondict['messages']:
        ts = int(item['timestamp_ms']/1000)
        date = datetime.fromtimestamp(ts)
        if date.weekday() == weekdayInt:
            count+=1
    return count

#https://docs.python.org/3/library/collections.html#collections.Counter
#for counting word frequency
def commonWords(jsondict):
    return

#testing
