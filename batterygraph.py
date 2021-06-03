from matplotlib import pyplot as graph, dates
import datetime

_BATTERY_LOGS = "/home/shreyas/.batterylogs/log_0.csv"

# date_format = dates.Dateformatter("%m-%d-%y")
# time_format = dates.Dateformatter("%H:%M:%S")

log_records = []
convert = [
    lambda date          : str(date),
    lambda time          : str(time),
    lambda status        : status.lower(),
    lambda capacity      : int(capacity),
    lambda charge_full   : int(charge_full),
    lambda charge_design : int(charge_design),
    lambda health        : int(health),
]

to_time = lambda time_log: int(time_log.split(':')[0])*100+(int(time_log.split(':')[1])*10//6)

with open(_BATTERY_LOGS) as log_file:
    log_records = log_file.readlines()

log_records = [[convert[i](log) for i, log in enumerate(log_row.split(','))] for log_row in log_records[1:]]

# print(*log_records, sep='\n')

# x_time = list(range(len(log_records)-1))
x_time = [to_time(logs[1]) for logs in log_records[1:]]
y_time = [logs[3] for logs in log_records[1:]]


#plot
graph.plot(x_time,y_time)

# beautify the x-labels
graph.gcf().autofmt_xdate()
graph.title("Battery Usage With Time")
graph.show()
