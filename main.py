#fb-info-parser
import json
from datetime import datetime
#https://matplotlib.org/users/installing.html

#count messages for each person
def countoneperson(filepath,fullname):
    with open(filepath, 'r') as f:
        jsondict = json.load(f)
    mw = 0
    other = 0
    for item in jsondict['messages']:
        if item['sender_name'] == fullname:
            other+=1
        if item['sender_name'] == 'Michael Woon':
            mw+=1
    otherpercent = (other*100)/float(mw+other)
    print "number of", fullname, "messages:", other
    print "number of Michael messages:", mw
    print otherpercent,"percent not michael"
    return

countoneperson('messages/tuan.json','Tuan Nguyen')

#https://docs.python.org/3/library/datetime.html
ts = int("1284101485")
date = datetime.utcfromtimestamp(ts)
print(date.month)
