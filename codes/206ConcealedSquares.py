# Project Euler Solutions
# Problem 206: Concealed Square
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 19:19, 18 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt, floor, ceil

def pattern_check(x):
	pattern_nms = '1_2_3_4_5_6_7_8_900'
	res_str = str(x)
	if res_str[-3:] == '900':
		for i in range(0, len(res_str), 2):
			if res_str[i] != pattern_nms[i]:
				return False
		return True if floor(sqrt(x)) == ceil(sqrt(x)) else False
	return False

i = floor(sqrt(1929394959697989900))
while i % 100 not in [30,70]:
	i-= 1
while not pattern_check(i * i):
	i = i - 40 if i % 100 == 70 else i - 30
print(i)
