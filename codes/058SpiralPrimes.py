# Project Euler Solutions
# Problem 058: Spiral primes
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 01:15, 18 March 2020
# https://github.com/v1neethnc/project-euler-solutions

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

diag_nos = [1]
non_pr_ct = 1
diff = 2
while True:
	num = diag_nos[-1]
	for i in range(0, 4):
		num += diff
		if not check(num):
			non_pr_ct += 1
		diag_nos.append(num)
	diff += 2
	if non_pr_ct/len(diag_nos) >= 0.9:
		break
print(diff - 1)
