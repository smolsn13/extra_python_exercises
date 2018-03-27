# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***

def pyramid(n):
	for i in range(n):
		print(' ' * (n - i - 1) + '#' * (i + 1) + ' ' + '#' * (i + 1) + ' ' * (n - i - 1))

pyramid(10)
