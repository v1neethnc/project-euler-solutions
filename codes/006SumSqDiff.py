# Project Euler Solutions
# Problem 006: Sum square difference
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 15:15, 21 June 2015
# https://github.com/v1neethnc/project-euler-solutions

# This can be done directly using the sum of squares formula and 
# the square of sum of n numbers formula.

n = (100*(100+1)*(2*100+1)//6)
n1 = (100*101//2)**2
print(n1-n)
