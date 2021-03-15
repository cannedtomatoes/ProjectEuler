#euler125

import math
from collections import Counter

def pal(n):
	number = list(str(n))
	
	half = len(number) / 2	
	i = 0
	last = len(number) - 1
	
	
	
	if len(number) % 2 == 0:
		end = half
	else:
		end = math.floor(half)
	
	while i < end:
		if number[i] == number[last]:
			i += 1
			last -= 1
		else:
			return False
	return True


limit = 10**8
squares = []

for i in range(1, 10001):
    squares.append(i*i)
    
#print(squares)

c = Counter()
total = 0

for length in range(2, 10001):
    
    print("Length = " + str(length))
    
    pos = 0
    
    while (pos + length) < 10000:
    
        t = sum(squares[pos:(pos+length)])
        #print("squares[" + str(pos) + ":" + str(pos+length) + "]")
        #print(squares[pos:(pos+length)])
        
        if c[t] == 0:
            c[t] = 1
        
            if pal(t):
                if t < limit:
                    total += t
                
                #print(t)
                #print("squares[" + str(pos) + ":" + str(pos+length) + "]")
        
        pos += 1
        
print("Total = " + str(total))