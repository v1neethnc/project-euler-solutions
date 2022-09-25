# Project Euler Solutions
# Problem 019: Counting Sundays
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 19:57, 17 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# There are ways like using Wang's Algorithm to calculate the day of the week,
# in this program I simply used the calendar package to generate calendars
# and check whether the first day of the month is a Sunday or not. 

import calendar

ctr = 0
for i in range(1901, 2001):
	for j in range(1, 13):
		if calendar.weekday(i, j, 1) == 6:
			ctr += 1
print(ctr)
