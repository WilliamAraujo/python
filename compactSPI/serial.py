#!/usr/bin/env python3

import time
import geniePi
import sys

PORT = '/dev/ttyAMA0'
BAUD_RATE = 115200

def opening_serial_communication():

	geniePi.genieSetup(PORT, BAUD_RATE)
	geniePi.genieWriteStr(0, 'Conexao Local')
	geniePi.genieWriteObj(0x0E, 0x00, 0x01)
	#time.sleep(1)
	geniePi.genieWriteStr(1, 'Pronto para operar!')
	
	while True:
		event = geniePi.genieReadObj(geniePi.GENIE_OBJ_WINBUTTON, 1)
		if event == 1:
			break
			
	#time.sleep(0.2)
	geniePi.genieWriteStr(2, 'Procurando Placas...')
	
	for i in range(1,5):
		devices = bus.scan(i)
		geniePi.genieWriteStr(i+2, str(devices))    

	geniePi.genieWriteStr(2, 'Placas encontradas!')
	
# Não entendo...
