#fb-info-parser
import json
import matplotlib.pyplot as plt
import numpy as np
from main import *


#https://matplotlib.org/contents.html
x = np.arange(4)
money = [1, 2, 5.5, 3]
plt.bar(x, money)
plt.xticks(x, ('One', 'Two', 'Three', 'Four'))
#plt.show()

## TODO: make each one have a bar for me and for them
#graph of ratio me vs them (bar)
def makeRatio(filepath):
    jsondict = getJson(filepath)
    other = countMessages(jsondict)
    mw = countMW(jsondict)
    vals = [other,mw]
    ind = np.arange(len(vals))
    plt.bar(ind,vals)
    plt.xticks(ind, (jsondict['participants'][0]['name'],'Michael Woon'))
    plt.set_title('Total messages per person')
    plt.show()
    return
#graph of weekdays (bar)
def makeWeekday(filepath):
    jsondict = getJson(filepath)
    vals = []
    for i in range(0,7):
        vals.append(numInWeekday(jsondict,i))
    ind = np.arange(len(vals))
    plt.bar(ind,vals)
    plt.xticks(ind,('Mon','Tues','Wed','Thurs','Fri','Sat','Sun'))
    plt.set_title('Number of messages per weekday')
    plt.show()
    return
#graph of months (bar)
def makeMonth(filepath):
    jsondict = getJson(filepath)
    vals = []
    for i in range(1,13):
        vals.append(numInMonth(jsondict,i))
    ind = np.arange(len(vals))
    plt.bar(ind,vals)
    plt.xticks(ind,('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
    plt.set_title('Number of messages per month')
    plt.show()
    return
makeMonth('messages/div.json')

#word freq (bar)
