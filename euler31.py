#euler 31
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#How many different ways can £2 be made using any number of coins?

def total(c):
	return ((c[0] * 100) + (c[1] * 50) + (c[2] * 20) + (c[3] * 10) + (c[4] * 5) + (c[5] * 2) + (c[6] * 1))

result = 0

for a in range(0, 3):
	
	for b in range(0, 5):
	
		for c in range(0, 11):
			
			for d in range(0, 21):
			
				for e in range(0, 41):
					
					for f in range(0, 101):
					
						for g in range(0, 201):
								
							coins = [a, b, c, d, e, f, g]
							
							if total(coins) == 200:
								result += 1
								print(coins)
							
#Account for 2 pound coin on its own
result += 1
								
print(result)