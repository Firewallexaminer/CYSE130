import pandas as pd


url = 'https://raw.githubusercontent.com/Firewallexaminer/CYSE130/refs/heads/main/cpu_usage.csv'
log = pd.read_csv(url)

i = 0
while i < 18:
    if log['CPU Usage'] > 70.0:
        print('Alert! Unusually High CPU Usage detected!')
    i = i+1
