# 2.ifconfig_reg #

## 题目： ##
#### 解析ifconfig命令的标准输出，返回一个hash。key是网卡名称 value是对应的ip。 ####
## 答案： ##

####通过ifconfig命令将网卡名字和ip地址提取出来； 
####ifconfig | grep -E ' Link |inet addr:' |awk '{name=$1;ip=0;getline;sub(/inet addr:/,"");ip = $1;if(match(ip,"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"))print name,ip}-' ####