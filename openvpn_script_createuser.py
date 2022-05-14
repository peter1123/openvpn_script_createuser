import csv
import os

csvfile= open('/tmp/VPN.csv','r')
reader = csv.DictReader(csvfile)

for row in reader:
    os.system('/usr/local/openvpn_as/scripts/sacli --user '+ row['username']+ ' --new_pass='+ row['password'] + ' --key "conn_group" --value '+ row['group']+' UserPropPut')
