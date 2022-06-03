import getpass
import telnetlib

HOST = "switch1"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('myswitches')

for IP in f:
   IP=IP.strip()
   print ("Configuring Switch " + (IP))
   HOST = IP
   tn = telnetlib.Telnet(HOST)
   tn.read_until(b"Username: ")
   tn.write(user.encode('ascii') + b"\n")
   if password:
      tn.read_until(b"Password: ")
      tn.write(password.encode('ascii') + b"\n")
   tn.write(b"conf t\n")
   tn.write(b"vlan 2\n")
   tn.write(b"name VLAN_2\n")
   tn.write(b"exit\n")
   tn.write(b"vlan 3\n")
   tn.write(b"name VLAN_3\n")
   tn.write(b"exit\n")
   tn.write(b"vlan 4\n")
   tn.write(b"name VLAN_4\n")
   tn.write(b"end\n")
   tn.write(b"exit\n")
   print(tn.read_all().decode('ascii'))