"""
auto.py - API standart

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: GPL 3

Description:
	Basic functions

"""
from os import getcwd as home
import random
import string

#global config
SB0X_VERSION = "2.0.1rc3"
SB0X_RELEASE_CODE_NAME = "Dex"
SB0X_PLATFROM = "linux"
SB0X_AUTHOR = "Levi Nachamni (levi0x0)"
SB0X_LICENSE = "GPL 3"
SB0X_CURRENT_MAINTAINER = "Levi Nachamni (levi0x0)"

"""
FIXEME: More nice API (:
KISS - Keep it Simple S**D
"""

def error(message):
		print "\033[01;31m[ERROR] %s\033[00m" % (message)


def warning(message):
		print "\033[01;33m[WARNING] %s\033[00m" % (message)

def notify(message):
		print "\033[01;34m%s\033[00m" % (message)

def debug(message):
		print "[DEBUG] %s" % (message)

def quit(code):
	notify("[*] Bye bye!")
	exit(code)

LOOP_COUNT = 0

"""
This API function will clear the screen
"""
def cles():
	print("\033[H\033[J")


"""
random_string - the function will create random string
"""
def random_string(length):
   	return ''.join(random.choice(string.lowercase) for i in range(length))

#the current path
home = home()
