#euler17

def convert(num):
	
	digits = ["", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	teens = ["", 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tens = ["", "ten", 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

	if num <= 10:
		return digits[num]
	elif num < 20:
		return teens[num-10]
	elif num < 100:
		lst = list(str(num))
		return (tens[int(lst[0])] + " " + digits[int(lst[1])])
	elif num == 100:
		return "one hundred"
	elif num < 1000:
		lst = list(str(num))
		
		if lst[1] == '1' and lst[2] != '0':
			return (digits[int(lst[0])] + " hundred and " + teens[int(lst[2])])
		
		return (digits[int(lst[0])] + " hundred and " + tens[int(lst[1])] + " " + digits[int(lst[2])])
	elif num == 1000:
		return "one thousand"

sum = 0
		
for i in range(1, 1001):
	sen = convert(i)
	sen2 = sen.split()
	if sen2[len(sen2)-1] == 'and':
		del sen2[len(sen2) - 1]
	#print(sen2)
	#input()
	
	for s in sen2:
		sum += len(s)
		#print(len(s))
	
print(sum)