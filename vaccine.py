import json
import requests
import webbrowser
import time
import html
import datetime
from pushbullet import PushBullet
today = datetime.datetime.today().strftime("%m-%d-%Y")
api_key = 'o.d127KfpZF6bs88SzEIxF54govzvQRkau'
pb = PushBullet(api_key=api_key)

print(type(today))
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
for i in range(1,10000):
    print(i)
    data = json.loads(requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=314&date=28-05-2021',headers=headers).text)
    for i in data['sessions']:
        if i['available_capacity_dose1']>1:
            print(i['name'],i['available_capacity_dose1'])
            push = pb.push_note('Dose Available',f'Center: {i['name']} \n Doses: {i['available_capacity_dose1']}')
    time.sleep(2)
