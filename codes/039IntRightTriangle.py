# Project Euler Solutions
# Problem 039: Integer right triangles
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 12:41, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

def right_tr_check(sides):
	if sides[0] + sides[1] < sides[2]:
		return False 
	return True if sides[0] ** 2 + sides[1]**2 == sides[2]**2 else False

res, maxsol = 0, 0
for perimeter in range(4, 1001):
	ctr = 0
	for a in range(1, int(perimeter*0.33) + 1):
		for b in range(a+1, perimeter//2):
			sides = [a, b, perimeter-(a+b)]
			if right_tr_check(sides):
				ctr += 1
	if ctr > maxsol:
		maxsol, res = ctr, perimeter
print(res)
