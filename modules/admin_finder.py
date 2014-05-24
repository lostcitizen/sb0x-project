"""
admin_finder.py - A simple Admin Finder module

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	A Simple Admin Finder Module

Established on code of Guy Mizrahi"
"""
import urllib2
import sys
from api.std import *

MODULE_NAME = "Admin Finder"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "A Simple Admin Finder Module"

os_slash = "/"
	
def admin_finder(target, lst):

	try:
		toGo = "%s/%s" % (target, lst)
		urllib2.urlopen(toGo)
	
	except urllib2.HTTPError, e:
		if e.code != 404:
			print "[+] %s | %s" % (toGo, e.code)
			sys.exit()
		elif e.code == 404:
			print "[-] %s [404]" % (toGo)
	except urllib2.URLError, e:
		print "[+] %s | %s" % (toGo, e.code)
	else:
		print "[+] %s" % (toGo)

def main():
	try:
		target = raw_input("Target:")
		if not "://" in target:
			error("http:// requierd..")
		else:
			pass
		print "\nFile Type:"
		print "=> 1 - PHP"
		print "=> 2 - ASP"
		print "=> 3 - ASPX"
		ask = int(raw_input("=> "))
		print "Hit [ENTER] for Default"
		if ask == 1:
			lst = raw_input("Wordlist: (Default)") or "%s/api/txt%saf_php.lst" % (home, os_slash)
		elif ask == 2:
			lst = raw_input("WorldList: (Default)") or "%s/api/txt%saf_asp.lst" % (home, os_slash)
		elif ask == 3:
			lst = raw_input("WordList: (Default)") or "%s/api/txt%saf_aspx.lst" % (home, os_slash)
			
		lst = open(lst, 'rU').readlines()
	
		for lst in lst:
			admin_finder(target, lst.replace('\n', ''))
	except KeyboardInterrupt as e:
		print e.message
	except AttributeError:
		error("Connection failed or URL Error")
	except Exception as e:
		error(e.message)
