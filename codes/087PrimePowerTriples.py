# Project Euler Solutions
# Problem 087: Prime power triples
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:32, 25 October 2020
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
vals = int(sqrt(50000000)) + 1
primes = SieveOfEratosthenes(vals)
primes = [i for i in range(0, len(primes)) if primes[i] == True]
cb_lim_ind, qu_lim_ind = 0, 0
cb_flag, qu_flag = False, False
for i in primes:
	if not cb_flag and i > 50000000 ** (1/3):
		cb_flag, cb_lim_ind = True, primes.index(i)
	elif not qu_flag and i > 50000000 ** (1/4):
		qu_flag, qu_lim_ind = True, primes.index(i)
vals_set = set()
for i in range(0, len(primes)):
	for j in range(0, cb_lim_ind):
		for k in range(0, qu_lim_ind):
			v1, v2, v3 = primes[i], primes[j], primes[k]
			res = (v1*v1) + (v2*v2*v2) + (v3*v3*v3*v3)
			if res >= 50000000:
				break
			elif res not in vals_set:
				vals_set.add(res)
print(len(vals_set))
