#euler 132

from sympy import isprime


def gen_primes(limit):

    output = []
    
    test = 7

    while test <= limit:

        if isprime(test):

            output.append(test)

        test += 1

    return output

def y_primes():

    test = 7

    while True:
    
        if isprime(test):

            yield test

        test += 1

total = 0
count = 0

for p in y_primes():

    if pow(10, 10**9, (9*p)) == 1:

        print(p)
        total += p
        count += 1

        if count == 40:
            print("TOTAL:", total)
            input()


