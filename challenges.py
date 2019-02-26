
#Function that takes a number "n" and returns the sum of the numbers from 1 to "n". 

# def sum_to(n):
# 	x = list(range(n))
# 	y = sum(x) + n
# 	print(y)


def sum_to(num):
  sum = 0
  for i in range(num + 1):
    sum += i
  print(sum)

sum_to(10)



#Function that takes a list parameter and returns the largest element in that list. 
#You can assume the list contents are all positive numbers.

def largest(list):
	largest = 0
	for i in list:
		if(i>largest):
			largest = i
	print(largest)


largest([1,2,34,5,6])




#Function that counts the number of occurrances of the second string inside the first string.

def occurances(one, two):
	occur = 0
	for i in one:
		if(i == two):
			occur += 1
	print(occur)


occurances('fleeeeep floop', 'e')












