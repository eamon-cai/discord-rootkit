import sqlite3
import os
from datetime import datetime, timedelta
from urllib.parse import urlparse, urlunparse

history_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Microsoft\Edge\User Data\Default\History')

def convert_time(timestamp):
    epoch_start = datetime(1601, 1, 1)
    return epoch_start + timedelta(microseconds=timestamp)

def remove_url_params(url):
    parsed_url = urlparse(url)
    return urlunparse(parsed_url._replace(query='', fragment=''))

conn = sqlite3.connect(history_path)
cursor = conn.cursor()
cursor.execute('SELECT url, title, last_visit_time FROM urls')
rows = cursor.fetchall()
output_file = 'edge_history.txt'

url_width = 100
title_width = 100
last_visit_width = 30

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(f'{'URL':<{url_width}} {'TITLE':<{title_width}} {'LAST VISIT':<{last_visit_width}}\n')
    file.write('='*(url_width + title_width + last_visit_width + 2) + '\n')
    for row in rows:
        url = remove_url_params(row[0])
        title = row[1]
        visit_time = convert_time(row[2])
        file.write(f'{url:<{url_width}} {title:<{title_width}} {visit_time}\n')

conn.close()