#euler 54

def all_same_suit(cards):
	suit = cards[0][1]
	for c in cards:
		if c[1] != suit:
			return False
	return True

def sort_by_value(cards):
	output = []
	for c in cards:
		if c[0] == '2':
			output.append(c)
	for c in cards:
		if c[0] == '3':
			output.append(c)
	for c in cards:
		if c[0] == '4':
			output.append(c)
	for c in cards:
		if c[0] == '5':
			output.append(c)
	for c in cards:
		if c[0] == '6':
			output.append(c)
	for c in cards:
		if c[0] == '7':
			output.append(c)
	for c in cards:
		if c[0] == '8':
			output.append(c)
	for c in cards:
		if c[0] == '9':
			output.append(c)
	for c in cards:
		if c[0] == 'T':
			output.append(c)
	for c in cards:
		if c[0] == 'J':
			output.append(c)
	for c in cards:
		if c[0] == 'Q':
			output.append(c)
	for c in cards:
		if c[0] == 'K':
			output.append(c)
	for c in cards:
		if c[0] == 'A':
			output.append(c)
	
	return output	

def highest_card_score(cards):
	sorted_cards = sort_by_value(cards)
	
	cards_length = len(cards)
	last_card = sorted_cards[cards_length - 1]
	if len(last_card) != 1:
		high_card = sorted_cards[cards_length - 1][0]
	else:
		high_card = last_card
		
	
	if high_card.isdigit():
		return int(high_card)
	elif high_card == 'T':
		return 10
	elif high_card == 'J':
		return 11
	elif high_card == 'Q':
		return 12
	elif high_card == 'K':
		return 13
	elif high_card == 'A':
		return 14
	else:
		print("high_card = " + high_card)
		exit()

def royal_flush(cards):
	high_val = None
	success = False
	
	if not all_same_suit(cards):
		success = False
	else:
		values = []
		for c in cards:
			values.append(c[0])
		values = sorted(values)
		if values == ['A', 'J', 'K', 'Q', 'T']:
			success = True
			high_val = 14
		
		
	return success, high_val

def straight_flush(cards):

	high_val = None
	success = False
	
	master_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	master_order_str = ''.join(master_order)
	
	values = []
	for c in cards:
		values.append(c[0])
			
	values_str = ''.join(sort_by_value(values))
	
	if values_str in master_order_str:
		success = True
		values_list = list(values_str)
		high_val = highest_card_score(values_list)

	return success, high_val

def flush(cards):
	high_val = None
	success = False
	
	if all_same_suit(cards):
		success = True
		high_val = highest_card_score(cards)

	return success, high_val

def four_of_a_kind(cards):
	success = False
	high_val = None
	
	value_counts = {}
	seen = []
	values = []
	for c in cards:
		values.append(c[0])
	for v in values:
		if v not in seen:
			seen.append(v)
			value_counts[v] = values.count(v)
			
	for key, value in value_counts.items():
		if value == 4:
			success = True
			if key.isdigit():
				high_val = int(key)
			elif key == 'T':
				high_val = 10
			elif key == 'J':
				high_val = 11
			elif key == 'Q':
				high_val = 12
			elif key == 'K':
				high_val = 13
			elif key == 'A':
				high_val = 14
			
	return success, high_val
			
def three_of_a_kind(cards):
	success = False
	high_val = None
	
	value_counts = {}
	seen = []
	values = []
	for c in cards:
		values.append(c[0])
	for v in values:
		if v not in seen:
			seen.append(v)
			value_counts[v] = values.count(v)
			
	for key, value in value_counts.items():
		if value == 3:
			success = True
			
			if key.isdigit():
				high_val = int(key)
			elif key == 'T':
				high_val = 10
			elif key == 'J':
				high_val = 11
			elif key == 'Q':
				high_val = 12
			elif key == 'K':
				high_val = 13
			elif key == 'A':
				high_val = 14
			
	return success, high_val

