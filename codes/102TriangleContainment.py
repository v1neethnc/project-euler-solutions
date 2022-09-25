# Project Euler Solutions
# Problem 102: Triangle containment
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:35, 24 October 2020
# https://github.com/v1neethnc/project-euler-solutions

def area_calc(p1, p2, p3):
	x1 = p1[0] - p3[0]
	y1 = p2[1] - p1[1]
	x2 = p1[0] - p2[0]
	y2 = p3[1] - p1[1]
	return 0.5 * abs((x1 * y1) - (x2 * y2))

res = 0
with open('../inputs/102_input') as fl:
	for i in fl.readlines():
		vals = list(map(int, i.strip().split(',')))
		p1 = (vals[0], vals[1])
		p2 = (vals[2], vals[3])
		p3 = (vals[4], vals[5])
		p4 = (0, 0)
		if area_calc(p1, p2, p4) + area_calc(p1, p3, p4) + area_calc(p2, p3, p4) == area_calc(p1, p2, p3):
			res += 1 
print(res)
