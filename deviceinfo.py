#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################
# Change url to your Home Assistant url
# Change YOUR-LONG-LIVED-TOKEN to your token in Home Assistant
#
# This script will send how much ram and disk space you are
# have, how much is used and how much is free on each decice.
# Six integrations will be created in Home Assistant,
################################################################


import shutil
import os
import socket
from requests import post

def setdata(endpoint, state, friendly_name, unit, icon): 
    url = "http://192.168.44.27:8123/api/states/" + endpoint
    headers = {
        "Authorization": "Bearer YOUR-LONG-LIVED-TOKEN",
        "content-type": "application/json",
    }
    data = {"state": state, "attributes": {"friendly_name": friendly_name, "icon": icon, "unit_of_measurement": unit}}

    response = post(url, headers=headers, json=data)
    print(response.text)

# get hostname
mhostname = socket.gethostname()
mhostname = mhostname.lower() # make lowecase

# get memory info in megabytes
tot_m, used_m, free_m, shared_m, buff_m, available_m = map(int, os.popen('free -t -m').readlines()[-3].split()[1:])
# Use the line below if you are interested in the total of ram + swap
#tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

# get diskspace info in bytes
total_disk, used_disk, free_disk = shutil.disk_usage("/")

# bytes to terrabytes
def toTB(mybytes):
    mytb = round(mybytes / 1099511627776, 1)
    return mytb

# megabytes to gigabytes
def toGB(mybytes):
    mygb = round(mybytes / 1073741824, 1)
    return mygb

# megabytes to gigabytes
def mb_to_GB(mymegabytes):
    mygb = round(mymegabytes * 0.0009765625, 1)
    return mygb

# data comes as bytes so make it GB instead
total_disk = toGB(total_disk)
used_disk = toGB(used_disk)
free_disk = toGB(free_disk)

# minne
print("input_number." + mhostname + "_memory_total")
setdata("input_number." + mhostname + "_memory_total", tot_m, mhostname + " memory total", "MB", "mdi:memory")
print("input_number." + mhostname + "_memory_used")
setdata("input_number." + mhostname + "_memory_used", used_m, mhostname + " memory used", "MB", "mdi:memory")
print("input_number." + mhostname + "_memory_free")
setdata("input_number." + mhostname + "_memory_free", free_m, mhostname + " memory free", "MB", "mdi:memory")

# hdd
print("input_number." + mhostname + "_hdd_total")
setdata("input_number." + mhostname + "_hdd_total", total_disk, mhostname + " hdd total", "GB", "mdi:harddisk")
print("input_number." + mhostname + "_hdd_used")
setdata("input_number." + mhostname + "_hdd_used", used_disk, mhostname + " hdd used", "GB", "mdi:harddisk")
print("input_number." + mhostname + "_hdd_free")
setdata("input_number." + mhostname + "_hdd_free", free_disk, mhostname + " hdd free", "GB", "mdi:harddisk")
