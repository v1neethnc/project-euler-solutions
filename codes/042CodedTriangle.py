# Project Euler Solutions
# Problem 042: Coded triangle numbers
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 22:14, 09 May 2019
# https://github.com/v1neethnc/project-euler-solutions


def textSum(txt):
	sm = 0
	l = len(txt)
	for i in range(0, l):
		sm = sm + ord(txt[i]) - 64
	return sm

def isTriangle(nm, numLt):
	if nm in numLt:
		return True
	return False

f = open('../inputs/042_input', "r")
codes = f.read()
code_list = codes.split('"')
count = 0


for i in code_list:
	if i in ['', ',']:
		code_list.remove(i)

triNum = []
for i in range(1,100):
	triNum.append(i*(i+1)//2)
for i in code_list:
	cd_sm = textSum(i)
	if isTriangle(cd_sm, triNum):
		count = count + 1
print(count)
