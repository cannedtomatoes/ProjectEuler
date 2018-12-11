// euler 120
// 3011116
// 333082500


#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{

	int r_max = 0;
	int total = 0;
	
	for (int a = 3; a <= 1000; a++)
	{		
		r_max = (2*a)*((a-1)/2);
		
		//cout << "a = " << a << ", r_max = " << r_max << "\n";
		//getchar();
		
		total += r_max;
		
		
	}
		
	cout << "\nTotal = " << total << "\n";	
		
	return 0;
	
}