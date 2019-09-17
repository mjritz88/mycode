#!/usr/bin/python3

import urllib.request
import json
import webbrowser

URL='https://api.nasa.gov/planetary/apod?api_key=iSvrIagmEbzvBZdnhSdWMtHuXau7Hq3r4it5xVin'

apodurlobj = urllib.request.urlopen(URL)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\nConverted Python data:")
print(decodeapod)

input("\nPress Enter to open NASA's Picture of the Day in your web browser")
webbrowser.open(decodeapod['url'])
