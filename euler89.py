#euler 89



def roman_to_arabic(chars):
	result = 0
	
	chars_list = list(chars)
	#print(chars_list)
	to_delete = []
	
	#Sliding window
	
	for i in range(0, len(chars_list)-1):				
			
		j = i + 1
		
		#print(str(i), str(j))
		#print(chars[i], chars[j])
				
		if chars[i] == 'I' and chars[j] == 'V':
			result += 4
			to_delete.append(i)
			to_delete.append(j)
		if chars[i] == 'I' and chars[j] == 'X':
			result += 9
			to_delete.append(i)
			to_delete.append(j)
		if chars[i] == 'X' and chars[j] == 'L':
			result += 40
			to_delete.append(i)
			to_delete.append(j)
		if chars[i] == 'X' and chars[j] == 'C':
			result += 90
			to_delete.append(i)
			to_delete.append(j)
		if chars[i] == 'C' and chars[j] == 'D':
			result += 400
			to_delete.append(i)
			to_delete.append(j)
		if chars[i] == 'C' and chars[j] == 'M':
			result += 900
			to_delete.append(i)
			to_delete.append(j)
		
	#print("To delete: " + str(to_delete))
	
	new_list = []	
	k = 0
	while k < len(chars_list):
		if k not in to_delete:
			new_list.append(chars_list[k])
		k += 1
	
	chars_list = new_list
	
	#print("Result so far: " + str(result))
	#print(chars_list)	
		
	for c in chars_list:
		if c == 'I':
			result += 1
		elif c == 'V':
			result += 5
		elif c == 'X':
			result += 10
		elif c == 'L':
			result += 50
		elif c == 'C':
			result += 100
		elif c == 'D':
			result += 500
		elif c == 'M':
			result += 1000
	
	return result

def arabic_to_roman(number):
	#print("Converting " + str(number))
	result = []
	number_list = []
	
	
	#print("Length = " + str(length))

	
	for num in list(str(number)):
		number_list.append(int(num))
		
	length = len(number_list)
	
	if length == 4:
		place = [1000, 100, 10, 1]
	elif length == 3:
		place = [100, 10, 1]
	elif length == 2:
		place = [10, 1]
	elif length == 1:
		place = [1]
	
	
	
	i = length - 1
	
	#print("i = " + str(i))
	
	while i >= 0:
	
		digit = number_list[i]
	
		if place[i] == 1:
			if digit <= 3:
				result.append(digit*'I')
			elif digit == 4:
				result.append('IV')
			elif digit == 5:
				result.append('V')
			elif digit > 5 and digit < 9:
				result.append('V' + ('I' * (digit-5)))
			elif number_list[i] == 9:
				result.append('IX')
				
		elif place[i] == 10:
			if digit <= 3:
				result.append(digit*'X')
			elif digit == 4:
				result.append('XL')
			elif digit == 5:
				result.append('L')
			elif digit > 5 and digit < 9:
				result.append('L' + ((digit-5) * 'X'))
			elif digit == 9:
				result.append('XC')
				
		elif place[i] == 100:
			if digit <= 3:
				result.append(digit*'C')
			elif digit == 4:
				result.append('CD')
			elif digit == 5:
				result.append('D')
			elif digit > 5 and digit < 9:
				result.append('D' + ((digit-5) * 'C'))
			elif digit == 9:
				result.append('CM')
		
		elif place[i] == 1000:
			result.append(digit * 'M')
			
		i -= 1
			
	return(''.join(reversed(result)))
		
f = open("p089_roman.txt")
r_numbers = []
all_text = f.readlines()
f.close()

for l in all_text:
	
	r_numbers.append(l.replace('\n', ''))
	
saved = 0

for r in r_numbers:
	l_orig = len(r)
	number = roman_to_arabic(r)
	r_new = arabic_to_roman(number)	
	l_new = len(r_new)
	
	saved += (l_orig - l_new)
	
	#print(r)
	#print(r_new)
	#print(saved)
	#input()
	
print(saved)	