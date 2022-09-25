# Project Euler Solutions
# Problem 187: Semiprimes
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 18:36, 29 October 2020
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
	prime[0], prime[1] = False, False
	return prime

n = 10**8
prime = SieveOfEratosthenes(n//2+1)
prime_lst = [i for i in range(len(prime)) if prime[i] == True]
ctr, i = 0, 0
while prime_lst[i] <= int(sqrt(n)) + 1:
	j = i
	while j < len(prime_lst) and prime_lst[i] * prime_lst[j] <= n:
		ctr += 1
		j += 1
	i += 1
print(ctr)
