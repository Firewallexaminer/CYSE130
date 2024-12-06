import pandas as pd


url = 'https://raw.githubusercontent.com/Firewallexaminer/CYSE130/refs/heads/main/cpu_usage.csv'
log = pd.read_csv(url)

log.head()

for value in log['CPU Usage']:
    if value > 70.0:
       warn = 'Syslog 4: Unusually High CPU Usage detected!'
       log['Debug'] = warn
       print(warn)
        

