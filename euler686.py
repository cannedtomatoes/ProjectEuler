#euler 686

import math

leading_target = 123

search = 678910

current = 0

test = 1

log_10_2 = math.log10(2)

while True:

    val = test * log_10_2

    m = val - math.floor(val)

    digs = math.floor(100*(10**m))

    if digs == leading_target:

        current += 1

        if current == search:

            print("Found! 2^", test)

    test += 1
