from pprint import pprint
import requests
import json
import datetime
import communication

# Creating variables
date_proc=datetime.date.today().strftime('%Y%m%d')
APIKEY='318a6436abf2421287be1230935bfc99'
fileCityID='city.list.json'
fileResult='wheather_{}.json'.format(date_proc)

def readCityID(country):
    listCityID=[]
    count=0
    with open(fileCityID) as f:
        data = json.load(f)
        
        for i in data:
            if i['country'] == country:
                # Max number of cityid per request
                if count < 20:
                    listCityID.append(i['id'])
                    count+=1
        
    return(listCityID)                

ids=','.join(str(e) for e in readCityID('BR'))

url='http://api.openweathermap.org/data/2.5/group?id={}&units=metric&APPID={}'.format(ids,APIKEY)
r = requests.get(url)
dictRequest=r.json()

print(dictRequest)

# with open(fileResult,'w') as f:
#     f.write(json.dumps(dictRequest))
