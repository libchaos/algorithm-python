#!/usr/bin/env python
#coding: utf-8

# N = 5

# a, b, c, d, e = xrange(5)

# G = [[0] * N for _ in xrange(N)]

# G[a][b] = G[b][a] = 1

# def addEdge(G, v1, v2):
#     G[v1][v2] = G[v2][1] = 1

# addEdge(G, a, e)

# addEdge(G, b, e)
# addEdge(G, b, c)

# addEdge(G, c, d) 
# #a, b, c, d, e
# G2 = [{b, d}, {c, d, e}, {b, c, e}, {a, b, d}] #邻接表
# #带权邻接表
# G3 = [{b:4, e:2}]




G = [
    {1, 2, 3}, #0
    {0, 4, 6}, #1 
    {0, 3}, #2
    {0, 2, 4}, #3
    {1, 3, 5, 6}, #4
    {4, 7}, #5
    {1, 4}, #6
    {5}, #7
]

def dfs(G, v, visited=set()):
    print v
    visited.add(v)
    for u in G[v]:
        if u not in visited:
            dfs(G, u, visited)


dfs(G, 0)


def dfsIter(G, v):
    visited = set()
    s = [v]

    while s:
        u = s.pop()
        if u not in visited:
            print u
            visited.add(u)
            s.extend(G[u])

dfsIter(G, 0)