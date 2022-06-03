import getpass
import telnetlib

# Enter your host ip address
HOST = "192.168.1.10"
# Enter your host username
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Change for your env
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name VLAN_4\n")
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"sh run\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))