import sys
import os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

service_file = open("batterylogger.service", 'w')

NAME = "Battery Logger Service"
PYTHON_EXEC = sys.executable
THIS_FOLDER = PYTHON_EXEC.split('venv')[0][:-1] if 'venv' in PYTHON_EXEC else os.path.dirname(__file__)
print(__file__)

service = \
f'''[Unit]
Description={NAME}
After=multi-user.target
# Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart={PYTHON_EXEC} {THIS_FOLDER if THIS_FOLDER else '.' }/batterystatslogger.py
# StandardInput=tty-force

[Install]
WantedBy=multi-user.target
'''

service_file.write(service+'\n')

service_file.close()
