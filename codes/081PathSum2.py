# Project Euler Solutions
# Problem 081: Path sum: two ways
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 22:32, 19 March 2020
# https://github.com/v1neethnc/project-euler-solutions

f = open("../inputs/081_input").readlines()
lst = []
for i in f:
	tmp = i.split(',')
	tmp = [int(i) for i in tmp]
	lst.append(tmp)

rows = len(lst) - 1
cols = len(lst[0]) - 1
for i in range(rows, -1, -1):
	for j in range(cols, -1, -1):
		if i < rows and j < cols:
			lst[i][j] += min(lst[i + 1][j], lst[i][j + 1])
		elif i < rows:
			lst[i][j] += lst[i+1][j]
		elif j < cols:
			lst[i][j] += lst[i][j+1]
print(lst[0][0])
