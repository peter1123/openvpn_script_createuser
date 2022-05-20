import pandas as pd
import string
import secrets
import paramiko
import json

host ='ip'
port ='22'
username = 'root'
password = 'password'

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,port,username,password)

command1 = f"""/usr/sbin/sacli UserPropGet """
stdin, stdout, stderr = client.exec_command(command1)
#获取当前用户列表
currentusr = stdout.read().decode()
#json格式化
jcurrentusr = json.loads(currentusr)


fPath = 'VPN.csv'
df = pd.read_csv(fPath)
x=df.columns.get_loc('password')
newusr = df['username'].tolist()
#比较是否存在重复的用户名
Duplicate_usr=(list(set(newusr)&set(jcurrentusr.keys())))

#如果有重复用户名则中断脚本并报错
if Duplicate_usr==False:
    print('Duplicate username,please check:')
    print(Duplicate_usr)
    exit()
#生成密码
for r in df.index:
    alphabet = string.ascii_letters + string.digits
    passcode = ''.join(secrets.choice(alphabet) for i in range(8))
    df.iat[r,x]=passcode
df.to_csv('VPN.csv',index=False)
