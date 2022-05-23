import csv
import paramiko
import json

with open("config.json","r") as f:
    config=json.load(f)

host =config["host"]
port =config["port"]
username = config["username"]
password = config["password"]

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,port,username,password)

with open ('VPN.csv','r',encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command1 = f"""/usr/sbin/sacli --user {row['username']} --key "conn_group" --value {row['group']} UserPropPut"""
        command2 = f"""/usr/sbin/sacli --user {row['username']} --new_pass={row['password']} SetLocalPassword"""
        stdin, stdout, stderr = client.exec_command(f"{command1} && {command2}")
        print(stdout.read().decode())
        err=stderr.read().decode()
        if err:
            print(err)

stdin.close()
