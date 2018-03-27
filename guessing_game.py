# Guessing Game

# Create a program that asks the user to guess a number between 1 and 100.

# Once the user guesses a number, the program should say, higher, lower, or
# tell the user that he got the number correct. The user should continue to
# make guesses until he guesses correctly. Also, once the user guesses correctly,
# the program should print the number of guesses needed to arrive at the correct answer.

# Below is sample output:


# Guess a number between 1 and 100
# 50 <-- user input
# The number is lower than 50.  Guess again
# 25
# The number is lower than 25.  Guess again
# 13
# The number is higher than 13.  Guess again
# 20
# The number is lower than 20.  Guess again
# 17
# The number is higher than 17.  Guess again
# 18
# The number is higher than 18.  Guess again
# 19
# You got it in 7 tries


# HINT:
# To get input from a user use the input() method:
# num_of_cookies = input("How many cookies should I eat?")
# num = int(num)

# This will assign the typed input value to your variable as a number


# *** your code here ***


def guess_number():
    guess = input("Guess what number I am thinking of, between 1-100: ")
    answer = '31'
    num_guesses = 1
    if guess == answer:
        print("You're a genius! " + answer + " was the correct number. You got it on the first try.")
    else:
        while guess != answer:
            num_guesses += 1
            if guess > answer:
                guess = input("Sorry, the number is lower than " + guess + ". Please try again: ")
            else:
                guess = input("Sorry, the number is higher than " + guess + ". Please try again: ")
        print("Yep, " + answer + " is the correct answer! That took you " + str(num_guesses) + " guesses.")

guess_number()
