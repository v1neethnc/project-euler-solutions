# Project Euler Solutions
# Problem 124: Ordered radicals
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:29, 18 February 2021
# https://github.com/v1neethnc/project-euler-solutions

def SieveOfEratosthenes(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	return prime


prime_list = SieveOfEratosthenes(100000)
list_val = [[i, 1] for i in range(len(prime_list))]
list_val[1][1] = 1
for i in range(2, len(prime_list)):
	if prime_list[i] == True:
		tmp = i
		while tmp < len(prime_list):
			list_val[tmp][1] *= i
			tmp += i
list_val.remove([0, 1])
list_val.sort(key = lambda x: (x[1], x[0]))
print(list_val[9999][0]) 
