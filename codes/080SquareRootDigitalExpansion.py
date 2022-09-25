# Project Euler Solutions
# Problem 080: Square root digital expansion
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 21:26, 24 October 2020
# https://github.com/v1neethnc/project-euler-solutions

import decimal
from math import sqrt
res = 0
squs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in range(1, 101):
	if i not in squs:
		dval = decimal.Decimal(i)
		dot100 = decimal.Context(prec=103)
		val = [int(i) for i in str(dval.sqrt(dot100)) if i != '.']
		res += sum(val[:100]) 
print(res)
