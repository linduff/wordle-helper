import json
import random
from datetime import datetime

random.seed(datetime.now())

aw_json = open('allWords.json')
allWords = json.load(aw_json)
mw_json = open('mysteryWords.json')
mysteryWords = json.load(mw_json)

NOT_IN = '0'
IN_WORD = '1'
RIGHT_PLACE = '2'

# az = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

def main():
	mw_length = len(mysteryWords)
	mysteryWord = mysteryWords[random.randint(0,mw_length)]

	guess = ''
	guesses = []

	while 1:
		guess = input('Guess a word: ')
		if(guess == mysteryWord):
			print('You guessed it! The word is ' + guess)
			exit()
		if guess in allWords:
			print(guess + ' is a valid word!')
			tempGuess = ''
			for index, letter in enumerate(guess):
				if(letter == mysteryWord[index]):
					tempGuess += letter.upper()
				elif(letter in mysteryWord):
					tempGuess += letter.lower()
				else:
					tempGuess += '-'
			guesses.append(tempGuess)
			print(guesses)
		else:
			print(guess + ' is not valid. Guess again.')

def numberOfMysteryWordsForEachWord():
	mwInAllWords = {}
	for word in allWords:
		tempDictEntry = 0
		for mWord in mysteryWords:
			for letter in word:
				if letter in mWord:
					tempDictEntry += 1
					break
		mwInAllWords[word] = tempDictEntry
	print(mwInAllWords)
		

def whatWordsAreLeft():
	# mysteryWords = ['their', 'there', 'heard', 'shear', 'reset', 'power', 'mover']
	# allWords = ['their', 'there', 'heard', 'shear', 'reset', 'power', 'mover', 'bower', 'super']
	print('Total possible words: ' + str(len(mysteryWords)))
	while len(mysteryWords) != 0:
		guess = input('Guess:    ')
		feedback = input('Feedback: ')
		guess = guess.lower()
		wordIndex = 0
		if feedback == '22222':
			print(guess + ' is correct!')
			break
		elif guess in mysteryWords:
			mysteryWords.remove(guess)

		if guess in allWords:
			while wordIndex < len(mysteryWords):
				prevMWLength = len(mysteryWords)
				# print(mysteryWords[wordIndex])
				for index in range(len(guess)):
					# print('index: ' + str(index) + '\nfeedback[index]: ' + feedback[index] + '\nguess[index]: ' + guess[index])
					# input()
					if feedback[index] == NOT_IN and guess[index] in mysteryWords[wordIndex]:
						# print(feedback[index] + ': ' + guess[index] + ' is in ' + mysteryWords[wordIndex])
						mysteryWords.remove(mysteryWords[wordIndex])
						break
					elif feedback[index] == IN_WORD and (guess[index] not in mysteryWords[wordIndex] or guess[index] == mysteryWords[wordIndex][index]):
						# print(feedback[index] + ': ' + guess[index] + ' not in ' + mysteryWords[wordIndex] + ' or in the wrong spot')
						mysteryWords.remove(mysteryWords[wordIndex])
						break
					elif feedback[index] == RIGHT_PLACE and guess[index] != mysteryWords[wordIndex][index]:
						# print(feedback[index] + ': ' + guess[index] + ' not at index ' + str(index) + ' in ' + mysteryWords[wordIndex])
						mysteryWords.remove(mysteryWords[wordIndex])
						break
				if prevMWLength == len(mysteryWords):
					wordIndex += 1

			print('Possible words left: ' + str(len(mysteryWords)))
			if len(mysteryWords) < 200:
				print(mysteryWords)
		else:
			'Invalid word. Try again.'



if __name__ == '__main__':
	# main()
	# numberOfMysteryWordsForEachWord()
	whatWordsAreLeft()

