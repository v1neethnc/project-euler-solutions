# Project Euler Solutions
# Problem 053: Combinatoric selections
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 02:13, 16 March 2020
# https://github.com/v1neethnc/project-euler-solutions

def factorial(x):
	fact = 1
	for i in range(1, x+1):
		fact = fact * i
	return fact

def combination_val(n, r):
	return factorial(n) / (factorial(r) * factorial(n-r))

ctr = 0
for n in range(1, 101):
	res_lst = set()
	for r in range(1, n//2 + 1):
		if combination_val(n, r) > 1000000:
			res_lst.add(r)
			res_lst.add(n-r)
	ctr = ctr + len(res_lst)
print(ctr)
