# Project Euler Solutions
# Problem 017: Number letter counts
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 17:55, 11 June 2017
# https://github.com/v1neethnc/project-euler-solutions

# Creating lists of possible words that can show up in the numbers between 1 and 1000.
# After creating, first calculate the number of occurrences of words between 1 and 100.
# Next, calculate the number of numbers that contain the word "hundred."
# Next, add to the solution the combination of words from 1-100 and the word hundred.
# Finally, add the words "onethousand" to the result.

digs = ['one','two','three','four','five','six','seven','eight','nine']
hnd = 'hundredand'
tn = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

ans = 0
s = 0
for i in digs:
	s = s+9*len(i)
for i in tn:
	s = s+len(i)
for i in tens:
	s = s+10*len(i)
#hundred and
ans = ans+9*99*len(hnd)
# <insert> hundred
for i in digs:
	ans = ans+100*len(i)
#just the hundred
ans = ans+9*len('hundred')
#onethousand
ans = ans+10*s+len('onethousand')
print(ans)
