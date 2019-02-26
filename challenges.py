
#Function that takes a number "n" and returns the sum of the numbers from 1 to "n". 
def sum_to(n):
	x = list(range(n))
	y = sum(x) + n
	print(y)

sum_to(10)