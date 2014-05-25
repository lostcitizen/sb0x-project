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

#global config
SB0X_VERSION = "2.0.1rc"
SB0X_RELEASE_CODE_NAME = "Dex"
SB0X_PLATFROM = "linux"
SB0X_AUTHOR = "Levi Nachamni (levi0x0)"
SB0X_LICENSE = "GPL 3"
SB0X_CURRENT_MAINTAINER = "Levi Nachamni (levi0x0)"

"""
FIXEME: More nice API (:
KISS - Keep it Simple S**D
"""


MOT="clean, simple, lightweight."

logo = """
		     __        _      ___       
		 ____\ \   ___| |__  / _ \__  __
		|_____\ \ / __| '_ \| | | \ \/ /
		|_____/ / \__ \ |_) | |_| |>  < 
		     /_/  |___/_.__/ \___//_/\_\ %s
			%s
""" % (SB0X_VERSION, MOT)

def header():
	print "\033[01;32m"
	print "\t\t+-----------------------------------+"
	print logo
	print "\t\t+-----------------------------------+\n"

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


#the current path
home = home()
