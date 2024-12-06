import psutil
import pandas as pd
import time

# Creates a table with time, hostname, and CPU usage
df = pd.DataFrame(columns=['Timestamp', 'CPU Usage', 'Hostname'])


# While script is running, checks and prints the cpu usage every second
while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    Timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'{Timestamp} - CPU Usage: {cpu_percent}%')
    new_row = pd.DataFrame([[Timestamp, cpu_percent, 'F3-C3-Switch']], columns=['Timestamp', 'CPU Usage', 'Hostname'])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('cpu_usage.csv', index=False)
    time.sleep(1)
    