#euler 84

import random
import sys
from collections import Counter

def record_square(dict, space):
	if space not in dict:
		dict[space] = 1
	else:
		dict[space] += 1

board = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']

current_pos = 0
current_square = '00'

freqs = {}

CC = ['JAIL', 'GO', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER']
CH = ['GO', 'JAIL', '11', '24', '39', '05', 'NEXTR', 'NEXTR', 'NEXTU', 'BACK3', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER', 'OTHER']

random.shuffle(CC)
random.shuffle(CH)

cc_card = 0
ch_card = 0

d_count = 0

freqs[current_square] = 1
#print("Current square: " + str(current_square))
#input()

while True:
	
	#d1 = random.randint(1, 6)
	#d2 = random.randint(1, 6)
	
	d1 = random.randint(1, 4)
	d2 = random.randint(1, 4)
	
	if d1 == d2:
		d_count += 1
		
		if d_count == 3:
			
			d_count = 0
			#Go to jail
			current_pos = 10
			current_square = '10'
			
			#print("Go to jail")
			#print("Current square: " + str(current_square))
			#input()
			
			record_square(freqs, current_square)
			
	else:
		d_count = 0
	
		moves = d1 + d2

		#print("Rolled a " + str(moves))
	
		if (current_pos + moves) > 39:
			current_pos += moves
			current_pos -= 40
		else:
			current_pos += moves
		
		current_square = board[current_pos]
		#print("Current square: " + str(current_square))
		#input()
		
		if current_square != '30':
			record_square(freqs, current_square)
			
		
		#If player lands on go to jail
	
		if current_square == '30':
			current_pos = 10
			current_square = '10'
		
			#print("Go to jail")
			#print("Current square: " + str(current_square))
			#input()
		
			record_square(freqs, current_square)
			
		#If player lands on community chest
	
		elif current_square == '02' or current_square == '17' or current_square == '33':
		
			#print("Community chest")
			#print("Current square: " + str(current_square))
			#input()
		
			if cc_card == 16:
				cc_card = 0
		
			# Advance to GO
		
		
		
			if CC[cc_card] == 'GO':
				current_pos = 0
				current_square = '00'
			
			
				#print("Advance to GO - CC")
				#print("Current square: " + str(current_square))
				#input()
				record_square(freqs, current_square)
				
		
			# Go to jail
		
			elif CC[cc_card] == 'JAIL':
			
				current_pos = 10
				current_square = '10'
			
				#print("Go to jail")
				#print("Current square: " + str(current_square))
				#input()
			
			
				record_square(freqs, current_square)
				
				
			cc_card += 1
	
		#If player lands on chance
	
		elif current_square == '07' or current_square == '22' or current_square == '36':
		
			if ch_card == 16:
				ch_card = 0
		
			# Advance to GO
		
			if CH[ch_card] == 'GO':
				current_pos = 0
				current_square = '00'
			
				#print("Advance to GO - CH")
				#print("Current square: " + str(current_square))
				#input()
				
				record_square(freqs, current_square)
				
		
			# Go to jail
		
			elif CH[ch_card] == 'JAIL':
				current_pos = 10
				current_square = '10'
			
				#print("Go to jail")
				#print("Current square: " + str(current_square))
				#input()
			
				record_square(freqs, current_square)
				
		
			# Go to C1
		
			elif CH[ch_card] == '11':
				current_pos = 11
				current_square = '11'
			
				#print("Go to C1")
				#print("Current square: " + str(current_square))
				#input()
				
				record_square(freqs, current_square)
				
				
			# Go to E3
		
			elif CH[ch_card] == '24':
				current_pos = 24
				current_square = '24'
			
				#print("Go to E3")
				#print("Current square: " + str(current_square))
				#input()
			
				record_square(freqs, current_square)
				
			
			# Go to H2
		
			elif CH[ch_card] == '39':
				current_pos = 39
				current_square = '39'
			
				#print("Go to H2")
				#print("Current square: " + str(current_square))
				#input()
			
				record_square(freqs, current_square)
				
			
			# Go to R1
		
			elif CH[ch_card] == '05':
				current_pos = 5
				current_square = '05'
			
				#print("Go to R1")
				#print("Current square: " + str(current_square))
				#input()
			
				record_square(freqs, current_square)
				
		
			elif CH[ch_card] == 'NEXTR':
				if current_pos < 5:
					current_pos = 5
					current_square = '05'
				elif current_pos < 15:
					current_pos = 15
					current_square = '15'
				elif current_pos < 25:
					current_pos = 25
					current_square = '25'
				elif current_pos < 35:
					current_pos = 35
					current_square = '35'
				else:
					current_pos = 5
					current_square = '05'
			
				#print("Go to next station")
				#print("Current square: " + str(current_square))
				#input()
			
				record_square(freqs, current_square)
				
				
			elif CH[ch_card] == 'NEXTU':
				if current_pos < 12:
					current_pos = 12
					current_square = '12'
				elif current_pos < 28:
					current_pos = 28
					current_square = '28'
				else:
					current_pos = 12
					current_square = '12'
			
				#print("Go to next utility")
				#print("Current square: " + str(current_square))
				#input()
			
				if current_square not in freqs:
					freqs[current_square] = 1
				else:
					freqs[current_square] += 1
		
			elif CH[ch_card] == 'BACK3':
			
				current_pos -= 3
				current_square = board[current_pos]
			
				#print("Go back 3")
				#print("Current square: " + str(current_square))
				#input()
		
				record_square(freqs, current_square)
				
			
			ch_card += 1
			

	#print(output(freqs))
	#print(freqs)
	#input()
	
	c = Counter(freqs)
	
	mc = c.most_common(3)
	
	output_list = []
	
	for key, val in mc:
		output_list.append(key)
		
	output = ''.join(output_list)
	
	#print(freqs)
	#print(output)
	#input()
	
	sys.stdout.write("\r" + output)
	sys.stdout.flush()