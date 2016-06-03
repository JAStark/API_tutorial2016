# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:49:58 2016

@author: jenniferstark
"""
# This code is good if you only want a one-off collection of the data.
# If you want to collect data periodically, use 'scheduled_API_code.py'


import json
import csv
import requests
import pandas as pd

## prep code:
# create csv to append data to
output_filename = 'foo.csv'
fileWriter = csv.writer(open(output_filename, "w+"),delimiter=",")
fileWriter.writerow(['anc', 'census_tract', 'coords', 'district', 'method', 'objectid', 'offense', 'report_time', 'shift', 'ward'])

# grab JSON data from crime API:
crime_incidents_30day_url = 'http://opendata.dc.gov/datasets/dc3289eab3d2400ea49c154863312434_8.geojson'

response = requests.get(crime_incidents_30day_url)
response.raise_for_status() # check for errors in response.

data = json.loads(response.text)
data = data['features']

# Get the data from the JSON, subtract only fields of interest, and append to csv
def get_data(data):

    data_list = []

    # Add JSON records to a list, only including those specified fields
    for i in range(len(data)):
        data_list.append(get_json_fields(i))

    # Convert data_list into pandas DataFrame
    dataDF = pd.DataFrame(data_list)

    # open the csv created earlier in 'append' mode
    # append data in dataframe to the csv.
    with open(output_filename, 'a') as f:
        dataDF.to_csv(f, mode='a', header=False, index=False)


# organise JSON data into only the fields you want. Make sure they match what is
# specified above for your .csv fileWriter - needs to also be in the same order
# on the left are the csv fields
# on the right are the JSON fields
def get_json_fields(i):

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

get_data(data)
