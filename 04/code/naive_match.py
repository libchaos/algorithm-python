#!/usr/bin/env python
#coding: utf-8


def naive_match(patten_str, match_str):
    m, n = len(patten_str), len(match_str)
    i, j = 0, 0

    while i < m and j < n:
        if patten_str[i] == match_str[j]:
            i, j = i+1, j+1
        else:
            i, j = 0, j-i+1
    if i == m:
        return j-i
    return -1


    