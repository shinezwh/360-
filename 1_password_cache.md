# 1.password_cache #
##问题：  ##
#### 运维操作在很多情况下需要访问不同的服务器，运维人员可能会频繁的输入自己的账号和密码。是否可以通过一个简单方式只需要输入一遍密码，然后余下的操作都可以不再重复的输入密码。密码应该存储在什么地方会比较隐蔽，让有这台机器sudo权限的其他人看不到####
## 答案： ##

#### 将所有要远程的服务器的私钥放在一台服务器上，所有其他服务器都用一个公钥，alias myssh=“ssh -i /root/.ssh/key.txt”,这个key.txt要设置好权限。然后配置ssh信任，如果要远程哪台服务器直接myssh ip或者域名，然后选择记住密码；这样只需要在第一次登陆是输入密码，其他时候不需再次输入密码。 ####