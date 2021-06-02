#!/usr/bin/python3
from batterystats import Battery
from sched import scheduler
from time import time, sleep
from os import listdir as ls, mkdir, path, environ as env

_BAT        = 0
_HOME       = "/home/"+ls("/home")[0]
_LOG_FOLDER = _HOME + '/.batterylogs'
_LOG_FILE   = _LOG_FOLDER + f'/log_{_BAT}.csv'

bat = Battery()
bat_logger = scheduler(time, sleep)

if not path.exists(_LOG_FOLDER):
    print("creating folder",_LOG_FOLDER)
    mkdir(_LOG_FOLDER)

if not path.exists(_LOG_FILE):
    print("creating file",_LOG_FOLDER)
    with open(_LOG_FILE, 'a') as log_file:
        log_file.write("date,time,status,capacity,capacity_full,capacity_full_design")

def log():
    data = [
        bat.date,
        bat.time,
        bat.status,
        bat.capacity,
        bat.capacity_full,
        bat.capacity_full_design,
    ]
    data = ','.join([str(item) for item in data])

    with open(_LOG_FILE, 'a') as log_file:
        log_file.write('\n'+data)
    
    print(data)

while True:
    bat_logger.enter(300, 1, log)
    bat_logger.run()
