#euler 26

import math

#1. Add each digit to digits list
#2. when [divisor, remainder] is repeated, set start_index to current index
#3. keep going until [divisor, remainder] is repeated a second time
#4. output all elements of digits from start_index to current index

highest_period = 0


for x in range(2, 1000):
	
	#print("1/" + str(x) + ":")
	
	digits = []

	#print("Attempting to calculate 1/" + str(x))

	divisor = 10
	past_results = []
	
	second_run = False
	done = False
	
	while not done:
		
		while (divisor / x) < 1:
			divisor *= 10
			
			if [divisor, x] not in past_results:
				digits.append(0)
				past_results.append([divisor, x])
			else:
				digits.append(0)
				if not second_run:
					start_index = len(digits) - 1
					#print("Setting start index to " + str(start_index))
					#print("Digits: " + str(digits))
				
					past_results = []
					second_run = True
				else:
					final_index = len(digits) - 3
					#print("Setting final index to: " + str(final_index))
					#print("Digits: " + str(digits))
					period = final_index - start_index + 1
					#print("Period = " + str(period))
					if period > highest_period:
						highest_period = period
						highest_d = x
					#print actual recurring decimals
					#for h in range(start_index, (final_index+1)):
						
						#print(digits[h])
						 
				
					done = True
			
			
			
			
				
		
		digit = math.floor(divisor / x)

		remainder = divisor - (digit * x) 
		
		#print("Digit: " + str(digit))
		#print("Divisor: " + str(divisor))
		#print("Remainder: " + str(remainder))
		#print("Past result: " + str(past_results))
		
		if [divisor, remainder] not in past_results:
		

			digits.append(digit)
		
			past_results.append([divisor, remainder])
		
		else:
			digits.append(digit)
			if not second_run:
				start_index = len(digits) - 1
				#print("Setting start index to " + str(start_index))
				#print("Digits: " + str(digits))
				
				past_results = []
				second_run = True
			else:
				final_index = len(digits) - 3
				#print("Setting final index to: " + str(final_index))
				#print("Digits: " + str(digits))
				period = final_index - start_index + 1
				#print("Period = " + str(period))
				if period > highest_period:
						highest_period = period
						highest_d = x
				#print actual recurring decimals
				#for h in range(start_index, (final_index+1)):
					#print(digits[h])
				
				done = True
				
		divisor = remainder * 10
		
		if remainder == 0:
			#print("1/" + str(x) + " is not recurring")
			#print("Period = 0")
			done = True
		
print("1/" + str(highest_d) + " has highest period of " + str(highest_period))