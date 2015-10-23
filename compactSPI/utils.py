#!/usr/bin/env python3

import sys

def print_message():

	print("\t# Project CompactSPI #\n")	
	
def handler_receive_data(string_data):

	print("Treating receveid string data: '" + str(string_data))


	length = len(string_data)
	integer_data = []
	
	print("Converting string data to integers...\n")
	for i in range(length):
		integer_data.append(ord(string_data[i]))       
	     
	check    = integer_data[0]
	addressA = integer_data[1]
	command  = integer_data[2]
	
	print("Cheguei no fim da função handler\n")




