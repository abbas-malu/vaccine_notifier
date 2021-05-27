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
tommorow = today.split('-')

dd = input('Enter Date dd format: ')
mm = input('Enter Month mm format: ')
yyyy = input('Enter Year yyyy format: ')
dis_id = input('Enter District Id: ')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.101 Safari/537.36'}
t = 1
while True:
    data = json.loads(requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={dis_id}&date={dd}-{mm}-{yyyy}',headers=headers).text)
    # print(data)
    print(t)
    for i in data['sessions']:
        # print(i['name'],':',i['available_capacity_dose1'])
        if i['available_capacity_dose1']>1:
            print(i['name'],i['available_capacity_dose1'])
            push = pb.push_note('Dose Available',f'Center: {i["name"]} \n Doses: {i["available_capacity_dose1"]}')
    time.sleep(10)
    t += 1
