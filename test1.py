# from tkinter import *
# import serial
# import RPi.GPIO as GPIO
# from threading import * 
# import time,datetime,json
# from urllib.request import urlretrieve
# from hashlib import md5


#with open("conf.json", "r") as conf_file: #opened conf json file
# conf_file = str(open("conf.json",'r'))
# print(conf_file)
# print(type(conf_file))
    
    #global conf_json
    #conf_json = json.load(conf_file)
# conf_file.close()
import requests 
  
# api-endpoint 
URL = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1"
try:
    global r
    r = requests.get(URL) 
    global conf_json
    conf_json = r.json()
        # urlretrieve("http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1","conf.json")
except:
    pass

print(conf_json)