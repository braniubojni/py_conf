from time import sleep
from check_ip_function import check_ip
from ping_up import host_UP, check_valid_ip, ping_until_UP
from telnet_send import def_command
from tftp_send import send_tftp_conf
import tftpy

def main():
	def_command(ping_until_UP(send_tftp_conf(host_UP(check_valid_ip()))))


if __name__ == "__main__":
	main()