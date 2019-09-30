from netmiko import ConnectHandler
from getpass import getpass
import argparse
import subprocess
import sys
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("hostname", help="OLT name")
	parser.add_argument("ont", help="ONT slot")
	
	args = parser.parse_args()
	

host = args.hostname
device = {
    'device_type': 'alcatel_sros',
    'host': host,
    'username': 'user',
    'password': 'alka%tail',
}
net_connect = ConnectHandler(**device)
txrx = net_connect.send_command("show equipment ont utilization current-interval " +str(args.ont)+ " detail | match exact:txucbyte")
rxrx = net_connect.send_command("show equipment ont utilization current-interval " +str(args.ont)+ " detail | match exact:rxucbyte")
data = (txrx.strip())
data1 = (rxrx.strip())
final=data.split()[2]
final1=data1.split()[2]
print ("download:"+final+" upload:"+final1)

#rxtx = net_connect.send_command("show equipment ont utilization current-interval " +str(args.ont)+ " detail | match exact:rxucbyte")
#data=[]
#clean_data=[]
#with open('check','w') as f:
#	print (txrx.replace('txucbyte : ', ' '), rxtx.replace('rxucbyte : ', ' '), file=f)
#f.close()
#with open('check','r') as f:
#	data=f.readlines()
	#print(data)
#	for x in data:
		#print(x.strip())
#		val=x.strip()
#		clean_data.append(val)
#	print(str("txucbyte:")+clean_data[1], str("rxucbyte:")+clean_data[2])
#f.close()
#net_connect.disconnect()

