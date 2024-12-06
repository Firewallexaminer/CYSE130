import psutil
import pandas as pd
import time



# Creates a table with time, hostname, and CPU usage
df = pd.DataFrame(columns=['Timestamp', 'CPU Usage', 'Hostname'])

# While script is running, checks and prints the cpu usage every second
while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    Timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"CPU Usage: {cpu_percent}%")
    time.sleep(1)


# 
df = df.append({'Timestamp': timestamp, 'CPU Usage': cpu_percent, 'Hostname': "CamServer"}, ignore_index=True)
df.to_csv('cpu_usage.csv', index=False)
print(f'{timestamp} - CPU Usage: {cpu_usage}%')