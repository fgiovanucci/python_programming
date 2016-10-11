# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    for letters in secretWord:
        if letters in lettersGuessed:
            return True
    return False
    
# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    end_string = ''
    for letters in secretWord:
        if letters in lettersGuessed:
            end_string + letters
        else:
            end_string + '_'
    return new_string

# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord,lettersGuessed))



# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.
    import string 
    available_letters = list(string.ascii_lowercase)
    for letters in lettersGuessed:
        if letters in available_letters:
            available_letters.remove(letters)
    return available_letters


      


# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


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
    print('Welcome to Hangman. Here are the rules: you have 8 guesses, you will not lose a turn for a repeated guess or a correct guess, after all your guesses have been used and you have not solved the hangman you lose.  Your secret word has', len(secretWord), 'letters.  Good Luck!' )
    lettersGuessed = []
    guesses_allowed = 8
    guesses_taken = 0
while not isWordGuessed(secretWord, lettersGuessed) and guesses_allowed < 8:
    letter = ('Guess a letter. ')
    print(getAvailableLetters(lettersGuessed))
    print(getGuessedWord(secretWord, lettersGuessed))
    if letter in secretWord:
        print('You have guessed correctly.')
    elif letter in lettersGuessed:
        print('You have already guessed this letter.')
    else:
        print('You have guessed wrong.  Please guess again!')
        guesses_taken = guesses_taken + 1
        print('You have', guesses_allowed - guesses_taken,'left.')
    lettersGuessed.append(letter)
if guesses_taken == guesses_allowed:
    print('You are out of turns.  You lose')
    print('The secret word was', secretWord,'.')
else:
    print('Congrats, you won!')



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
