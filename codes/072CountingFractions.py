# Project Euler Solutions
# Problem 072: Counting fractions
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 15:08, 24 October 2020
# https://github.com/v1neethnc/project-euler-solutions

from math import pow, sqrt
def SieveOfEratosthenes(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	return prime

def primeFactors(n): 
	factor_dict = {}
	d = 2
	while n % 2 == 0:
		if d not in factor_dict.keys():
			factor_dict[d] = 0 
		factor_dict[d] += 1
		n = n / 2
	for i in range(3,int(sqrt(n))+1,2): 
		while n % i== 0:
			if i not in factor_dict.keys():
				factor_dict[i] = 0
			factor_dict[i] += 1
			n = n // i
		if n == 1:
			break
	if n > 2:
		factor_dict[n] = 1
	factor_dict = {int(i):factor_dict[i] for i in factor_dict.keys()}
	return factor_dict

def totientCalc(num, factors_dict):
	res = 1
	for i in factors_dict.keys():
		tmp = (i ** (factors_dict[i] - 1)) * (i - 1)
		res *= tmp
	return res
sm = 0
primes = SieveOfEratosthenes(1000000)
for d in range(2, 1000001):
	# print(n)'
	if not primes[d]:
		val = primeFactors(d)
		tot_res = totientCalc(d, val)
	else:
		tot_res = d-1
	sm += tot_res
print(sm)