def one_pair(cards):
	success = False
	high_val = None
	
	value_counts = {}
	seen = []
	values = []
	pair_count = 0
	for c in cards:
		values.append(c[0])
	for v in values:
		if v not in seen:
			seen.append(v)
			value_counts[v] = values.count(v)
			
	for key, value in value_counts.items():
		if value == 2:
			pair_count += 1
	
	if pair_count == 1:
		success = True
		for key, value in value_counts.items():
			if value == 2:
				if key.isdigit():
					high_val = int(key)
				elif key == 'T':
					high_val = 10
				elif key == 'J':
					high_val = 11
				elif key == 'Q':
					high_val = 12
				elif key == 'K':
					high_val = 13
				elif key == 'A':
					high_val = 14
	
	
	return success, high_val
	
def two_pairs(cards):
	success = False
	high_val = None
	
	value_counts = {}
	seen = []
	values = []
	pair_count = 0
	for c in cards:
		values.append(c[0])
	for v in values:
		if v not in seen:
			seen.append(v)
			value_counts[v] = values.count(v)
			
	for key, value in value_counts.items():
		if value == 2:
			pair_count += 1
	
	if pair_count == 2:
		success = True
		high_val = highest_card_score(values)	
		
	return success, high_val

def straight(cards):
	success = False
	high_val = None
	
	
	master_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	master_order_str = ''.join(master_order)
	
	values = []
	for c in cards:
		values.append(c[0])
			
	values_str = ''.join(sort_by_value(values))

	if values_str in master_order_str:
		success = True
		high_val = highest_card_score(values)
		
	return success, high_val

def full_house(cards):
	success = False
	high_val = None
	
	high_val_1 = None
	success_1 = False
	high_val_2 = None
	success_2 = False
	
	success_1, high_val_1 = three_of_a_kind(cards)
	success_2, high_val_2 = one_pair(cards)
	
	if success_1 and success_2:
		success = True
		high_val = max(high_val_1, high_val_2)
		
	return success, high_val

def score(cards):
	
	total = 0
	result = False
	
	high_val = highest_card_score(cards)
	total += high_val

	
	result, value = one_pair(cards)	
	if result:
		#print("one pair")
		total += value * 10
		
	result, value = two_pairs(cards)	
	if result:
		#print("two pair")
		total += value * 100
		
	result, value = three_of_a_kind(cards)	
	if result:
		#print("three of a kind")
		total += value * 1000
		
	result, value = straight(cards)	
	if result:
		#print("straight")
		total += value * 10000
		
	result, value = flush(cards)	
	if result:
		#print("flush")
		total += value * 100000
		
	result, value = full_house(cards)	
	if result:
		#print("full house")
		total += value * 1000000
		
	result, value = four_of_a_kind(cards)	
	if result:
		#print("four of a kind")
		total += value * 10000000
		
	result, value = straight_flush(cards)	
	if result:
		#print("straight flush")
		total += value * 100000000
		
	result, value = royal_flush(cards)	
	if result:
		#print("royal flush")
		total += value * 1000000000
		
	return total							
	
def decide_winner(p1_cards, p2_cards):
	#returns 1 or player 1 and 2 for player 2
	
	p1_score = score(p1_cards)
	p2_score = score(p2_cards)
	
	if p1_score > p2_score:
		#print("p1: " + str(p1_score))
		#print("p2: " + str(p2_score))
		return 1
	elif p2_score > p1_score:
		#print("p1: " + str(p1_score))
		#print("p2: " + str(p2_score))
		return 2
	else:
		print("Tie")
		exit()

#PROCESS CARDS

f = open("p054_poker.txt")
lines = f.readlines()
f.close()

p1_hands = []
p2_hands = []

for line in lines:
	cards = line.split()
	
	p1_hand = []
	p2_hand = []
	
	i = 0
	while i < 10:
		if i < 5:
			p1_hand.append(cards[i])
		else:
			p2_hand.append(cards[i])
		i += 1
		
	p1_hands.append(p1_hand)
	p2_hands.append(p2_hand)
	
#BEGIN COMPARISONS

k = 0
p1_total = 0

while k < len(p1_hands):
	#print("p1_hands[k]: " + str(p1_hands[k]))
	#print("p2_hands[k]: " + str(p2_hands[k]))
	winner = decide_winner(p1_hands[k], p2_hands[k])
	#print(winner)
	#input()
	
	if winner == 1:
		p1_total += 1
	
	k += 1
	
print("Player 1 won " + str(p1_total) + " rounds.")