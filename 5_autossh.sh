#!/bin/bash

while [ '' == '' ]
do
 ssh_d_process_num=`ps aux|grep -E 'ssh \-' |grep -v grep |wc -l`
 if [ "$ssh_d_process_num" == "0" ]; then
  /home/user/sshpass -p "password" ssh -D 7070 user@ServerIP &
 fi

 sleep 300
done