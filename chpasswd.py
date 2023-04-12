# 用ssh批量修改密码的脚本
import paramiko  # 远控模块
import configparser  # 读取config模块
import os

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取ip列表和账号密码
ips = config['hosts']['ips'].split(',')
username = config ['config']['username']
passwd_old = config['config']['passwd_old']
passwd_new = config['config']['passwd_new']

n = 0 # 计数

# 遍历ip列表，连接远程服务器，更改密码
for ip in ips:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=passwd_old)
    stdin, stdout, stderr = ssh.exec_command('echo "{0}:{1}" | chpasswd'.format(username, passwd_new))
    ssh.close()
    n = n + 1

print("完成，共修改",n,"个。")
os.system('pause')
