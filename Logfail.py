import psutil
import pandas as pd
import time

# Initialize an empty DataFrame
df = pd.DataFrame(columns=['Timestamp', 'CPU Usage'])

while True:
    # Get the current CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a new DataFrame for the new row
    new_row = pd.DataFrame([[timestamp, cpu_usage]], columns=['Timestamp', 'CPU Usage'])
    
    # Concatenate the new row to the existing DataFrame
    df = pd.concat([df, new_row], ignore_index=True)
    
    # Save the DataFrame to a CSV file
    df.to_csv('cpu_usage.csv', index=False)
    
    # Print the CPU usage (optional)
    print(f'{timestamp} - CPU Usage: {cpu_usage}%')
