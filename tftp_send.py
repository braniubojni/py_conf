from time import sleep
from check_ip_function import check_ip
from ping_up import host_UP,check_valid_ip
import tftpy

# E:\Config\6511.conf
# E:\Config\6519VPN.conf


def send_tftp_conf(ip):
    """
        This function is sending config to host,by port 69
    """
    if ip:
        path = input("\nType your path till filename\nExample:\n" + "\t" +r"E:\Config\filename.conf" + "\n")
        conf_name = path.split("\\")[-1]
        try:
            print("Sending config/firmware by TFTP ...\n")
            client = tftpy.TftpClient(ip, port=69)
            client.upload(filename=conf_name, input=path)
            print("\nConfig upload is done...\n")
            sleep(20)            
        except:
            print("\nSomething went wrong probably problem with config path or in hosts side TFTP port is closed")
        return ip
    else:
        print("ip was disappered in tftp fun")
        return False


if __name__ == "__main__":
    print(send_tftp_conf(host_UP(check_valid_ip())))
    
    