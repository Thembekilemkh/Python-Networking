import socket
import threading

# We first gonna send a header message to the server that just simply tells us how much
# data to expect than adjust the recving bytes parameter accordingly

HEADER = 64
PORT = 55039
host_name = socket.gethostname()
SERVER = socket.gethostbyname(host_name)
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "Disconnected"
print("Socket connection from: ", SERVER)
print("host_name: ", host_name)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection, addr, type_):
	print(f"NEW CONNECTION {addr} connected." )
	connected = True
	while connected:
		# Number of bytes my G
		if type_ == "send":
			send("Hello from Madala's laptop", connection)
			connected = False
		elif type_ == "recieve":
			connected = recieve(connection, addr)
		'''
		#Blocking code 
		msg_length = connection.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = connection.recv(msg_length).decode(FORMAT)

			if msg == DISCONNECT_MESSAGE:
				connected = False
		connected = recieve(connection, addr)
		'''

	connection.close()

def start(type_):
	server.listen()
	while True:
		# Get the address of the client
		# Blocking code
		print(f"Listening on {SERVER}")
		conn, addr = server.accept()
		try:
			t = threading.Thread(target=handle_client, args=(conn, addr, type_)).start()
			print(f"Current active connections: {threading.activeCount() - 1}")
		except Exception as e:
			print("Something went wrong: ", e)
			conn.close()

def recieve(connection, addr):
	#Blocking code 
	msg_length = connection.recv(HEADER).decode(FORMAT)

	if msg_length:
		msg_length = int(msg_length)
		msg = connection.recv(msg_length).decode(FORMAT)

		if msg == DISCONNECT_MESSAGE:
			return False
	return True

def send(msg, connection):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)

	# Adding the to the first packet so that it fits 64 bytes 
	send_length = send_length+b' '*(HEADER - len(send_length))
	connection.send(send_length)
	connection.send(message)

operation = ["send", "receive"]
print("Starting server...")
start(operation[0])


	