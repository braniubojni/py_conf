import getpass
import telnetlib
from ping_up import ping_until_UP


def ask_question(question=False):
	question = input("Do you want to send commands to your device by Telnet?(By default 'no')\n")
	if "yes" == question.lower():
		return True
	elif "no" == question.lower():
		return False
	else:
		print("You wrote neither than 'yes' or 'no'. I'll accept that as 'no'\n")
		return False

# after reboot we'll send comand by Telnet
def def_command(ip):
	if not ip:
		return print("\nThe host is unavailable after sending the file*")
	if ask_question():
		print("\n0 will mean exit\n")
		user = input("\nType login name: ")
		passwd = getpass.getpass()
		tn = telnetlib.Telnet(ip)
		tn.write(user.encode('ascii') + b'\n')
		tn.read_until(b'Password: ')
		tn.write(passwd.encode('ascii') + b"\n")
		comand = input("Which command: \n\t")
		while comand != 0:
			tn.write(comand.encode('ascii') + b'\n')

		return print(tn.read_all().decode('ascii'))
	else:
		print("\nDone")
		return False


	# else:
	# 	user = input("\nType login name: ")
	# 	passwd = getpass.getpass()
	# 	tn = telnetlib.Telnet(ip)
	# 	tn.read_until(b'Login: ')
	# 	tn.write(user.encode('ascii') + b'\n')
	# 	tn.read_until(b'Password: ')
	# 	tn.write(passwd.encode('ascii') + b"\n")
	# 	tn.write(b"fdefault save\n")
	# 	tn.write(b"exit\n")

	

if __name__=="__main__":
	def_command(ping_until_UP("192.168.1.1"))