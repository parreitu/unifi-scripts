#!/usr/bin/python

import os
import time
from datetime import datetime

# You can schedule this script in your crontab to be executed periodically

# You need the sshpass package, so you should insntall it before:  apt-get install sshpass
 
# first of all, you should issue a ssh connection from the machine where you are executing this
# script to each AP included in the unifi_ap_list. Once you have done this, you are sure that the
# the AP's fingerprint is included in your machine's  .ssh/known_hosts file, something neccessary 
# to estabilish a ssh connection

# Change this list and include the IP address of the AP's you want to reboot
unifi_ap_list=["IP_ADDRESS01","IP_ADDRESS01","IP_ADDRESS01",....,"IP_ADDRESS01"]

# You can find/change this information in your "Unifi Controller --> Settings --> Site --> Device Authentication"
user="myuser"
password="mypassword"


logfile = open('/tmp/unifi-reboot.log','a')


logfile.write("============================================================================================"+'\n')

for ap in unifi_ap_list:
    i = datetime.now()
    logfile.write(str("DateTime: " + str(i) + "-->  Rebooting Unifi AP with IP address: " + ap + '\n'))      
    command = 'sshpass -p '+password+' ssh  '+user+'@'+ap+' reboot'
    #print command
    os.system(command)
    # Wait for 5 minutes before restarting the next AP. I think that it is better giving time to each
    # AP for recovering itself and search for a free channel when the AP's channel config is set to 'Auto'.
    time.sleep(300)
