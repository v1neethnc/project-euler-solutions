# Project Euler Solutions
# Problem 099: Largest exponential
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 11:56, 04 June 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import log

max_val, line_no = 0, 0
with open("../inputs/099_input") as file_data:
	ln_no = 0
	for line in file_data.readlines():
		ln_no += 1
		line = line.split(",")
		line = [int(i.strip()) for i in line]
		res = line[1] * log(line[0])
		if res > max_val:
			max_val, line_no = res, ln_no
print(line_no)
