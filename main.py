#fb-info-parser
import json
#https://matplotlib.org/users/installing.html

with open('messages\hle.json', 'r') as f:
    jsondict = json.load(f)

#count messages for each person
mw = 0
hl = 0
for item in jsondict['messages']:
    if item['sender_name'] == 'Hayden Le':
        hl+=1
    if item['sender_name'] == 'Michael Woon':
        mw+=1
print(hl)
print(mw)
