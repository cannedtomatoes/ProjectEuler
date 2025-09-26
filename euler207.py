#euler 207

import math
import sys
import struct

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def is_power_of_two(n):
    """
    Checks if a non-negative integer is a power of 2 using a bitwise trick.
    """
    if n <= 0:
        return False
    else:
        # A number is a power of 2 if and only if 
        # (n > 0) AND (n & (n - 1) == 0)
        return (n & (n - 1)) == 0

def is_float_power_of_two_bitwise(f):
    """
    Checks if a positive float is a power of two by inspecting its IEEE 754 bits.
    A float is a power of two if and only if the mantissa (significand) is zero.
    """
    if f <= 0.0 or f == float('inf'):
        # Handle non-positive numbers, zero, and infinity
        return False

    # 1. Get the 64-bit integer representation of the float
    # '<Q' means little-endian (Intel) 64-bit unsigned long long
    # This is a low-level operation that gets the actual bits
    raw_bits = struct.unpack('<Q', struct.pack('<d', f))[0]

    # IEEE 754 Double-Precision (64-bit) Layout:
    # Bit 63: Sign (1 bit)
    # Bits 62-52: Exponent (11 bits)
    # Bits 51-0: Mantissa/Significand (52 bits)

    # 2. Extract the Mantissa bits
    # The mantissa is in the lowest 52 bits.
    # We use a bitmask of 52 ones: (2**52 - 1)
    MANTISSA_MASK = 0xFFFFFFFFFFFFF  # 52 bits set to 1

    mantissa = raw_bits & MANTISSA_MASK

    # 3. Check the Exponent (special case: denormalized numbers)
    # Denormalized numbers have an exponent of 0 and a non-zero mantissa.
    # We must exclude them because they are NOT powers of 2.
    # The Exponent is bits 52 through 62.
    EXPONENT_MASK = 0x7FF0000000000000  # 11 bits set to 1 at position 52

    exponent = raw_bits & EXPONENT_MASK

    # A positive float 'f' is a power of two if:
    # a) It is a normal number (exponent is NOT zero)
    # b) The 52 bits of the mantissa are all zero.
    if exponent != 0 and mantissa == 0:
        return True
        
    # We check for denormalized numbers with exponent=0. They have a non-zero 
    # implicit bit, so a mantissa of 0 means the number is 0.0, which we handle 
    # at the start. So, any other power of 2 must have a non-zero exponent.
        
    return False

def next_val(n):

    return (2**(2*n)) - (2**n)

found = 0

n = 1

a = next_val(n)

target = 1/12345

perfect = 0

m = 1

k = m * (m + 1)

#for k in range(1, m+1):
while True:
    


    found += 1

    if k == a:

        perfect += 1
        n += 1
        a = next_val(n)

       
    #print("P(" + str(k) + ") = " + str(perfect/found))
    sys.stdout.write('\r' + "P(" + str(k) + ") = " + str(perfect/found))
    sys.stdout.flush()
    

    q = perfect/found
    
    if q < target:
        print("\nWinner:", k)
        input()
    

    m += 1
    k = m * (m + 1)
