#euler63

#naive attempt

def num_dig(n):
	return len(list(str(n)))

base = 2
exp = 1
count = 1
while True:
	base_done = False
	while not base_done:
		
		result = base**exp
		digits = num_dig(result)
		
		#print(str(base) + "^" + str(exp) + " = " + str(result) + " has " + str(digits) + " digits")
		
		if exp == digits:
			print("Solution " + str(count) + ": " + str(base) + "^" + str(exp) + " = " + str(result) + " has " + str(digits) + " digits")
			count += 1
		elif base == 10 and exp == 1:
			print("Solution " + str(count) + ": " + str(base) + "^" + str(exp) + " = " + str(result) + " has " + str(digits) + " digits")
		elif base < 10:	
			if exp > digits:
				base += 1
				exp = 0
				base_done = True
		else:
			if exp < digits:
				base += 1
				exp = 0
				base_done = True
		
		exp += 1
		#input()