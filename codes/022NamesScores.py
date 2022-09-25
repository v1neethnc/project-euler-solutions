# Project Euler Solutions
# Problem 022: Names scores
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 18:20, 11 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# Perform preprocessing on the list by replacing the punctuations and creating a list of names.
# After preprocessing, sort the list in ascending/lexicographic order to generate the proper ranks.
# Next, iterate through each name and use their ASCII value to find out the score of each letter.
# Use this score to calculate rank weighted score and update the sum variable with each name.

fp = open('../inputs/022_input','r')
data = fp.read()
xp = data.replace('"','')
names = xp.split(',')
names.sort()
ans = 0
n = 1
for i in names:
	s = 0
	for j in range(0,len(i)):
		x = ord(i[j])
		s = s+x-64
	s = s*n
	n = n+1
	ans = ans+s
print(ans)
