//euler112

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> seperate_into_digits( unsigned int value )
{
    vector<int> digits ;
    for( ; value > 0 ; value /= 10 ) digits.push_back( value%10 ) ;
    reverse( digits.begin(), digits.end() ) ;
    return digits ;
}

bool increasing(int num)
{
	vector<int> num_v = seperate_into_digits(num);
	int prev = 0;
	
	for(int i = 0; i < num_v.size(); i++)
	{
		if (num_v[i] < prev)
		{
			//cout << num_v[i] << " < " << prev << ", returning false for increasing\n";
			return false;
		}
		else
		{
			//cout << num_v[i] << " > " << prev << ", continuing.\n";
			prev = num_v[i];
		}
	}
	return true;
}

bool decreasing(int num)
{
	vector<int> num_v = seperate_into_digits(num);
	int prev = 10;
	
	for(int i = 0; i < num_v.size(); i++)
	{
		if (num_v[i] > prev)
		{
			//cout << num_v[i] << " > " << prev << ", returning false for decreasing\n";
			
			return false;
		}
		else
		{
			//cout << num_v[i] << " > " << prev << ", continuing.\n";
			prev = num_v[i];
		}
	}
	return true;
}

bool bouncy(int num)
{
	if (!increasing(num) && !decreasing(num))
	{
		return true;
	}
	else
	{
		return false;
	}
}
	
			

int main()
{
	double q = 1.0;
	double b = 0;

	double current = 1;
	
	while (q != 0.99)
	{
		if(bouncy(current))
		{
			b++;
		}
		

		current++;
		q = b/current;
		
		cout << "\rTesting: " << fixed << current << ", q = " << q << "    ";
	}
	
	
	return 0;
	
}