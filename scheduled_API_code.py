# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 21:53:57 2016

@author: jenniferstark
"""


import json
import csv
import requests
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging


output_filename = 'spider_foo.csv'
fileWriter = csv.writer(open(output_filename, "w+"),delimiter=",")
fileWriter.writerow(['anc', 'census_tract', 'coords', 'district', 'method', 'objectid', 'offense', 'report_time', 'shift', 'ward'])

def fetch():

    crime_incidents_30day_url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8.geojson'

    response = requests.get(crime_incidents_30day_url)
    time.sleep(5)
    response.raise_for_status() # check for errors in response.

    data = json.loads(response.text) #r.json()
    print("\nThis is the response status: ", response.raise_for_status())

    data = data['features']

    get_data(data)



def get_data(data):

    data_list = []

    print("Starting 'get_data': ")
    for i in range(len(data)):
        data_list.append(get_json_fields(data, i))

    dataDF = pd.DataFrame(data_list)
    #return dataDF

    print("Started making csv: ")
    with open(output_filename, 'a') as f:
        dataDF.to_csv(f, mode='a', header=False, index=False)

    drop_duplicates(output_filename)




def drop_duplicates(output_filename):
        print("Starting 'drop_duplicates':  ")
        temp = pd.read_csv(output_filename)
        temp.drop_duplicates(subset=temp.objectid,keep='last', inplace=True)
        temp.to_csv(output_filename, header=False, index=False)



def get_json_fields(data, i):

    row_data = {}


    row_data['anc'] = data[i]['properties']['ANC']
    row_data['census_tract'] = data[i]['properties']['CENSUS_TRACT']
    row_data['coords'] = data[i]['geometry']['coordinates']
    row_data['district'] = data[i]['properties']['DISTRICT']
    row_data['method'] = data[i]['properties']['METHOD']
    row_data['objectid'] = data[i]['properties']['OBJECTID']
    row_data['offense'] = data[i]['properties']['OFFENSE']
    row_data['report_time'] = data[i]['properties']['REPORTDATETIME']
    row_data['shift'] = data[i]['properties']['SHIFT']
    row_data['ward'] = data[i]['properties']['WARD']

    return row_data


# Create a scheduler to trigger every N minutes
# http://apscheduler.readthedocs.org/en/3.0/userguide.html#code-examples
logging.basicConfig()
scheduler = BackgroundScheduler()
scheduler.add_job(fetch, 'interval', hours = 696) # = 29 days
scheduler.start()

while True:
	time.sleep(1)

#nohup python -u scheduled_API_code.py > nohup.txt &
