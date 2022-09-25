# Project Euler Solutions
# Problem 024: Lexicographic permutations
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 14:39, 20 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# Function to calculate factorial.
# For a n digit number, the number of permutations are n!
# Since the numbers are in lexicographic order, and since we need to find out the 1 millionth
# value, we can simply use a counter to indicate the number of possible values that are present 
# with the current length of strings.

def fact(x):
	if x==1:
		return x
	return x*fact(x-1)

permutate = 999999
st = ""
x = [0,1,2,3,4,5,6,7,8,9]
m = [0,0,0,0,0,0,0,0,0,0]
n = len(x)
for i in range(1,10):
	y = fact(10-i)
	j = permutate//y
	permutate = permutate%y
	st = st+str(x[j])
	x.remove(x[j])
	if permutate==0:
		break
if len(x)>0:
	st = st+str(x[0])
print(st)
