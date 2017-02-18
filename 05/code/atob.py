#!/usr/bin/env python
#coding: utf-8

from collections import deque

def atob(a, b):
	q = deque([(a, 0)])
	checked = {a}

	while True:
		s, c = q.popleft()
		if s == b:
			break
		if s < b:
			if s + 1 not in checked:
				q.append((s + 1, c + 1))
				checked.add(s + 1)
			if s * 2 not in checked:
				q.append((s * 2, c + 1))
				checked.add(s * 2)
		if s > 0:
			if s - 1 not in checked:
				q.append((s - 1, c + 1))
				checked.add(s - 1)
	return c 


print atob(5, 98)


