#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python example code to upload apk file to EPAM android test farm
"""
import ssl
import requests


TOKEN = 'some-uuid-like'
FILE = 'myfile.apk'
DEVICE = 'serialNo'
URL = 'mobilecloud.epam.com/automation/api/storage/install/'
SCHEME = 'https'
SSLIGNORE = 'Yes'

if SSLIGNORE == 'Yes':
    requests.packages.urllib3.disable_warnings()
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
else:
    pass


def main():
    """
    post function for authorize and upload/install apk
    """
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    fullurl = f'{SCHEME}://{URL}{DEVICE}'
    prepfile = {'file': open(FILE, 'rb')}
    r_url = requests.post(fullurl, files=prepfile, headers=headers)
    print(r_url)


if __name__ == '__main__':
    main()
