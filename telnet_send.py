import getpass
import telnetlib
from ping_up import ping_until_UP



# after reboot we'll send comand by Telnet
def def_command(ip):
	if not ip:
		return print("\nThe host is unavailable after sending the file*")
	else:
		user = input("\nType login name: ")
		passwd = getpass.getpass()
		tn = telnetlib.Telnet(ip)
		tn.read_until(b'Login: ')
		tn.write(user.encode('ascii') + b'\n')
		tn.read_until(b'Password: ')
		tn.write(passwd.encode('ascii') + b"\n")
		tn.write(b"fdefault save\n")
		tn.write(b"exit\n")

	return print(tn.read_all().decode('ascii'))

if __name__=="__main__":
	def_command(ping_until_UP("192.168.1.1"))