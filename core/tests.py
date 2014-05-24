"""
tests.py - tests

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1

"""

"""
XXX:  Please write in this module in Python 3 syntax
"""
import sys 
import platform
import os
from time import sleep

class tests(object):
	"""testing user OS"""
	def __init__(self):
		self.home = os.getcwd()
		self.outputdir = "%s/output" % (self.home)
	#================================#
	#[1] test python version function for python 2.7
	#================================#
	def test_python_version(self):
		if sys.version_info.major > 2:
			print("\033[01;31m[ERROR] you Cant run sb0x with python 3 install python 2.7\033[00m")
			sys.exit()
		else:
			pass
	#end 1
	
	#=========================#
	#[2]testing os for linux               
	#==========================
	def is_linux():
		if platform.system == "Linux":
			return True
		elif sys.platform == "linux2" or sys.platform == "linux": 
			return True
		else:
			return False
		#end 2
	#=======================#
	#[3] Testing os for Mac "
	#=======================#
	def is_mac(self):
		if sys.platform == "mac" or sys.platform == "darwin":
			return True
		else:
			return False
	#end 3
	#=======================#
	#[4]Testin os for Windows"
	#=======================#
	def is_windows(self):
		if sys.platform == "win32" or "win" in sys.platform:
			return True
		else:
			return False
		#end 4
	#========================#
	#test for output dir#
	#=======================#
	def test_for_output(self):
		if not os.path.exists(self.outputdir):
			print("\033[01;31msb0x-project First time USE.\033[00m")
			print("[DEBUG] sb0x-project Path: %s" %(self.home))
			sleep(2)
			licnese = open("%s/doc/LICENSE" %(self.home)).read()
			print("\033[01;32m%s\033[00m" % (licnese))
			print("\n\033[01;34mThis software was created for educational purposes ONLY!\033[00m\n")
			print("\033[01;34mnew user Please Watch the Video tutorial:\nhttps://github.com/levi0x0/sb0x-project/wiki/VideoTutorial\n")
			print("* Please report bugs Github.com/levi0x0/sb0x-project/issues")
			print("* if you  like the project Please star us on Github.com/levi0x0/sb0x-project (i'ts free (:)")
			try:
				print("That's it! You are ready to GO.\n\033[00m\n")
				ask = raw_input("Do you agree? (y/N):")
				if ask == "y" or ask == "Y" or ask == "yes":
					if "sb0x" in self.outputdir:
						os.mkdir(self.outputdir)
					else:
						print("[ERROR] Path: %s is not sb0x-project path" %(self.outputdir))
				else:
					sys.exit()
			except Exception as e:
				print(e.message)
				print("Interrupt")
		else:
			pass

def init():
	test = tests()
	if (test.is_windows == True):
		print("No Windows here! (:")
		print("The current sb0x version is not support Windows")
		sys.exit()
	else:
		pass
