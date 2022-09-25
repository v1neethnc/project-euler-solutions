# Project Euler Solutions
# Problem 050: Consecutive prime sum
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 15:58, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

max_prim, final, i = 0, 0, 2
ls = []
while max_prim < 1000000:
	if check(i):
		ls.append(i)
		temp = sum(ls)
		j = 0
		while temp > max_prim:
			temp = temp - ls[j]
			if check(temp):
				max_prim = temp
				if max_prim < 1000000:
					final = max_prim
			j += 1
	i += 1
print(final)
