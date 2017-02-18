#!/usr/bin/env python
#coding: utf-8


from collections import deque

def division(M, n):
	res = []
	q = deque(xrange(n))
	pre = n

	while q:
		cur = q.popleft()
		if pre >= cur:
			res.append([])

		for a in res[-1]:
			if M[cur][a]:
				q.append(cur)
				break
		else:
			res[-1].append(cur)
		pre = cur

	return res


N = 9

R = {
	(1, 4), (4, 8), (1, 8), (1, 7),
	(8, 3), (1, 0), (0, 5), (1, 5),
	(3, 4), (5, 6), (5, 2), (6, 2), (5, 4)
}

M = [[0] * N for _ in xrange(N)]
for i, j in R:
	M[i][j] = M[j][i] = 1

print division(M, N)