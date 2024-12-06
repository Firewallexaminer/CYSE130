import pandas as pd


url = 'https://raw.githubusercontent.com/Firewallexaminer/CYSE130/refs/heads/main/cpu_usage.csv'
log = pd.read_csv(url)

for value in log['CPU Usage']:
    if value > 70.0:
       warn = 'Syslog 4: Unusually High CPU Usage detected!'
       log['Debug'] = warn
       print(warn)
    elif value > 45.0:
        debug = 'Syslog 7: CPU Usage at ' + str(value)
        log['Debug'] = debug
        print(debug)
    else:
        log['Debug'] = 'Syslog 7: Low (normal)'
        print('Syslog 7: low')
log.to_csv('CPU_Warn.csv', index=False)