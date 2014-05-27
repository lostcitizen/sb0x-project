"""
main.py - General config

Author: Levi Nachamni (levi0x0)
"""

import os 
import glob
import sys
import subprocess
from importlib import import_module
import logging
from api import auto #import auto-complate api module
from api.std import *#the standart API module


DEBUG = 0 #devel mode

"""
	The get modules function returns the modules name
	And split .py
	Remove __init__.py from the array
"""

def get_modules():
		try:
			os.chdir("%s/modules" %(home))
			mod_lst = glob.glob("*py")
			os.chdir(home)
			lst = []
			for module in mod_lst:
				if module == "__init__.py":
					pass
				else:
					lst.append(module.replace(".py", ""))
		except Exception as e:
			error(e.message)
			return(1)

		return lst

def help():
	notify("Main Options:")
	notify("\thelp, ? - print help.")
	notify("\tload - load modules.")
	notify("\tCtrl + c - Back to main.")
	notify("\t- to start type 'load.'")

def help_load():
	notify("Load Options:")
	notify("\thelp, ? - print help.")
	notify("\tlist - Modules list, to load module type his name in the prompt.")
	notify("\tinfo - print module info autohr, version etc... Usage: info module_name")
	notify("\tCTRL + c - back to main (for exit)")
"""
The system auto-complate commands array
"""
options_array_system = ["ls", "quit", "clear", "pwd", "load", "help", "?"]

def dump_module_info(module):
	module = module.replace("info", "").strip()

	module_path = "modules.%s" % (module)
	info = import_module(module_path)
	print "\t=> Module Name: %s" %(info.MODULE_NAME)
	print "\t=> Module Author: %s" %(info.MODULE_AUTHOR)
 	print "\t=> Module Version: %s" %(info.MODULE_VERSION)
	print "\t=> Module License: %s" %(info.MODULE_LICENSE)
	print "\t=> Module Description: %s" %(info.MODULE_DESC)

def shell(execs):
	"""The sb0xExec shell"""
	if "cd" in execs:
		try:
			os.chdir(execs.replace("cd", "").strip())
		except Exception as e:
			pass
	else:
		notify("sh: %s" %(execs))
		subprocess.call(execs, shell=True)

def load():
	counter = 0
	while True:
		options_array_system = ['info', 'exit', 'list', 'load']
		counter += 1
		options_array = get_modules() + options_array_system
		auto.sb0x_complete(options_array)
		prompt = "\033[01;36m[%d] load => \033[00m" % (counter)
		run = raw_input(prompt)
		if not run:
			continue
		elif run == "list":
			counter2 = 0
			for module in get_modules():
				counter2 += 1
				notify("\t=> %d. %s" %(counter2, module))
			continue
		elif run == "help" or run == "?":
			help_load()
			continue
		elif run == "exit" or run == "q":
			quit(0)
		elif run == "clear":
			cles()
			continue
		elif "info" in run:
			try:
				dump_module_info(run)
                                continue
			except KeyError:
				error(sys.exc_info()[0])
				error(" info: Failed to dump info for: %s" %(run.replace("info", "")))
				continue
			except Exception as e:
				error(sys.exc_info()[0])
			        notify("Import error for: %s" % (run))
				continue
		elif run:
			os.chdir("%s" %(home))
			module_path = "modules.%s" % (run)

		try:
			init_module = import_module(module_path)
			"""
				Import module -
				The Module Must Contain main() function [REQUIERD]
				See the API tutorial in the Wiki:
				https://github.com/levi0x0/sb0x-project/wiki/API/
			"""
			init_module.main()
			continue
		except AttributeError as e:
			error(e.message)
			continue
		except Exception as e:
			print(e.message)
			continue
