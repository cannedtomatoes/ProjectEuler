#euler 700

import math

x = 1
lowest = math.inf
results = []

while True:
    ec = (1504170715041707*x) % 4503599627370517

    if ec < lowest:
        print(x, ec)
        results.append(ec)
        lowest = ec

    if ec == 15806432:
        break

    x += 1


#When ec = 1, n = 3451657199285664

ec_test = 1
current_max = 4503599627370517

while ec_test != 15806432:

    number = (3451657199285664 * ec_test) % 4503599627370517

    if number < current_max:
        current_max = number

        results.append(ec_test)

        print(number, ec_test)

    ec_test += 1

    

print(sum(results))
