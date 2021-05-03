#euler 173
# 12, 20, 28
#

import sys

odds = []
evens = []

total = 1000000
done = False

s = 4
while not done:
    
    tiles = (s*4) - 4
    if tiles <= total:
        #print(tiles)
        evens.append(tiles)
        s += 2
    else:
        done = True


done = False
s = 3
while not done:
    
    tiles = (s*4) - 4
    if tiles <= total:
        #print(tiles)
        odds.append(tiles)
        s += 2
    else:
        done = True

total_lam = 0

for width in range(0, len(evens) + 1):
    
    start_pos = 0
    
    while start_pos < len(evens):
        
        sys.stdout.write("\rEvens width " + str(width))
        sys.stdout.flush()
	
        try:
            lam = sum(evens[start_pos:(start_pos+width)])
        except:
            break
        else:
            if lam <= total and lam > 0:
                total_lam += 1
                #print(evens[start_pos:(start_pos+width)])
                #print(lam)
            else:
                break
            
        start_pos += 1

for width in range(0, len(odds) + 1):
    
    start_pos = 0
    
    while start_pos < len(odds):
        
        sys.stdout.write("\rOdds width " + str(width))
        sys.stdout.flush()
	
        try:
            lam = sum(odds[start_pos:(start_pos+width)])
        except:
            break
        else:
            if lam <= total and lam > 0:
                total_lam += 1
                #print(odds[start_pos:(start_pos+width)])
                #print(lam)
            else:
                break
    
        start_pos += 1
        
print(total_lam)