import socket

FORMAT = "utf-8"
DISCONNECT_MESSAGE = "Disconnected"
HEADER = 64
PORT = 5041
SERVER = ""
host_name = socket.gethostname()
SERVER = socket.gethostbyname(host_name)
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)

	# Adding the to the first packet so that it fits 64 bytes 
	send_length = send_length+b' '*(HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

def receive():
	#Blocking code 
	print("Waiting for a message...")
	msg_length = client.recv(HEADER).decode(FORMAT)

	if msg_length:
		msg_length = int(msg_length)
		msg = client.recv(msg_length).decode(FORMAT)

		print(f"Message from server: {msg}")

operation = "receive"
if operation == "send":
	send("Hello from sublime")
	send(DISCONNECT_MESSAGE)
elif operation == "receive":
	receive()