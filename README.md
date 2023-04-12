# SSH_chpasswd
一个快速更改多个linux服务器密码的python脚本。A Python script that quickly changes passwords for multiple Linux servers.

# 介绍
在2023年4月11日，我的老师让我写的一个python脚本，用来快速更改多个linux服务器的密码。

共有两个文件，分别是chpasswd.py和config.ini。

在config.ini文件里有两项，分别是“[hosts]”和“[config]”。

[hosts]里“ips=”后面填写ip，多个ip用“,”隔开。

并且在[config]的“username=”后面填账号，“passwd_old=”后面填更改前的旧密码，“passwd_new=”后面填更改后的新密码。

为了方便使用，我将python脚本做成了exe一起上传。

# Introduction
English:

On April 11, 2023, my teacher asked me to write a Python script to quickly change passwords for multiple Linux servers. 

There are two files, chpasswd.py and config.ini. 

There are two items in the config.ini file, namely "[hosts]" and "[config]". 

Fill in the IP address after "ips=" in [hosts], and separate multiple IPs with ",". 

And fill in the account after "username=" in [config], the old password before the change after "passwd_old=", and the new password after the change after "passwd_new=".

For ease of use, I have made the Python script into an exe and uploaded it together.
