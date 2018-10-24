#fb-info-parser
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
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind, (jsondict['participants'][0]['name'],'Michael Woon'))
    plt.title('Total messages per person')
    plt.show()
    return
#graph of weekdays (bar)
def makeWeekday(filepath):
    jsondict = getJson(filepath)
    vals = []
    for i in range(0,7):
        vals.append(numInWeekday(jsondict,i))
    ind = np.arange(len(vals))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind,('Mon','Tues','Wed','Thurs','Fri','Sat','Sun'))
    plt.title('Number of messages per weekday')
    plt.show()
    return
#graph of months (bar)
def makeMonth(filepath):
    jsondict = getJson(filepath)
    vals = []
    for i in range(1,13):
        vals.append(numInMonth(jsondict,i))
    ind = np.arange(len(vals))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind,('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
    plt.title('Number of messages on each weekday')
    plt.show()
    return

#months with years
#TODO figure out how to order dic keys
def makeMonyr(filepath):
    jsondict = getJson(filepath)
    dates = monthYear(jsondict)
    vals = dates.values()
    keys = dates.keys()
    ind = np.arange(len(vals))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind,keys,rotation='vertical')
    plt.title('Messages on each month')
    plt.show()
    return
makeMonyr('messages/div.json')


#graph of hours (bar)
def makeHours(filepath):
    jsondict = getJson(filepath)
    vals = []
    for i in range(24):
        vals.append(numInHour(jsondict,i))
    ind = np.arange(len(vals))
    hours = list(range(24))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind,hours)
    plt.title('Number of messages in each hour')
    plt.show()
    return

#graph all days, count from each day
def makeAllDays(filepath):
    jsondict = getJson(filepath)
    days = allDays(jsondict)
    ind = np.arange(len(days))
    plt.bar(ind,days,color='SkyBlue')
    plt.title('Messages on every day')
    plt.show()
    return

#word freq (bar)
def makeWords(filepath):
    jsondict = getJson(filepath)
    str = messageString(jsondict)
    commons = commonWords(str)
    vals = []
    words = []
    for tup in commons:
        vals.append(tup[1])
        words.append(tup[0])
    ind = np.arange(len(vals))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xticks(ind,words)
    plt.title('Most common words')
    plt.show()
    return
