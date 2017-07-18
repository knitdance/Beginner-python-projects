import random
 
guess = int(input("Guess a number between 0 and 20: "))
x = random.randint(0, 20)
print(x)

if guess == x:
	print("Congratulations, you guessed right!")
	
while True:
	if guess < x:
		print("Your guess is too low. Guess another number:")
		guess = int(input()) 

	elif guess > x:
		print("Your guess is too high. Guess another number:")
		guess = int(input()) 
	

	else:
		print("Congratulations, you guessed right!")
		break
		
	

#Learning here - important in the while loop to do if, elif, else.
#if can't be followed by if - it seems to work until it goes weird.
#the else must be part of the while loop for when the condition does become true.
#must add a break at the end of the while loop or it prints congratulation forever.