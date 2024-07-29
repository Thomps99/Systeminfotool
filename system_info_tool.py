import os
import platform
import psutil
import socket
import subprocess
import shutil
import time
from datetime import timedelta
from termcolor import colored
from getpass import getuser

def get_basic_info():
    hostname = socket.gethostname()
    kernel_version = platform.release()
    distribution = ' '.join(platform.linux_distribution())
    return hostname, kernel_version, distribution

def get_cpu_info():
    cpu_model = platform.processor()
    architecture = platform.architecture()[0]
    cores = os.cpu_count()
    try:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
    except:
        temp = "Unavailable"
    return cpu_model, architecture, cores, temp

def get_memory_info():
    mem = psutil.virtual_memory()
    total = mem.total // (1024**2)
    used = mem.used // (1024**2)
    free = mem.available // (1024**2)
    return total, used, free

def get_disk_usage():
    partitions = psutil.disk_partitions()
    usage_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total = usage.total // (1024**3)
        used = usage.used // (1024**3)
        free = usage.free // (1024**3)
        usage_info.append((partition.device, total, used, free))
    return usage_info

def get_network_info():
    interfaces = psutil.net_if_addrs()
    net_io = psutil.net_io_counters(pernic=True)
    network_info = []
    for iface, addrs in interfaces.items():
        ip = 'N/A'
        mac = 'N/A'
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
            elif addr.family == psutil.AF_LINK:
                mac = addr.address
        stats = net_io.get(iface, None)
        if stats:
            network_info.append((iface, ip, mac, stats.bytes_sent, stats.bytes_recv))
    return network_info

def get_uptime():
    return timedelta(seconds=int(time.time() - psutil.boot_time()))

def ping_test(host):
    if getuser() != 'root':
        print(colored("This operation requires administrative privileges. Please run the script with sudo.", "red"))
        return
    try:
        output = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

def colorize_output():
    def colorize(text, color):
        return colored(text, color)
    return colorize

def interactive_mode():
    print("Select the information you want to display:")
    print("1. Basic System Information")
    print("2. CPU Information")
    print("3. Memory Information")
    print("4. Disk Usage")
    print("5. Network Information")
    print("6. Uptime")
    print("7. Ping Test")
    print("8. All Information")
    
    choice = input("Enter your choice: ")
    return choice

def main():
    color = colorize_output()
    
    while True:
        choice = interactive_mode()
        
        if choice == '1' or choice == '8':
            hostname, kernel_version, distribution = get_basic_info()
            print(color("Basic System Information:", "blue"))
            print(f"Hostname: {hostname}")
            print(f"Kernel Version: {kernel_version}")
            print(f"Distribution: {distribution}\n")

        if choice == '2' or choice == '8':
            cpu_model, architecture, cores, temp = get_cpu_info()
            print(color("CPU Information:", "blue"))
            print(f"Model: {cpu_model}")
            print(f"Architecture: {architecture}")
            print(f"Cores: {cores}")
            print(f"Temperature: {temp}\n")

        if choice == '3' or choice == '8':
            total, used, free = get_memory_info()
            print(color("Memory Information:", "blue"))
            print(f"Total Memory: {total} MB")
            print(f"Used Memory: {used} MB")
            print(f"Free Memory: {free} MB\n")

        if choice == '4' or choice == '8':
            usage_info = get_disk_usage()
            print(color("Disk Usage:", "blue"))
            for device, total, used, free in usage_info:
                print(f"Device: {device}")
                print(f"Total: {total} GB")
                print(f"Used: {used} GB")
                print(f"Free: {free} GB\n")
        
        if choice == '5' or choice == '8':
            network_info = get_network_info()
            print(color("Network Information:", "blue"))
            for iface, ip, mac, sent, recv in network_info:
                print(f"Interface: {iface}")
                print(f"IP Address: {ip}")
                print(f"MAC Address: {mac}")
                print(f"Bytes Sent: {sent}")
                print(f"Bytes Received: {recv}\n")

        if choice == '6' or choice == '8':
            uptime = get_uptime()
            print(color("Uptime:", "blue"))
            print(f"System Uptime: {uptime}\n")
        
        if choice == '7' or choice == '8':
            host = input("Enter a host or IP address to ping: ")
            print(color("Ping Test Results:", "blue"))
            ping_results = ping_test(host)
            if ping_results:
                print(ping_results)
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice. Please try again.")
        
        another = input("Would you like to see more information? (y/n): ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":
    main()
