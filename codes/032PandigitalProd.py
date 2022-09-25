# Project Euler Solutions
# Problem 032: Pandigital products
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 19:28, 15 March 2020
# https://github.com/v1neethnc/project-euler-solutions

import itertools

def generate_pairs(x):
    res = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            if '0' not in str(i) and '0' not in str(x // i):
                res.append(set(str(i) + str(x // i)))
    return res

sm = 0
for nums in range(1000, 9999):
    num_set = set(str(nums))
    if len(num_set) == len(str(nums)) and '0' not in num_set:
        for i in generate_pairs(nums):
            if len(num_set.intersection(i)) == 0 and len(num_set.union(i)) == 9:
                sm = sm + nums
                break
print(sm)
