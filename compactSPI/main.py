#!/usr/bin/env python3

from asyncio import *
from functools import wraps
import signal

from network import *
from utils import *
#from serial import *
import sys
import time

loop = get_event_loop()
save_handler = loop.call_soon(lambda: None)

def on_interrupt():
	print("Interrupted!\n")
	for task in Task.all_tasks():
		task.cancel()
	loop.stop()

if __name__ == '__main__':

	loop.add_signal_handler(signal.SIGINT, on_interrupt)
	loop.add_signal_handler(signal.SIGTERM, on_interrupt)
	loop.add_signal_handler(signal.SIGQUIT, on_interrupt)
	
	print_message()	

	sock = create_tcp_socket()	
	binding_tcp_socket(sock)
	listening_tcp_socket(sock)

	connection = accepting_new_connection(sock)

	string_data = receive_data_from_client(connection)
	handler_receive_data(string_data)
	print(string_data)			


