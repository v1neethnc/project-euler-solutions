# Project Euler Solutions
# Problem 243: Resilience
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 00:22, 05 November 2020
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

primes = SieveOfEratosthenes(95000)
prime_lst = [i for i in range(2, len(primes)) if primes[i] == True]
res, ind, val = 1, 0, 1
threshold = 15499/94744
factors = {}
while res >= threshold and ind < len(prime_lst):
	factors[prime_lst[ind]] = 1
	val *= prime_lst[ind]
	tot_num = totientCalc(val, factors)
	res = (tot_num / (val - 1))
	ind += 1
val = val // prime_lst[ind - 1]
factors = {prime_lst[i]:1 for i in range(0, ind - 1)}
composites = [i for i in range(2, prime_lst[ind - 1]) if i not in prime_lst]
for i in composites:
	factors_composites = primeFactors(i)
	for j in factors_composites:
		factors[j] += factors_composites[j]
	num_val = val * i
	tot_num = totientCalc(val * i, factors)
	res = tot_num / ((val * i) - 1)
	if res < threshold:
		print(val*i)
		break
	for j in factors_composites:
		factors[j] -= factors_composites[j]
