#!/usr/bin/env python
#coding: utf-8

def initMaze():
	maze = [[0] * 7 for _ in xrange(5+2)]
	walls = [
		(1, 3), 
		(2, 1), (2, 5),
		(3, 3), (3, 4),
		(4, 2), #(4, 3),
		(5, 4),
	]

	for i in xrange(5 + 2):
		maze[i][0] = maze[i][-1] = 1
		maze[0][i] = maze[-1][i] = 1

	for i, j in walls:
		maze[i][j] = 1
	return maze

maze = initMaze()

def path(maze, start, end):
	i, j = start
	ei, ej = end

	s = [(i, j)]
	maze[i][j] = 1

	while s:
		i, j = s[-1]
		if (i, j) == (ei, ej):
			break

		for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
			if maze[i+di][j+dj] == 0:
				maze[i+di][j+dj] = 1
				s.append((i+di, j+dj))
				break
		else:
			s.pop()

	return s


maze = initMaze()
print path(maze, (1, 1), (5, 5))


