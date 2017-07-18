import random

print("Your first roll is", random.randint(1,6))

roll_again = input("Would you like to roll again?:")

while roll_again.lower() == ("y" or "yes"):
	print("Your dice says", random.randint(1,6))
	roll_again = input("Would you like to roll again?:")

if roll_again.lower() != ("y" or "yes"):
	print("Goodbye")



#Learning point - the key thing here is if there are
#two conditions after == THERE MUST BE BRACKETS AROUND THEM
#OR EVERYTHING FUCKS UP.
#There is no need to add the if bit - just seems more polite.
	
