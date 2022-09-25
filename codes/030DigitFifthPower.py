# Project Euler Solutions
# Problem 030: Digit fifth powers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:49, 17 May 2017
# https://github.com/v1neethnc/project-euler-solutions

def fifthpower(x):
	num = str(x)
	su = 0
	for i in num:
		su += int(i) ** 5
	if x==su:
		return True
	else:
		return False

s = 0
for i in range(2,400000):
	if fifthpower(i):
		s = s+i
print(s)
