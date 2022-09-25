# Project Euler Solutions
# Problem 059: XOR decryption
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 00:39, 18 March 2020
# https://github.com/v1neethnc/project-euler-solutions

from statistics import mode

inp_str = open('../inputs/059_input').read().split(',')
inp_str = [int(i) for i in inp_str]
lsts = []
for i in range(0,3):
	lst = []
	for j in range(i, len(inp_str), 3):
		lst.append(inp_str[j])
	lsts.append(lst)

freqs = [mode(i) for i in lsts]
key = [i ^ 32 for i in freqs]
res = sum([inp_str[i] ^ key[i%3] for i in range(0, len(inp_str))])
print(res)
