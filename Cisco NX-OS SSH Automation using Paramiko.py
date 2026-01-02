
# This program will simply log in to the device and run connect nxos and show interface brief and give us the output.
import paramiko
import time
from getpass import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# =========Device Details=========

Host = "X.X.X.X" # Enter device IP address.
username = "admin"
password = getpass("enter your passowrd : ")
port = 22

try:
    ssh.connect(
        hostname= Host,
        username= username,
        password=password,
        port= port
    )
    print("Connected successfully 🚀 (credentials loaded securely)")
    print("Success! Connected to the server-- Script by Abhas101")
except paramiko.AuthenticationException:
    print("Auth failed: check your username and pass")
except paramiko.SSHException as e:
    print(f"connection failed:{e}")
    exit()

# ===== Open Interactive Shell =====
shell = ssh.invoke_shell()
time.sleep(1)

# Disable paging
shell.send("terminal length 0\n")
time.sleep(1)

# Send command
shell.send("conn nxos\n")
time.sleep(2)

shell.send("show interface brief\n")
time.sleep(2)

# Read output
output = shell.recv(65535).decode()
print(output)

ssh.close()
