#!/usr/bin/env python
#coding: utf-8


def knapsack(t, w):
	n = len(w)
	s = []
	k = 0

	while s or k < n :
		while t > 0 and k < n:
			if t >= w[k]:
				s.append(k)
				t -= w[k]
			k += 1

		if t == 0:
			print s
		k = s.pop()
		t += w[k]
		k += 1


knapsack(9  , [1, 8, 4, 3, 5, 2])