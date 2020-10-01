import random #import random module

def play_again():
	answer = input("\nWould you like to play again ? \n yes / no\n").lower() #input from user after playing game 1st time
	if answer == "y" or answer == "yes" :							#if input is yes
		play_game()																#enter to th play_game function
	else :																				#if input is no
		pass																			#end program
   		
def get_word():
	words = ['emotica' , 'avc' , 'souls' , 'vibranz' , 'picxels']
	return random.choice(words)								#random, word choose by interpreter
	

def play_game():
	alphabet =   'abcdefghijklmnopqrstuvwxyz'
	word = get_word()
	letters_guessed = [ ]
	score = 10
	guessed = False
	words = ['emotica' , 'avc' , 'souls' , 'vibranz' , 'picxels']
	index = words.index(word)						#to find the index of that random word
	print("\t \t ##### WELCOM TO HANGMAN GAME ##### \n \n")
	print(len(word) * '*')									#to print the word in encrypted form
	#to print the hint of word choosen by interpreter
	if index == 0:
		print('Hint: Performs theatricals.')
	if index == 1:
		print('Hint: where writings are turned into cinema.')
	if index == 2:
		print('Hint: Speaks through music.')
	if index == 3:
		print('Hint: Makes music alive.')
	if index == 4:
		print('Hint: It freezes the memories for us.')
	type =int(input('\n \n How will you guess the letter? \n 1.Gues the entire word. \n 2.Guess the letters one by one. \n'))		#to take information how user want to guess
	if type == 1:				#user choose guess direct word
		print('\n')
		print(len(word) * '*')
		print('score = ',int(score))
		while guessed  == False and score > 0 :			#starting a while loop when guesses = false and score > 0
			guess = input('\nGuess the word:\t').lower()		#it store the guess word given by the user
			if len(guess) == len(word):						#if guess word is correct
				if guess == word:
					print('correct guess')
					guessed = True						#guessed become true for stop the while loop
					score = int(score) + 5		     #5 points given to user
					print('score = ',int(score))
					print('\t \t YOU WIN :)')
					print('\t     YOUR SCORE IS', int(score))
				else :
					print('incorrect guess')			#if guess is incorrect
					score = int(score)  - 3				# 3 point is reduce from user score
					print('score = ',int(score))
			else :
				print('incorrect guess')
				score = int(score)  - 3
				print('score = ',int(score))
	if type == 2:								#user chooes to find the word by guessing one by one letter
		print(len(word) * '*')
		print ("score =", int(score))
		while guessed == False and score>0:		#starting a while loop when guesses = false and score > 0
			guess = input('\nGuess the letter \t').lower()  #.lower() is used for to save all alphabets in lowerform
			if len(guess) == 1:		#to check user put only one letter or not
				if guess not in alphabet:		#to check the input given by user is alphabet or not
					print('It is not an alphabet')
				if guess in letters_guessed:		#to check the input given by user is  repet or not
					print('alredy guess')
					if guess in word:
						score=int(score)-5
					#if guess not in word:
						#score=int(score)+2    #in phone elif function doesn't support so for correct the error in score i added line no. 68 - 71
				if guess in word:				#to check the input given by user is present in word or not
					print("correct guess")
					letters_guessed.append(guess) #store the guess letter in letters_guessed file
					score=int(score)+3	#if yes add 3 point to user score
				if guess not in word:		#to check the input given by user is alphabet or not
					print("incorrect guess")
					letters_guessed.append(guess)
					score=int(score)-2		#if not the reduce 2 points from user score
			else:
				print('You enter more than one letter or does not enter the letter')
				#to show the user guessed and unguessed letters of the word
			status= ''
			if guessed == False:
				for letter in word:
					if letter in letters_guessed:
						status=status + letter	#show the correct guessed letter in its place
					else:
						status=status + "*"      #show * in place of unguessed letters
				print(status)
				print('score = ',int(score))		#show the final score of the user
			if status == word :
				print('\t \t YOU WIN :)')
				print('\t     YOUR SCORE IS', int(score))
				guessed = True
			#if score <= 0 :
				#print('\t \t YOU LOSE  ):')
	if score <= 0 :
		print('\t \t YOU LOSE ):')
	if type != 1 and type != 2:
		print('This is not in option ')
	play_again()		#ask the user
play_game()