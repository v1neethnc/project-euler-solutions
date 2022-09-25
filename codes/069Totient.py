# Project Euler Solutions
# Problem 069: Totient maximum
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 20:40, 09 June 2017
# https://github.com/v1neethnc/project-euler-solutions

import math
def checkprime(x):
	for i in range(2,x):
		if x%i==0:
			return False
	return True
res = 2
i = 3
while res*i<1000000:
	if checkprime(i):
		res =  res*i
	i = i+1
print(res)
