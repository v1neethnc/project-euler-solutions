# Project Euler Solutions
# Problem 062: Cubic permutations
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:41, 20 October 2020
# https://github.com/v1neethnc/project-euler-solutions

i = 27
# Dict to store sorted_list_of_cube: [min_num, count]
cubes_list = {}
while True:
	val = str(sorted(str(i**3)))
	if val not in cubes_list.keys():
		cubes_list[val] = [i, 1]
	else:
		cubes_list[val][1] += 1
		if cubes_list[val][1] == 5:
			print(cubes_list[val][0] ** 3)
			break
	i += 1
