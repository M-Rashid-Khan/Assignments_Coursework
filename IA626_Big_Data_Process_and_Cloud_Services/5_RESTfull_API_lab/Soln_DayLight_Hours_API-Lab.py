#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, json
from datetime import datetime

def getDayLight(z):
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={z},us&appid=a6962678a5cba51e8db12b46bc87a867'
    r = requests.get(url)
    data =json.loads(r.text)
    d = {}
    #print(data['sys']['sunrise'])
    if str(data['cod']) == '200':
            d["status"] = 'ok'
            d["rise"] = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            d["set"] = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            d["riseunix"] = data['sys']['sunrise']
            d["setunix"] = data['sys']['sunset']
    else:
        d["status"] = 'error'
        d["rise"] = None
        d["set"] = None
        d["riseunix"] = None
        d["setunix"] = None
#         print('error')
#             d['msg'] = 'Invalid response'
#             d['apimsg'] = data['message']
    return d


# In[2]:


import csv    
with open('ziplist.csv', 'r') as f: 
    reader = csv.reader(f)
    z_l = []
    for i,line in enumerate(reader):
        if i > 0:
            z = int(line[0]) 
            z_l.append(z)
            


# In[3]:


list_dict = []
for z in z_l:
    line = {}
    t = getDayLight(z)
    line["zip"] = z
    line["start"] = t["rise"]
    line["end"] = t["set"]
    list_dict.append(line)
    #print(list_dict)
    line ={}


# In[4]:


fields = ['zip', 'start', 'end'] 
    
# name of csv file 
filename = "ziplist_2.csv"
    
# writing to csv file 
with open(filename, 'w', newline = '') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
    writer.writeheader()
    writer.writerows(list_dict)
print("Done, File name: ziplist_2 for results!!!")

