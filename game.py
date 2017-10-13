import math
import random

def guessNo(guess):
	if guess < ans:
		return 'Guess Higher next time'

	elif guess == ans:
		return 'You guessed your answer right'

	elif guess > ans:
		return 'Try harder next time Bro!'
  
print ('The guess Game\n========================')

print('Instructions :')
print('******************')
print('1.You will take guess of only numbers between 1 and 10.')
print('2. If you fail 7 times the correct answer will be displayed.')
print("")
print('				 ENJOY		')
print("")
print(' 	*****************************************************')
print(' 	*****************************************************')

print("")
print("")

ans = random.randint(1,10)
print('Am thinking about a Number between 1 and 10')
print('')
#ask the player to guess 7 times
for guessTaken in range(1,7):	
	print ("ENTER YOUR GUESS")
	print("")
	guess = input()
	guess =int (guess)

	if guess < ans:
		print ('Guess Higher next time')

	elif guess > ans:
		print ('Try harder next time Bro!')

	else:    

	    break    # This condition is the correct guess!

if guess == ans: 
   print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!') 

else: 
    print('Nope. The number I was thinking of was ' + str(ans))






	