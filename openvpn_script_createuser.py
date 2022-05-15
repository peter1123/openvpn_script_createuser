import csv
import os

with open ('VPN.csv','r',encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        os.system('/usr/sbin/sacli --user '+ row['username']+ ' --new_pass='+ row['password'] + ' --key '"conn_group"' --value '+ row['group']+' UserPropPut')
