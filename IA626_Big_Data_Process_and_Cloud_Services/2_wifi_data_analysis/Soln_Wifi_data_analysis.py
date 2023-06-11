#!/usr/bin/env python
# coding: utf-8

# In[100]:


#The following code reads csv data from test.csv into memory as a list of #dictionaries called ‘data’ . Example:
#[{'col2': 2, 'col3': 3, 'col1': 1}, {'col2': 5, 'col3': 6, 'col1': 4}]
import csv
with open('wifi_list.csv') as f:
    data = [{k: str(v) for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]


# In[101]:


dlist = []
for row in data:
    if 'cph' in row['SSID'].lower():
        dlist.append(row)
shist = {}
#dlist[0]['MAC'][0:8]

for row in dlist:
    mac = row['MAC'][0:8]
#     print(mac)
    if mac in shist:
        shist[mac] +=1
    else:
        shist[mac] = 1

#print(shist)

s = "mac manufacturer | count\n"
s += "------------------------------\n"
# print(s)
for manufacturer,count in shist.items():
    #print(f"{manufacturer} | {count}")
    s+= f"{manufacturer}         |    {count}\n"
print(s)


# In[102]:


#For Channel List distint
# print(s)
# print(data[0]['Channel'])
chList = []
for row in data:
#     print(row)
    ch = row["Channel"]
    if ch in chList:
        pass
    else: 
        chList.append(ch)
# print(chList)


# In[79]:


#For Mac Address list distint
# macList = []
# macList2 = []
# for row in data:
#     mac = row["MAC"][0:8]
#     if mac in macList:
#         pass
#     else:
#         macList.append(mac)
#         macList2.append(row['MAC'])
#print(len(macList2), macList2)
#total 253 different mac addressess connected


# In[104]:


# mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
# myset = set(mylist)
# print(myset)


# In[124]:


ch_ip_c = {}
for ch in chList:
    ch_ip = []
    for row in data:
        chn = row['Channel']
        ip = row["MAC"]
        if chn == ch :
            ch_ip.append(ip)
        else:
            pass
    #print(ch_ip)
    ch_ip = set(ch_ip)
    #print(ch_ip)
    ch_ip_c[ch] = len(ch_ip)
    #print(ch_ip_c)
#print(ch_ip_c)

from collections import OrderedDict
ch_ip_c = OrderedDict(sorted(ch_ip_c.items()))
#print(ch_ip_c)
ch_keys = ch_ip_c.keys()
#print(ch_keys)

s= 'Channel # | Count of distint MAC Addresses\n'
s+="......................................\n"
for key,value in ch_ip_c.items():
    s+=f"{key}        |    {value}\n"
print(s)


# In[123]:





# In[116]:


# def _compare_keys(x, y):
#     try:
#         x = int(x)
#     except ValueError:
#         xint = False
#     else:
#         xint = True
#     try:
#         y = int(y)
#     except ValueError:
#         if xint:
#             return -1
#         return cmp(x.lower(), y.lower())
#         # or cmp(x, y) if you want case sensitivity.
#     else:
#         if xint:
#             return cmp(x, y)
#         return 1


# In[117]:


# print(ch_ip_c)
# for k in sorted(ch_ip_c, cmp=_compare_keys):
#     print(k, ch_ip_c[k]) # or whatever.


# In[106]:


# chList.pop(0)
# print(chList)
# print(data[15])


# In[107]:


# s= 'Channel Number | Count of MAC Addresses\n'
# ChCount = {}
# for key in chList:
#     ChCount[key] = {}
# print(ChCount)


# In[108]:


# for row in data: 
#     ch = row["Channel"]
#     ip = row["MAC"]
#     #print(ch,ip)
#     print(ChCount[ch])
#     if ChCount.has_key(ch):
#         print(ip)
#         ChCount[ch]= [ChCount[ch],ip]
#     else:
#         break
#         print('Breakked')
#         break
#         ChCount[ch] = None
#         print(ChCount[ch])
#         print(ip)
#         ChCount[ch]= [ChCount[ch],ip]
#     print(ChCount)
#     break

#print(ChCount)

