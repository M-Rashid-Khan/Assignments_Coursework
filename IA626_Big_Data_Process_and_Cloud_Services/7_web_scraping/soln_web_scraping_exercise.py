#!/usr/bin/env python
# coding: utf-8

# In[140]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

team = {'brnm':'Brown','clkm':'Clarkson','clgm':'Colgate', 'corm':"Cornel",'darm':"Dartmouth",'harm':"Harvard",'prnm':"Princeton",'quip':"Quinnipiac",'renm':"Rensselaer",'stlm':"St.Lawrence",'unim':"Union",'yalm':"Yale"}

for key,value in team.items():
    try: 
        url = f'http://www.collegehockeystats.net/1920/teamstats/{key}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'html.parser')
        table1 = soup.find('table', class_='chssmallreg')
        df = pd.DataFrame(columns=['PlayerNo','GP','A','PName', 'G'])
        n = 0
        for row in table1.find_all('tr'):    
            columns = row.find_all('td')
            if(columns[1].text.strip() == 'Bench'):
                break
            elif(columns != [] and n>1):
                playerNo = columns[0].text.strip()
                games_played = columns[24].text.strip()
                assists= columns[25].text.strip()
                pName = columns[1].text.strip()
                goals = columns[26].text.strip()
                df = df.append({'PlayerNo': playerNo,'GP': games_played, 'A': assists, 'PName': pName, 'G': goals}, ignore_index=True)
            n+=1
        obs = []
        ob = {}
        ob['players'] = []
        ob['name'] = value
        for index, row in df.iterrows():
            r = {}
            r['playerNo'] = row['PlayerNo']
            r['games_palyed'] = row['GP']
            r['assists'] = row['A']
            r['name'] = row['PName']
            r['goals'] = row['G']
            ob['players'].append(r)
        obs.append(ob)
        print(obs)
    except Exception as e:
        print(e)

