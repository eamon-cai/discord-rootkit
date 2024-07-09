import sqlite3
import os
from datetime import datetime, timedelta

# Path to the Edge cookies database file
cookies_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Microsoft\Edge\User Data\Default\Network\Cookies')

# Function to convert WebKit timestamp to human-readable format
def convert_time(timestamp):
    epoch_start = datetime(1601, 1, 1)
    return epoch_start + timedelta(microseconds=timestamp)

# Connect to the database
conn = sqlite3.connect(cookies_path)
cursor = conn.cursor()

# Query the cookies table
cursor.execute("SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc FROM cookies")

# Fetch all results
rows = cursor.fetchall()

# Define the output file path
output_file = 'edge_cookies.txt'

# Define column widths
host_key_width = 50
name_width = 50
value_width = 50
time_width = 30

# Write the results to the file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f"{'HOST KEY':<{host_key_width}} {'NAME':<{name_width}} {'VALUE':<{value_width}} {'CREATION TIME':<{time_width}} {'LAST ACCESS TIME':<{time_width}} {'EXPIRY TIME':<{time_width}}\n")
    file.write("="*(host_key_width + name_width + value_width + time_width*3 + 5) + "\n")
    for row in rows:
        host_key = row[0]
        name = row[1]
        value = row[2]
        creation_time = convert_time(row[3])
        last_access_time = convert_time(row[4])
        expiry_time = convert_time(row[5])
        file.write(f"{host_key:<{host_key_width}} {name:<{name_width}} {value:<{value_width}} {creation_time:<{time_width}} {last_access_time:<{time_width}} {expiry_time:<{time_width}}\n")

# Close the connection
conn.close()
