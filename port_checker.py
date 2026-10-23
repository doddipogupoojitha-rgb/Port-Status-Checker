import socket
from datetime import datetime
import sys

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def check_port(target_ip, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target_ip, port))
        s.close()
        return "Open" if result == 0 else "Closed"
    except:
        return "Filtered"

print("-"*50)
print("PORT STATUS CHECKER - Workora Task")
print("-"*50)
target = input("Enter Target IP (e.g., 127.0.0.1): ").strip() or "127.0.0.1"
start_port = int(input("Enter Start Port: ") or 20)
end_port = int(input("Enter End Port: ") or 100)

try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid Hostname")
    sys.exit()

print(f"\nScanning {target} ({target_ip})")
print(f"{'PORT':<10} {'STATUS':<12} {'SERVICE':<15}")
print("-"*50)
for port in range(start_port, end_port+1):
    status = check_port(target_ip, port)
    service = get_service_name(port) if status == "Open" else "-"
    print(f"{port:<10} {status:<12} {service:<15}")
print("-"*50)
print("Scan Completed!")
