# Project Euler Solutions
# Problem 357: Prime generating integers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:51, 22 October 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import sqrt
def SieveOfEratosthenes(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	return prime

prime = SieveOfEratosthenes(150000000)
sm = 1
for i in range(2, 100000001, 4):
	if (i // 2) % 2 == 1 and prime[i+1]:
		flag = True
		j = 1
		root = int(sqrt(i)) + 1 
		while j <= root:
			if i % j == 0:
				if not (prime[j + i//j]):
					flag = False
					break
			j += 1
		if flag:
			sm += i
print(sm)
