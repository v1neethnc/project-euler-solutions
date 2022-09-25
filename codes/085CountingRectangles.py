# Project Euler Solutions
# Problem 085: Counting rectangles
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 00:17, 24 October 2020
# https://github.com/v1neethnc/project-euler-solutions

max_val, ar = 0, 0
for r in range(2, 95):
	for c in range(r, 95):
		rects = r * (r + 1) * c * (c + 1) // 4
		if rects < 2000000 and rects > max_val:
			max_val, ar, rt, ct = rects, r * c, r, c
print(ar)
