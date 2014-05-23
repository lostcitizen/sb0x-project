"""
auto.py - API autocomplete module

Author: Levi Nachamni (levi0x0)
Date: 20/05/2014
Version: 0.1
License: sb0x-license

Description:
	This module will autocomplete raw_input()
	The options_array argument:
		options_array['hello-world', 'ls', 'this-is-a-command']

	for more information:
		https://github.com/levi0x0/sb0x-project/wiki/api/auto.py

"""
import readline

class auto(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

def sb0x_complete(options_array):
			completer = auto(options_array)
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab:complete')
