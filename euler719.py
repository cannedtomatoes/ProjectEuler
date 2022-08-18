#euler 719

import itertools


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]



def div(s, n):
    return [[s[i:j] for i, j in zip([None, *cuts], [*cuts, None])]
            for cuts in itertools.combinations(range(1, len(s)), n-1)]

def find_match(num, orig):
	
	splits = 2
	
	while splits <= len(num):
		
		nums = div(num, splits)
		

		for nu in nums:
		
			attempt = 0
		
			for numb in nu:
			
				attempt += int(numb)
		
			if attempt == orig:
				
				return True
			
		
		splits += 1
		
	return False
		
number = 1
sq = 1

result = 0

highest = 10 ** 12

while sq <= highest:
	
	
	sq = number * number
	
	
	a = find_match(str(sq), number)
	
	if a:
		result += sq
		print(number)
	
	number += 1
	

print("Result: " + str(result))

	




