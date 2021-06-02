#!/usr/bin/python3
from batterystats import Battery
from sched import scheduler
from time import time, sleep
from os import mkdir, path, environ as env

_BAT        = 0
_HOME       = "/home/shreyas/"
_LOG_FOLDER = _HOME + '/.batterylogs'
_LOG_FILE   = _LOG_FOLDER + f'/log_{_BAT}.csv'


bat = Battery()
bat_logger = scheduler(time, sleep)

if not path.exists(_LOG_FOLDER):
    print("creating folder",_LOG_FOLDER)
    mkdir(_LOG_FOLDER)

def log():
    data = bat.main_stats
    data = ','.join([str(data[key]) for key in data])

    with open(_LOG_FILE, 'a') as log_file:
        log_file.write(data+'\n')
    
    print(data)

while True:
    bat_logger.enter(300, 1, log)
    bat_logger.run()