import ipaddress

def check_ip(ip):
	'''This function is checking for valid IP address'''
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError as err:
		return False


if __name__ == '__main__':
	ip1 = '10.0.50.1'
	ip2 = '10.1.45'

	print("IP address check...")
	print(ip1, check_ip(ip1))
	print(ip2, check_ip(ip2))
