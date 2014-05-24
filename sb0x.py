#!/usr/bin/env python2.7
"""
sb0x.py - Main shell

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1

"""
from core.tests import tests, init
tests = tests()
tests.test_python_version()
init()
tests.test_for_output()
import sys
import os
from core.main import *
import api.auto
import api.std

"""
This CODE Use sb0x-project API this is short and Simple.
Some Functions you Can Find in the std.py Module

if Not Read the API Tutorial:
https://github.com/levi0x0/sb0x-project/wiki/API 
"""
class sb0x_shell(object):
		"""sb0x shell"""
		def __init__(self):
			self.prompt = "\033[01;35mMain => \033[00m"

		def run(self):
			notify("  \t\tType 'help' or '?' for help")
			while True:
				options_array = options_array_system
				api.auto.sb0x_complete(options_array)
				self.run = raw_input(self.prompt)
				if self.run == "load":
					try:
						load()
					except Exception as e:
						error(sys.exc_info()[0])
						error(e.message)
				elif self.run == "banner":
					header()
				elif self.run == "exit" or self.run == "q":
					api.std.quit(0)
				elif self.run == "help" or self.run == "?":
					help();
				else:
					notify("[*] X: %s" % (self.run))
					os.system(self.run)


"""
The Main Fucntion Init the Code
"""
def main():
	start = sb0x_shell()
	start.run()


"""
The While loop is For The Exception
"""
if __name__ == '__main__':
	while True:
		try:
			LOOP_COUNT += 1
			if LOOP_COUNT == 1:
				api.std.cles()
				header()
			main()
		except KeyboardInterrupt:
			notify("\ntype 'q' to quit")
		except EOFError:
			notify("Ctrl + D Pressed")
			api.std.quit(0)
