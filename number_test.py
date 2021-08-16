import random

# If you want to Start debug for the game, set this to True
debug = False
# settings for the game
min_number = 1
max_number = 50
max_score = 10000
attempt_reduce_points = 5000

# the score system
def score_system(attempts):
	return max_score - attempts*attempt_reduce_points

# the random number to be genereted
def random_number():
	random_number = random.randint(min_number,max_number)
	return int(random_number)

# calculate the max number of attempts based on scores and how many points reduce each failure.
def max_attempts():
	return int(max_score / attempt_reduce_points) 



#actual "gui" to make the game look "cool" lol jk ;)
print("\n \n \n")
print("---------------------------------------------------")
print("------------ Number guessing game! ----------------")
print("--------- Created by: Anton Andersson -------------")
print("---------------------------------------------------")
print("\n \n \n")

# Start by getting a random number between min_number and max_number
number_to_guess = random_number()

# count the attempts , starting at zero, because all programmers knows that counting start at zero!
count_attempts = 0
max_attempts = max_attempts()

# Debug info
if debug == True:
	print("(Debug info) Answer is:  " + str(number_to_guess))

# The game 

while True:
	# get the user input and show the player in what range the number can be
	print( "\n" + "Attempts left: " + str(max_attempts) +  "\n")
	input_raw = input("Guess a number between " + str(min_number) + " and " + str(max_number) + " : "  )

	# debug info to see if everything works
	if debug == True:
		print("(Debug info) User typed in: " + str(input_raw))


	if input_raw.isnumeric() == True and count_attempts <= max_attempts: #check if the input is a number or not, so we dont count misstypes
		count_attempts += 1
		max_attempts -= 1
		if int(input_raw) < number_to_guess: #if the number is higher then the user has entered.
			print( "\n" + "The number is higher then " + str(input_raw) + "\n")
		if int(input_raw) > number_to_guess: #if the number is lower then the user has entered.
			print( "\n" + "The number is lower then " + str(input_raw)  + "\n")
		if int(input_raw) == number_to_guess: # If the guess is on the spot! Congratz to the player!
			print("Well done! The correct number was " + input_raw)
			print("Your score: " + str(score_system(count_attempts))) # Show the score for the player
			break
	if count_attempts > max_attempts: # if all lifes are gone
		print("Sorry your score is 0 :'( you lost " + "\n")
		break

	if input_raw.isnumeric() == False: # tell the user to enter a number
		print("You need to enter a positive number!")


