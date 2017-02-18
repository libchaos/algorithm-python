#!/usr/bin/env python
#coding: utf-8

operators = {
	'+': lambda op1, op2: op1 + op2,
	'-': lambda op1, op2: op1 - op2,
	'*': lambda op1, op2: op1 * op2,
	'/': lambda op1, op2: op1 / op2,
}


def evalPostfix(e):
	tokens = e.split()
	s = []

	for token in tokens:
		if token.isdigit():
			s.append(int(token))

		elif token in operators:
			f = operators[token]
			op2 = s.pop()
			op1 = s.pop()
			s.append(f(op1, op2))

	return s.pop()


print evalPostfix('2 3 4 * +')

