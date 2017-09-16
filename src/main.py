__author__ = 'sudeep'

import os
from driveapi_interface import get_api_key, get_service, get_file, download_file
from file import get_list_from_file
from participant import get_participants
from email import send_email, compose_email

service_name = 'drive'
version = 'v2'
file_id = '1lS84DTgZfNOaYNMOHFlTV_sx4IVRT1pRkHIuloozjfI'
api_key = get_api_key()

service = get_service(service_name, version, api_key)
drive_file = get_file(service, file_id)
content = download_file(service, drive_file)

# TODO - Refactor this and make it a function that retrieves the latest copy of the file and saves it as newVersion.csv
local_version = open('../newVersion.csv', 'w')
local_version.write(content)
local_version.close()

old_list = get_list_from_file('../resources/oldVersion.csv')
new_list = get_list_from_file('../resources/newVersion.csv')
participants = get_participants(old_list, new_list)

for i in participants:
    send_email(i.email, [p.email for p in participants if p != i][0], compose_email(i, participants))

os.remove('../resources/oldVersion.csv')
os.rename('../resources/newVersion.csv', '../resources/oldVersion.csv')



