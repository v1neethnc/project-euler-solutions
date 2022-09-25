# Project Euler Solutions
# Problem 054: Poker hands
# Copyright (c) v1neethnc. All Rights Reserved.
# Solution timestamp: 16:27, 20 October 2020
# https://github.com/v1neethnc/project-euler-solutions

# Compare the max rank hand and send the list of indices in descending order (rank, maxrankhand, list of indices)

def cards_rank(cards):
	nums = [i[0] for i in cards]
	suits = [i[1] for i in cards]
	vals = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	indexes = [vals.index(i) for i in nums]
	indexes.sort(reverse = True)
	uniq_nums = list(set(nums))
	# Royal flush
	if set(nums).issubset(set(vals[-5:])) and len(set(suits)) == 1:
		return (1, max(indexes), indexes)
	# Straight flush
	elif sum(indexes) == 5*indexes[2] and len(set(suits)) == 1:
		return (2, max(indexes), indexes)
	else:
		if len(uniq_nums) == 2:
			crd1_ct, crd2_ct = nums.count(uniq_nums[0]), nums.count(uniq_nums[1])
			# Four of a kind 
			if crd1_ct == 4 or crd2_ct == 4:
				max_val_crd = uniq_nums[0] if crd1_ct == 4 else uniq_nums[1]
				return (3, max_val_crd, indexes)
			# Full house
			else:
				max_val_crd = uniq_nums[0] if crd1_ct == 3 else uniq_nums[1]
				return (4, max_val_crd, indexes)
		# Flush
		if len(set(suits)) == 1:
			return (5, max(indexes), indexes)
		# Straight
		if indexes == list(range(max(indexes), min(indexes)-1, -1)):
			return (6, max(indexes), indexes)
		# Three of a kind
		if 3 in [nums.count(i) for i in set(nums)]:
			max_val_crd = [i for i in set(nums) if nums.count(i) == 3]
			return (7, vals.index(max_val_crd[0]), indexes)
		# Two pairs
		if [nums.count(i) for i in set(nums)].count(2) == 2:
			max_val_crd = max([i for i in set(nums) if nums.count(i) == 2])
			return (8, vals.index(max_val_crd), indexes)
		# One pair
		if [nums.count(i) for i in set(nums)].count(2) == 1:
			max_val_crd = [i for i in set(nums) if nums.count(i) == 2]
			return (9, vals.index(max_val_crd[0]), indexes)
		# High card
		return (10, max(indexes), indexes)


p1_wins, p2_wins, rno = 0, 0, 0
p1_rows, p2_rows = [], []
ctr1, ctr2 = 0, 0
for i in open("../inputs/054_input").readlines():
	i = i.replace("\n", "")
	cards = i.split(" ")
	player1, player2 = cards[0:5], cards[5:]
	res1, res2 = cards_rank(player1), cards_rank(player2)
	# If player 1 hand rank is better than player 2 hand rank
	if res1[0] < res2[0]:
		p1_wins += 1
	# If player 2 hand rank is better than player 1 hand rank
	elif res1[0] > res2[0]:
		p2_wins += 1
	# If rank is same
	else:
		# Compare maximum rank cards
		if res1[1] > res2[1]:
			p1_wins += 1
		elif res1[1] < res2[1]:
			p2_wins += 1
		else:
			# Compare cards in descending order
			for i in range(0, 5):
				if res1[2][i] > res2[2][i]:
					p1_wins += 1
					break
				elif res1[2][i] < res2[2][i]:
					p2_wins += 1
					break
print(p1_wins)
