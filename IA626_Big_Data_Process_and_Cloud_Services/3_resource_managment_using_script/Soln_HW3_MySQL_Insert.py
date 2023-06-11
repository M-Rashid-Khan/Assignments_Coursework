#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pymysql,csv,time,mysecrets
start = time.time()

conn = pymysql.connect(host=mysecrets.host, port=3306, user=mysecrets.user, passwd=mysecrets.passwd, db='ia626', autocommit=True)

cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute("DROP TABLE IF EXISTS `rashidm_pvsubset`;")

sql = '''
CREATE TABLE IF NOT EXISTS `rashidm_pvsubset` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `summons_number` int(5) NOT NULL,
  `plate_id` varchar(10) NOT NULL,
  `registration_state` varchar(10) NOT NULL,
  `issue_date` date NOT NULL,
  `violation_code` int(3) NOT NULL,
  `vehicle_body_type` varchar(5) NOT NULL,
  `vehicle_make` varchar(10) NOT NULL,
  `vehicle_expiration_date` date NOT NULL,
  `house_number` varchar(10) NOT NULL,
  `street_name` varchar(20) NOT NULL,
  `vehicle_color` varchar(10) NOT NULL,
  `vehicle_year` year(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
'''
cur.execute(sql)


# In[32]:


import pymysql,csv,time,mysecrets

conn = pymysql.connect(host=mysecrets.host, port=3306, user=mysecrets.user, passwd=mysecrets.passwd, db='ia626', autocommit=True)

cur = conn.cursor(pymysql.cursors.DictCursor)
import datetime
with open('pvsubset.csv') as f: 
    data = [{k:str(v) for k, v in row.items()}
           for row in csv.DictReader(f, skipinitialspace=True)]
sql = '''INSERT INTO `rashidm_pvsubset` (`summons_number`, `plate_id`, `registration_state`, `issue_date`,`violation_code`,
`vehicle_body_type`, `vehicle_make`, `vehicle_expiration_date`,`house_number`, `street_name`, `vehicle_color`, `vehicle_year`)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

n = 0
tokens = []
for row in data:
    datetime_str_id = row['Issue Date']
    datetime_obj = datetime.datetime.strptime(datetime_str_id,'%m/%d/%Y')
    new_datetime_str_id = datetime_obj.strftime("%Y-%m-%d")
    
    datetime_str_ed = row["Vehicle Expiration Date"]

    if len(datetime_str_ed) == 8:
        y = datetime_str_ed[0:4]
        ed = y
        ed+='-'
        m = datetime_str_ed[5:6]
        ed+=m
        ed+='-'
        d = datetime_str_ed[6:]
        if d == '88':
            ed+='28'
            datetime_str_ed = ed
        else: 
            ed+=d
            datetime_str_ed = ed
    else: 
        datetime_str_ed = None
    
    vehicle_y = row['Vehicle Year']
    if len(vehicle_y) == 4: 
        vy = vehicle_y
    else: 
        vy = None
        
    l = [row['Summons Number'], row["Plate ID"],row["Registration State"],new_datetime_str_id,row["Violation Code"],row["Vehicle Body Type"],
              row["Vehicle Make"],datetime_str_ed,row["House Number"],row["Street Name"],row["Vehicle Color"],vy]
#     print(l)
    tokens.append(l)
#     cur.execute(sql,tokens)
    n+=1
    if len(tokens) > 500:
        cur.executemany(sql,tokens)
        conn.commit()
        tokens = []
        print(n)
if len(tokens) > 0:
    cur.executemany(sql,tokens)
    conn.commit()
    
print("-----------------------------------------------------------------------\n")
print("Whole script took time 'For 500 Blocksize SQL Query': ", str(time.time() - start), '\n')
print("-----------------------------------------------------------------------")

