#fb-info-parser
import matplotlib.pyplot as plt
import numpy as np
from main import *


## TODO: make each one have a bar for me and for them
#graph of ratio me vs them (bar)
def makeRatio(filepath):
    jsondict = getJson(filepath)
    other = countMessages(jsondict)
    mw = countMW(jsondict)
    percentthem = getPercentThem(mw,other)
    mwpercent = 100-percentthem
    labels = jsondict['participants'][0]['name'],'Michael Woon'
    vals = [other,mw]
    plt.pie(vals,  labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
    title = 'Total Messages: ' + str(other+mw)
    plt.title(title)
    plt.axis('equal')
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
    return

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
    return

#graph all days, count from each day
#somehow show day with most
def makeAllDays(filepath):
    jsondict = getJson(filepath)
    days = allDays(jsondict)
    vals = days.values()
    keys = days.keys()
    ind = np.arange(len(vals))
    plt.bar(ind,vals,color='SkyBlue')
    plt.xlabel('Number of days')
    plt.title('Messages on each day')
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
    return

#make all plots at once
#TODO change window title
def allPlots(filepath):
    plt.subplot(1,2,1)
    makeRatio(filepath)
    plt.subplot(1,2,2)
    makeMonyr(filepath)
    plt.show()
    plt.subplot(1,2,1)
    makeWeekday(filepath)
    plt.subplot(1,2,2)
    makeHours(filepath)
    plt.show()
    plt.subplot(1,1,1)
    makeAllDays(filepath)
    plt.show()
    plt.subplot(1,1,1)
    makeWords(filepath) #keeps showing on new page
    plt.show()
    return

allPlots('messages/hn.json')
