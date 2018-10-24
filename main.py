#fb-info-parser
# -*- coding: utf-8 -*-
import json
from datetime import datetime
from collections import Counter
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
    final = { 'messages' : messagelist }
    return final
#returns messages i sent
    messagelist = []
    for item in jsondict['messages']:
        if item['sender_name'] == 'Michael Woon':
            messagelist.append(item)
    final = { 'messages' : messagelist }
    return final
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

#num on each hour, range(24)
def numInHour(jsondict,hourInt):
    count = 0
    for item in jsondict['messages']:
        ts = int(item['timestamp_ms']/1000)
        date = datetime.fromtimestamp(ts)
        if date.hour == hourInt:
            count+=1
    return count

#num on each day, returns list of all day counts
#needs editing to insert zeros for missed days
#make into dictionary where keys are dates
def allDays(jsondict):
    days = []
    days.append(0)
    first = jsondict['messages'][0]
    ts = int(first['timestamp_ms']/1000)
    date = datetime.fromtimestamp(ts)
    current = date.day
    for item in jsondict['messages']:
        ts = int(item['timestamp_ms']/1000)
        date = datetime.fromtimestamp(ts)
        if date.day == current:
            days[-1] += 1
        else:
            days.append(1)
        current = date.day
    return days

#returns number of messages on each month/year, dict
#add handling for dates with zero
def monthYear(jsondict):
    dates = {}
    for item in jsondict['messages']:
        ts = int(item['timestamp_ms']/1000)
        date = datetime.fromtimestamp(ts)
        month = str(date.month)
        yr = str(date.year)
        datestr = month + "-" + yr
        if datestr in dates:
            dates[datestr] += 1
        else:
            dates[datestr] = 1
    return dates

# dic = getJson('messages/div.json')
# print(monthYear(dic))

#https://docs.python.org/3/library/collections.html#collections.Counter
#for counting word frequency
def messageString(jsondict):
    allmessages = ''
    for item in jsondict['messages']:
        if 'content' in item:
            s = item['content'].encode(sys.stdout.encoding, errors='replace')
            s = s.lower()
            allmessages += s
            allmessages += ' '
    stop_words = set(stopwords.words('english'))
    stop_words.add('u')
    stop_words.add('like')
    stop_words.add('get')
    stop_words.add('im')
    stop_words.add("i'm")
    stop_words.add("lol")
    stop_words.add("lmao")
    stop_words.add("ur")
    stop_words.add("oh")
    word_tokens = allmessages.split()
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def commonWords(wordlist):
    commons = Counter(wordlist).most_common(20)
    return commons

# fix monYr and alldays
# day with most - similar to alldays
# week/year
# multiple graphs in one
# https://www.nltk.org/
