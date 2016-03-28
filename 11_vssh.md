# 11.vssh #

## 题目： ##

11.vssh：在对单台机器做操作时我们经常会用“ssh ip”的方式登录到一台服务器上，能不能编写这样一个工具vssh ip1,ip2,...ipn来模拟登录到n台服务器，
登录后所有操作相当于同时对n台服务器生效

## 答案： ##

可以通过expect写成shell脚本来批量处理，具体如下：
如果系统里没有expect请自行到官网下载安装：http://expect.sourceforge.net/
### 1、创建服务器列表配置文件：
[root@localhost ~]# vi server_list.conf

说明：配置文件有4列，以空格分割：服务器IP ssh端口号 用户名 密码
### 2、编写expect脚本： ###
[root@localhost ~]# vi dotask.exp

set ipaddress [lindex $argv 0]
set port [lindex $argv 1]
set username [lindex $argv 2]
set passwd [lindex $argv 3]
set timeout 30
spawn ssh $ipaddress -p$port -l$username
expect {
"yes/no" { send "yes\r";exp_continue }
"password:" { send "$passwd\r" }
}
expect -re "\](\$|#) "
send "touch test \r"
expect -re "\](\$|#) "
send "exit\r"

说明：这里只实现了登录服务器后在当前目录创建了一个test文件，具体需求请自行修改添加命令

### 3、批量执行 ###
其实只要写好第2步的脚本就可以通过下面命令执行一台服务器的处理：
[root@localhost ~]# expect dotask.exp 192.168.0.10 22 root 123456
但为了能批量处理n台，再写个shell脚本就行了，如下：
[root@localhost ~]# vi doexcute.sh
\#!/bin/bash

filename="server_list.conf"
while read line
do
 \#echo $line;
  expect dotask.exp$line
done < $filename

说明：读取配置文件，循环执行
