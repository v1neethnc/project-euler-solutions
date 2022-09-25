# Project Euler Solutions
# Problem 035: Circular primes
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 12:00, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

def rotations(x):
	res = [x]
	tmp = str(x)
	while True:
		tmp = tmp[1:] + tmp[0]
		if int(tmp) == x:
			return res
		res.append(int(tmp))
		
checked = [2]
for i in range(3, 1000000, 2):
	rots = rotations(i)
	if i not in checked:
		flag = 0
		for j in rots:
			if not check(j):
				flag = 1
				break
		if flag == 0:
			checked.extend(rots)
print(len(checked))
