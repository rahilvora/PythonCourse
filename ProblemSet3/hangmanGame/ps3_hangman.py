# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0 
    for guess in lettersGuessed:
        if guess in secretWord:
            count +=1
    if count >= len(secretWord):
        return True
    else:
        return False
#isWordGuessed('sobbingly', ['s','o','b','b','i','n','g','l','y'])
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count  = 0
    initial = 0
    list = []
    while count < len(secretWord):
        list += '_' 
        count += 1
    for guess in lettersGuessed:
        temp = []
        while initial < len(secretWord):
            if secretWord[initial] == guess:
                temp += [initial]
            initial += 1
        for a in temp:
            list[a] = guess
        temp = []
        initial = 0       
    string = ''.join(list) 
    return string     

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import  string
    allWords = string.ascii_lowercase
    for a in lettersGuessed:
        allWords = allWords.replace(a,'')
    return allWords


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    import sys
    secretWord = secretWord.lower()
    border = '_____________'
    lettersGuessed = []
    mistakesMade = 8
    dumy = getGuessedWord(secretWord,lettersGuessed)
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ',len(secretWord),' letters long.'
    while mistakesMade>0:
            print border
            print ''
            print 'You have ',mistakesMade,' guesses left'
            sys.stdout.write('Available words: ')
            sys.stdout.write(getAvailableLetters(lettersGuessed))
            print '' 
            guess = str(raw_input('Please guess a letter: '))
            if guess not in lettersGuessed:
                lettersGuessed += guess
                if dumy == getGuessedWord(secretWord,lettersGuessed):
                    sys.stdout.write("That letter is not in my word: ")
                    sys.stdout.write(dumy)
                    print ''
                    mistakesMade -= 1
                else:
                    dumy = getGuessedWord(secretWord, lettersGuessed)
                    sys.stdout.write('Good guess: ') 
                    sys.stdout.write(dumy)
                    print ''
                    if dumy == secretWord:
                        break
            else:
                sys.stdout.write("Oops! You've already guessed that letter: ")
                sys.stdout.write(dumy)
                print ''
    print lettersGuessed
    if dumy == secretWord:
        print "Congratulation you won"
    else:
        print "You lose, Correct word was", secretWord
                 


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
