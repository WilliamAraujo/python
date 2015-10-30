#!/usr/bin/env python3

from network import *
from utils import *
#from serial import *
import sys
import time

if __name__ == '__main__':

	print_message()	

	sock = create_tcp_socket()	
	binding_tcp_socket(sock)
	listening_tcp_socket(sock)

	while True:
	
		connection = accepting_new_connection(sock)
		
		while True:
		
			ret = receive_data_from_client(connection)
			if (ret == False):
				connection.close()
				break
		


