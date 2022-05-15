import csv
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#please change your username & password
client.connect(hostname='ipaddress', port=22, username='username', password='password')

with open ('VPN.csv','r',encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stdin, stdout, stderr = client.exec_command('/usr/sbin/sacli --user '+ row['username']+ ' --key '"conn_group"' --value '+ row['group']+' UserPropPut;/usr/sbin/sacli --user '+ row['username']+ ' --new_pass='+ row['password'] +' SetLocalPassword')
stdin.close()
