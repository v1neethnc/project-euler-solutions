# Project Euler Solutions
# Problem 031: Coin sums
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 19:07, 20 June 2017
# https://github.com/v1neethnc/project-euler-solutions

total_req = 200
res = [1] + [0]*total_req
coins = [1, 2, 5, 10, 20, 50, 100, 200]
for coin in coins:
	for i in range(coin, total_req+1):
		res[i] += res[i - coin]
print(res[total_req])

# for a in range(200,-1,-200):
# 	for b in range(a,-1,-100):
# 		for c in range(b,-1,-50):
# 			for d in range(c,-1,-20):
# 				for e in range(d,-1,-10):
# 					for f in range(e,-1,-5):
# 						for g in range(f,-1,-2):
# 							res = res+1
# print(res)	
