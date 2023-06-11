#!/usr/bin/env python
# coding: utf-8

# In[40]:


import datetime
f = open('access_subset.log', 'r')
s = f.read()
f.close()
lines = s.split("\n")
#print(lines)
#print(type(lines))
n = 0 
for line in lines:
    #print(line)
    cols = line.split(" ")
    #print(cols)
    ip = cols[0]
    dts = cols[3].replace("[","")
    dto = datetime.datetime.strptime(dts,"%d/%b/%Y:%H:%M:%S")
    utc = cols[4].replace(']',"")
    htp_error = cols[8]
    print(ip,dto.year,dto.month,dto.day,dto.hour,dto.minute,dto.second)
    print(utc)
    print(htp_error)
    
    
    
#     n+=1
#     if n > 10:
#         break


# In[26]:


# import datetime
# dts = "19/Aug/2015:10:13:23"
# dto = datetime.datetime.strptime(dts,"%d/%b/%Y:%H:%M:%S")
# print(dto.day)


# In[28]:


# import datetime
# dts = "19/Augu/2015:10:13:23"
# dto = None
# try:
#     dto = datetime.datetime.strptime(dts,"%d/%b/%Y:%H:%M:%S")
# except Exception as e:
#     print(e)
    
# if dto is not None:
#     print("Date is ", dto)
# else:
#     print("Datetime not converted")

