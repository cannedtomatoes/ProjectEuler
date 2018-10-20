#euler 19
#1 Jan 1900 was a Monday.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def leapyear(y):
	if y % 4 == 0:
		if y % 100 == 0:
			if y % 400 == 0:
				return True
			else:
				return False
		else:
			return True
				
			
	else:
		return False

days_of_the_week = []
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(0, 60000):
	days_of_the_week.extend(week)


months = {1:31, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

year = 1900
month = 1
day = 1
day_it = 0

result = 0

while year <= 2000:
	
	#if leapyear(year):
		#print(year)
	
	month = 1
	
	while month <=  12:
		
		if month == 2:
			if leapyear(year):
				days_in_month = 29
			else:
				days_in_month = 28
		else:
			days_in_month = months[month]
		
		day = 1
		
		while day <= days_in_month:
		
			today = days_of_the_week[day_it]

			#print(today + " " + str(day) + " " + str(month) + " " + str(year))
			#input()
			
			if today == 'Sunday' and day == 1:
				result += 1
				#print("WINNER")
				print(today + " " + str(day) + " " + str(month) + " " + str(year))
			
			day += 1
			day_it += 1
			
		
		month += 1
		
	year += 1

print(result)