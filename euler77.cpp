// euler 77

// C++ program Miller-Rabin primality test 
#include <bits/stdc++.h> 
using namespace std; 

// Utility function to do modular exponentiation. 
// It returns (x^y) % p 
int power(int x, unsigned int y, int p) 
{ 
    int res = 1;      // Initialize result 
    x = x % p;  // Update x if it is more than or 
                // equal to p 
    while (y > 0) 
    { 
        // If y is odd, multiply x with result 
        if (y & 1) 
            res = (res*x) % p; 
  
        // y must be even now 
        y = y>>1; // y = y/2 
        x = (x*x) % p; 
    } 
    return res; 
} 
  
// This function is called for all k trials. It returns 
// false if n is composite and returns false if n is 
// probably prime. 
// d is an odd number such that  d*2<sup>r</sup> = n-1 
// for some r >= 1 
bool miillerTest(int d, int n) 
{ 
    // Pick a random number in [2..n-2] 
    // Corner cases make sure that n > 4 
    int a = 2 + rand() % (n - 4); 
  
    // Compute a^d % n 
    int x = power(a, d, n); 
  
    if (x == 1  || x == n-1) 
       return true; 
  
    // Keep squaring x while one of the following doesn't 
    // happen 
    // (i)   d does not reach n-1 
    // (ii)  (x^2) % n is not 1 
    // (iii) (x^2) % n is not n-1 
    while (d != n-1) 
    { 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1)      return false; 
        if (x == n-1)    return true; 
    } 
  
    // Return composite 
    return false; 
} 
  
// It returns false if n is composite and returns true if n 
// is probably prime.  k is an input parameter that determines 
// accuracy level. Higher value of k indicates more accuracy. 
bool isPrime(int n, int k) 
{ 
    // Corner cases 
    if (n <= 1 || n == 4)  return false; 
    if (n <= 3) return true; 
  
    // Find r such that n = 2^d * r + 1 for some r >= 1 
    int d = n - 1; 
    while (d % 2 == 0) 
        d /= 2; 
  
    // Iterate given nber of 'k' times 
    for (int i = 0; i < k; i++) 
         if (!miillerTest(d, n)) 
              return false; 
  
    return true; 
} 

bool all_prime(int *part_array, int len)
{
	for (int i = 0; i < len; i++)
	{
		if (!isPrime(part_array[i], 4))
		{
			return false;
		}
	}
	return true;
}

int num_prime_parts(int n) 
{ 
    int p[n]; // An array to store a partition 
    int k = 0;  // Index of last element in a partition 
    p[k] = n;  // Initialize first partition as number itself 
	bool first = true;
	int result = 0;
	
    // This loop first prints current partition, then generates next 
    // partition. The loop stops when the current partition has all 1s 
    while (true) 
    { 

		if (!first)
		{
			if (all_prime(p, k+1))
			{
				result++;
			}
		}
		else
		{
			first = false;
		}
		
		
        // Generate next partition 
  
        // Find the rightmost non-one value in p[]. Also, update the 
        // rem_val so that we know how much value can be accommodated 
        int rem_val = 0; 
        while (k >= 0 && p[k] == 1) 
        { 
            rem_val += p[k]; 
            k--; 
        } 
  
        // if k < 0, all the values are 1 so there are no more partitions 
        if (k < 0)  return result; 
  
        // Decrease the p[k] found above and adjust the rem_val 
        p[k]--; 
        rem_val++; 
  
  
        // If rem_val is more, then the sorted order is violated.  Divide 
        // rem_val in different values of size p[k] and copy these values at 
        // different positions after p[k] 
        while (rem_val > p[k]) 
        { 
            p[k+1] = p[k]; 
            rem_val = rem_val - p[k]; 
            k++; 
        } 
  
        // Copy rem_val to next position and increment position 
        p[k+1] = rem_val; 
        k++; 
    } 
} 

  



// Driver program 
int main() 
{ 
    int test = 1;
	int result = 0;
	bool found = false;
	
	while (!found)
	{
		result = num_prime_parts(test);
		cout << "\r" << test << ": " << result;
		
		if (result > 5000)
		{
			found = true;
			cout << "\nResult: " << test;
		}
		test++;
	}

  
    return 0; 
} 