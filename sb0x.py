#!/usr/bin/env python2.7
"""
sb0x.py - Main shell

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1

"""

import sys
import optparse
import os
try:
    from core.tests import tests, init
    tests = tests()
    tests.test_python_version()
    init()
    tests.test_for_output()
except Exception as e:
    print("\033[01;31m[ERROR] %s\033[00m" %(e) )
    sys.exit(1)

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
					shell(self.run)


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
        parser = optparse.OptionParser(version=SB0X_VERSION)
        parser.parse_args()

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
                except Exception as e:
                    error(e.message)
                    api.std.quit(1)
