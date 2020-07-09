import getpass
import telnetlib
from ping_up import ping_until_UP


def ask_question(question=False):
	question = input("Do you want to send commands to your device by Telnet?(By default 'no')\n([y]/n)\n")
	if "yes" == question.lower() or 'y' == question.lower():
		return True
	elif "no" == question.lower() or "n" == question.lower():
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
		comand = True
		while comand != '':
			comand = input("Which command: \n\t")
			tn.write(comand.encode('ascii') + b'\n')
			print(tn.read_very_eager().decode('utf-8'))

		return print(tn.read_all().decode('ascii'))
	else:
		print("\nDone")
		return False


	

if __name__=="__main__":
	def_command(ping_until_UP("192.168.1.1"))