#euler 90

import itertools

def numbers(d1, d2):
    
    output = []
    
    for n1 in d1:
        
        for n2 in d2:
            
            #print(n1 + " " + n2)
            
            if n1 == '6' or n1 == '9':
                
                output.append(int('6' + n2))
                output.append(int('9' + n2))
                output.append(int(n2 + '6'))
                output.append(int(n2 + '9'))
            
            if n2 == '6' or n2 == '9':
                
                output.append(int('6' + n1))
                output.append(int('9' + n1))
                output.append(int(n1 + '6'))
                output.append(int(n1 + '9'))
            
            if n1 != '6' and n1 != '9' and n2 != '6' and n2 != '9':
                output.append(int(n1 + n2))
                output.append(int(n2 + n1))
            
    return output

def all_exist(nums):
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    for s in squares:
        if s not in nums:
            return False
    
    return True

#01, 04, 09, 16, 25, 36, 49, 64, and 81

digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
results_all = []

for comb1 in itertools.combinations(digs, 6):
    
    for comb2 in itertools.combinations(digs, 6):
        
        result = numbers(comb1, comb2)
        
        if all_exist(result):
            
            res = (sorted(comb1), sorted(comb2))
            
            if res not in results_all:
                results_all.append(res)
                
                print(res)
                
print(str(len(results_all)/2))