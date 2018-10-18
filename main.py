#fb-info-parser
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def getJson(filepath,fullname):
    with open(filepath, 'r') as f:
        jsondict = json.load(f)
    return jsondict
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

#TODO
def numPerMonth(jsondict,monthInt):
    return

def numPerWeekday(jsondict,weekdayInt):
    return

#testing
dic = getJson('messages/tuan.json','Tuan Nguyen')
print(countMessages(dic))
print(countMW(dic))

#https://docs.python.org/3/library/datetime.html
ts = int("1284101485")
date = datetime.utcfromtimestamp(ts)
print(date.month)

#https://matplotlib.org/contents.html
x = np.arange(4)
money = [1, 2, 5.5, 3]
plt.bar(x, money)
plt.xticks(x, ('One', 'Two', 'Three', 'Four'))
#plt.show()
