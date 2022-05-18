import pandas as pd
import string
import secrets

fPath = 'VPN.csv'
df = pd.read_csv(fPath)
x=df.columns.get_loc('password')

for r in df.index:
    alphabet = string.ascii_letters + string.digits
    passcode = ''.join(secrets.choice(alphabet) for i in range(8))
    df.iat[r,x]=passcode
df.to_csv('VPN.csv',index=False)