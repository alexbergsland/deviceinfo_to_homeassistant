# Device info to homeassistant
Send hdd and ram data to home assistant with python.

## Requirements
Python 3.3 or newer.\
`shutil.disk_usage` requires Python 3.3 and above.

## How to use
I have this script on all my servers so I get info of hdd and memory use sent to Home Assistant at regular intervals.
The script makes inegrations in Home Assistant like this if the hostname is `webserver`:
```bash
input_number.webserver_memory_used
```

I have the script shared through NFS so I only need to change it on one server for it to update on all of them.
My `crontab -e` looks like this:
```bash
# Send device info to Home Assistant
* * * * * /usr/bin/python3 /mnt/script/deviceinfo.py
```
Which will send the info every minute.

## Instructions
Change `http://192.168.44.27` to the IP of your Home Assistant instance.\
Change `YOUR-LONG-LIVED-TOKEN` to your long lived access token, you can make one in your profile.\
Scroll to the bottom, click Create Token. Give it a suitable name and paste it in this script.\
