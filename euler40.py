#euler 40

num_list = []

for i in range(10000000):
	num_list.append(str(i))
	
num_str = ''.join(num_list)

result = int(num_str[1]) * int(num_str[10]) * int(num_str[100]) * int(num_str[1000]) * int(num_str[10000]) * int(num_str[100000]) * int(num_str[1000000]) 
print(result)
