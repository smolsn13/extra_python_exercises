# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***
def fibonacci(n):
	list = [0, 1]
	if n == 1:
	    list = [0]

	elif n > len(list):
		for i in range(n - 2):
			list.append(list[i] + list[i + 1])


	print(list)


fibonacci(10)
