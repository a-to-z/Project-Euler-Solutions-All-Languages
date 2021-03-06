#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Project Euler Problem #2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

a = 0
b = 1
nextNum = a + b
limit = 4000000
sums = 0

while nextNum < 4000000:
	if nextNum % 2 == 0:
		sums += nextNum
	a = b
	b = nextNum
	nextNum = a + b

print sums #Answer = 4613731
