import threading
import socket
from queue import Queue

target = "192.168.1.1"
que = Queue()
open_ports = []

def portscan(port):
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		return True
	except:
		return False

def fill_que(port_list):
	for i in range(port_list):
		que.put(i)

def worker():
	while not que.empty():
		port = que.get()
		if portscan(port):
			print(f"Port {port} open!!!!!!!!")
			open_ports.append(port)
		else:
			pass
			
port_to_scan = 65500
thread_list = []

fill_que(port_to_scan) 
for t in range(20):
	thread = threading.Thread(target=worker)
	thread_list.append(thread)

for thr in thread_list:
	thr.start()

for thread in thread_list:
	thread.join()


print("The open ports: ", open_ports)
with open("open_port.txt", "w") as f:
	f.write("Open ports on the tiny smart phone")

	for port in open_ports:
		f.write(str(port))