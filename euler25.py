#euler25

def fib():
	a, b = 0, 1
	while True:            # First iteration:
		yield a            # yield 0 to start with and then
		a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
		
		
		
for i, f in enumerate(fib()):
	if len(str(f)) >= 1000:
		print(i)
		exit()