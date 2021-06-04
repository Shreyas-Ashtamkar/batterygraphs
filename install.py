import sys
import os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

service_file = open("batterylogger.service", 'w')

NAME = "Battery Logger Service"
PYTHON_EXEC = sys.executable
THIS_FOLDER = os.path.dirname(__file__)

service = \
f'''[Unit]
Description={NAME}
After=multi-user.target
# Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart={PYTHON_EXEC} {THIS_FOLDER}/batterystatslogger.py
# StandardInput=tty-force

[Install]
WantedBy=multi-user.target
'''

service_file.write(service+'\n')

service_file.close()
