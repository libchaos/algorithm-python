#!/usr/bin/env python
#coding: utf-8

from collections import deque

def yanghui(k):
	#0 -> 1 -> 2-> ...-> k
	q = deque([1])

	for i in xrange(k):
		for _ in xrange(i):
			q.append(q.popleft() + q[0])

		q.append(1)
	return list(q)

print yanghui(4)