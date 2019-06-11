#euler 206

from tqdm import tqdm

def works(num):
	num_list = list(str(num))
	
	if num_list[0] != '1':
		return False
	elif num_list[2] != '2':
		return False
	elif num_list[4] != '3':
		return False
	elif num_list[6] != '4':
		return False
	elif num_list[8] != '5':
		return False
	elif num_list[10] != '6':
		return False
	elif num_list[12] != '7':
		return False
	elif num_list[14] != '8':
		return False
	elif num_list[16] != '9':
		return False
	elif num_list[18] != '0':
		return False
		
	return True

n = 1000000000

#while True:
for n in tqdm(range(1000000000, 1389244399)):
	
	#print("Testing " + str(n))
	
	sq = n * n
	
	if works(sq):
		print("Winner!")
		print(str(n) + "^2 = " + str(sq))
		exit()
	
	
	elif sq > 1930000000000000000:
		print("Failed!")
		exit() 
	
	
		
	n += 1