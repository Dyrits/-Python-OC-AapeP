import os
from random import randrange
from math import ceil

money = 1000
playing = True
while playing == True:
	guess=0
	while guess < 1 or guess > 50:
		try:
			guess = int(input('Guess a number between 1 and 50:'))
		except ValueError:
			print("The value is invalid. It must be a number between 1 and 50.")
			continue
		if guess < 1 or guess > 50:
			print("The number guessed must be between 1 and 50.")
	print('You have {}$'.format(money))
	bet=0
	while bet == 0 or bet > money or bet < 0:
		try:
			bet = int(input('Enter the ammount of money you want to bet:'))
		except ValueError:
			print("The value is invalid. Enter a valid value.")
			continue
		if bet > money or bet < 0:
			print("The ammount must not exceed the ammount of money you have, and can not be negative.")
	result = randrange(1, 50)
	print('You chose the number {}!'.format(guess))
	print('You bet {} on it!'.format(bet))
	print('The result is {}!'.format(result))
	if result == guess:
		print('Congratulations, you won {}$!'.format(bet * 3))
		money += bet * 3
		print('You now have {}$'.format(money))
	elif result % 2 == guess % 2:
		print('Congratulations, you won {}$ for picking the right colour!'.format(ceil(bet / 2)))
		money += ceil(bet / 2)
		print('You now have {}$'.format(money))
	else:
		print('Sadly, you lost...')
		money -= bet
		print('You now have {}$'.format(money))
		if money < 0 or money == 0:
			playing = False
			print("You can't continue to play. You have no money left.")
			break
	continue_playing = 0		
	while continue_playing != 'y' and continue_playing != 'n':
		continue_playing = str(input('Do you want to continue? (Y/N)').lower())
		if continue_playing == 0 or continue_playing != 'y' and continue_playing != 'n':
			print('Please, enter Y for YES, or N for No.')
	if continue_playing == 'n':
		playing = False
		print('You chose to stop playing, leaving the game with {}$'.format(money))

os.system("Pause")