from pythonping import ping
from check_ip_function import check_ip
from time import sleep


def check_valid_ip():
    """ 
    Function is looking for valid IP and checking is IP is up, blank will return default
    IP which is 192.168.1.1
    """
    HOST = input("Your host IP(empty string is 192.168.1.1): ")
    if check_ip(HOST):
        return HOST
    elif HOST == '':
        HOST = "192.168.1.1"
        return HOST
    else:
        print("You type incorrect IP address!!!")
        return False


def host_UP(HOST):
    """
    Function returning "Request timed out" if host is down
    and will replay "Host is up" if it gets reply from host
    """
    if HOST:
        resp = ping(HOST, count=15)
        ping_count = 0
        while not resp.success():
            print("Unreachable")
            resp = ping(HOST, count=2, verbose=True)
            ping_count += 1
            if ping_count == 3:
                print("Seems like  device isn't connected to PC. Disabling the script")
                return False
        else:
            sleep(2)
            print("\nHost is UP")
            return HOST

    else:
        return False

def ping_until_UP(ip):
    if not ip:
        print("\nThe host is unavailable after sending the file\n")
    else:
        resp = ping(ip, count=15)
        ping_count = 0
        while not resp.success():
            print("Unreachable")
            resp = ping(ip, count=2, verbose=True)
            ping_count += 1
            if ping_count == 3:
                print("Seems like  device isn't connected to PC.")
                return False
        else:
            sleep(10)
            print("\nHost is UP")
            return ip



if __name__ == "__main__":
    print(host_UP(check_valid_ip()))
