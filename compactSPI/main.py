#!/usr/bin/env python3

from network import *
from utils import *
#from serial import *
import sys

if __name__ == '__main__':

	print_message()
	try:	
		sock = create_tcp_socket()
		binding_tcp_socket(sock)
		listening_tcp_socket(sock)
		connection = accepting_new_connection(sock)

		while True:
			receive_data_from_client(connection)
			print("Back to main...\n")

	except KeyboardInterrupt:	
		print("Exiting the program...\n")
		pass

