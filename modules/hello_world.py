"""
hello_world.py - A simple Module

Author: Levi Nachamni (levi0x0)
Date: 22/05/2014
Version: 0.1
License: GPL 3

Description:
	A Simple Hello World Module

"""

#import the standart sb0x API Modules
from api.std import *

MODULE_NAME = "Hello World"
MODULE_AUTHOR = "Levi Nachmani (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.1"
MODULE_DESC = "A Simple Hello World Module"

def hello_world():
	cles() #this API Function will clear the screen 
	notify("This is Hello World Module!")
	error("This is ERROR!")
	warning("This is Warning")

def main():
	"""
		initialize your code here
	"""
	hello_world()


"""
END OF THE CODE!
"""

