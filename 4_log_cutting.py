#!/usr/bin/env python
#-*-coding:utf-8-*-
#Python access.log cut

import subprocess 

def mkdir():
subprocess.call('mkdir -pv /var/log/$(date -d "yesterday" +"%Y")/$(date -d "yesterday" +"%m")/',shell=True)
def mv():
subprocess.call('mv /var/log/access.log /var/log/$(date -d"yesterday"+"%Y")/$(date -d "yesterday"+"%m")/access_$(date -d "yesterday"+"%Y%m%d").log,shell=TRUE)
def kill():
pid =open("/var/log/access.log","r")
f =pid.read()
f =f.strip()
pid.close()
kill ="kill"
kill_usage ="-USR1"
subprocess.call([kill,kill_usage,f])
defmain():
mkdir()
mv()
kill()
if__name__ =="__main__":
main()