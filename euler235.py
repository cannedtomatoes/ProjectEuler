# euler 235

import sys

def S(r):

    numerator = 897 - (900*r) + (14103*(r**5000)) - (14100*(r**5001))

    denominator = (1-r)**2

    return numerator/denominator


r_guess = 1.002

target = -600_000_000_000



last_gap = 0.0000000000001

gap = 0.0001

done = False

added_last = False
subtracted_last = True

while not done:

    S_guess = S(r_guess)
    #print("S_guess =", S_guess)
   
    sys.stdout.write("\r" + "r = " + str(r_guess) + ", gap = " + str(gap) + ", guess = " + str(S_guess))
    sys.stdout.flush()
    
    if S_guess < target:

        if not added_last:
            #print("We subtracted last time, increasing gap")
            added_last = True
            subtracted_last = False
            gap /= 10

        r_guess -= gap
        #print("subtracting, r is now", r_guess)

    elif S_guess > target:

        if not subtracted_last:
            #print("We added last time, increasing gap")
            subtracted_last = True
            added_last = False
            gap /= 10

        r_guess += gap
        #print("adding, r is now", r_guess)

    else:

        if abs(S_guess - target) < 1:
            done = True
            print("*****")
            print(r_guess)
    
