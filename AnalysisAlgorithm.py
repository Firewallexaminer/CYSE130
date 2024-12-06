import pandas as pd


url = 'https://raw.githubusercontent.com/Firewallexaminer/CYSE130/refs/heads/main/cpu_usage.csv'
log = pd.read_csv(url)

log.head()

for value in log['CPU Usage']:
    if value > 70.0:
       warn = 'Syslog 4: Unusually High CPU Usage detected!'
       log['Debug'] = warn
       print(warn)
       log.to_csv('CPU_Warn.csv', index=False)
    elif value > 45.0:
        debug = 'Syslog 7: CPU Usage at ' + str(value)
        log['Debug'] = debug
        print(debug)
        log.to_csv('CPU_Warn.csv', index=False)
    else:
        log['Debug'] = 'Syslog 7: Low (normal)'
        print(7)
        log.to_csv('CPU_Warn.csv', index=False)

        

