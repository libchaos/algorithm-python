#!/usr/bin/env python
#coding: utf-8


LEFT = {'{', '[', '('}
RIGHT = {'}', ']', ')'}

def match(exp):
	s = []
	for c in exp:
		if c in LEFT:
			s.append(c)
		elif c in RIGHT:
			if not s:
				return False
			if not 1 <= ord(c) - ord(s[-1]) <=2:
				return False
			s.pop()
	return not s



print match('{}[{]()')
