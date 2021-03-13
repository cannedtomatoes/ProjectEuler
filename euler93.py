#euler 93
#1258 52

import itertools
import string

def clean(res):
    
    res1 = set(res)
    res2 = list(res1)
    res3 = sorted(res2)
    
    return res3

def cons(nums):
    
    end = len(nums)
    
    if end < 2 or nums[0] != 1:
        return False
    
    i = 1

    while i < end:
        if nums[i] - nums[i-1] != 1:
            return False
        
        i += 1
    #print("Returning true " + str(nums))
    #input()
    return True

def longest(num_list):
    
    prev = 0   
   
    for i in range(2, len(num_list)):
        if cons(num_list[:i]):
            prev = num_list[i-1]
        else:
            return prev

def operate(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b

#digs = [1, 2, 3, 4]
all_digs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ops = ['+', '-', '*', '/']
high = 0

for digs in itertools.combinations(all_digs, 4):
    
    #print(digs)
    output = []

    for d_perm in itertools.permutations(digs):
        
        
        
        #print("Using " + str(d_perm))
        
        one = d_perm[0]
        two = d_perm[1]
        three = d_perm[2]
        four = d_perm[3]
        
        for o_comb in itertools.combinations_with_replacement(ops, 3):
        
            for o_perm in itertools.permutations(o_comb):
            
                #print("Using " + str(o_perm))
 
                #Now do every version of
                #a+b+c+d
                #(a+b)+c+d
                #a+(b+c)+d
                #a+b+(c+d)
                #a+(b+c+d)
                #(a+b+c)+d
                #(a+b)+(c+d)
                
                exp1 = str(one) + " " + o_perm[0] + " " + str(two) + " " + o_perm[1] + " " + str(three) + " " + o_perm[2] + " " + str(four)
                exp2 = "(" + str(one) + " " + o_perm[0] + " " + str(two) + ") " + o_perm[1] + " " + str(three) + " " + o_perm[2] + " " + str(four)
                exp3 = str(one) + " " + o_perm[0] + " (" + str(two) + " " + o_perm[1] + " " + str(three) + ") " + o_perm[2] + " " + str(four)
                exp4 = str(one) + " " + o_perm[0] + " " + str(two) + " " + o_perm[1] + " (" + str(three) + " " + o_perm[2] + " " + str(four) + ")"
                exp5 = str(one) + " " + o_perm[0] + " (" + str(two) + " " + o_perm[1] + " " + str(three) + " " + o_perm[2] + " " + str(four) + ")"
                exp6 = "(" + str(one) + " " + o_perm[0] + " " + str(two) + " " + o_perm[1] + " " + str(three) + ") " + o_perm[2] + " " + str(four)
                exp7 = "(" + str(one) + " " + o_perm[0] + " " + str(two) + ") " + o_perm[1] + " (" + str(three) + " " + o_perm[2] + " " + str(four) + ")"
                
                #print(exp1 + " = " + str(eval(exp1)))
                #print(exp2 + " = " + str(eval(exp2)))
                #print(exp3 + " = " + str(eval(exp3)))
                #print(exp4 + " = " + str(eval(exp4)))
                #print(exp5 + " = " + str(eval(exp5)))
                #print(exp6 + " = " + str(eval(exp6)))
                #print(exp7 + " = " + str(eval(exp7)))
                #input()
                
                exps = []
                
                try:
                    exps.append(eval(exp1))
                except:
                    pass
                try:
                    exps.append(eval(exp2))
                except:
                    pass
                try:
                    exps.append(eval(exp3))
                except:
                    pass
                try:
                    exps.append(eval(exp4))
                except:
                    pass
                try:
                    exps.append(eval(exp5))
                except:
                    pass
                try:
                    exps.append(eval(exp6))
                except:
                    pass
                try:
                    exps.append(eval(exp7))
                except:
                    pass
                
                for e in exps:
                
                    if e > 0 and float(e).is_integer():
                        
                        
                        output.append(int(e))
                        #print(e)
                        #print("(((" + str(one) + " " + o_perm[0] + " " + str(two) + ") " + o_perm[1] + " " + str(three) + ") " + o_perm[2] + " " + str(four) + " = " + str(result))
    #print(output)
    final = clean(output)
    #print(final)
    #input()
    high_temp = longest(final)
    if high_temp:
                    
        if high_temp > high:
            high = high_temp
            print(str(d_perm) + " " + str(high))
            print(final)
                        
                    
                                