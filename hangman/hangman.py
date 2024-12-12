
import random

def choose_word():
    words = ["kantara","animal","jawaan","dunki",
             "ZNMD","salaar","dhoom","3idiots","bramhastra"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += " _ "
    return display

def draw_hangman(attempts):
    hangman_graphics 
        '''
         ------
         |    
         |
         |
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |
         |
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        '''
        ,
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        '''
    ]
    hangman_graphics.reverse()
    return hangman_graphics[attempts]

def classifyLetter(guess,word_to_guess,CorrectlyGuessedLetters,wronglyGuessedLetters):
    if guess in word_to_guess:
        CorrectlyGuessedLetters.append(guess)
    elif guess not in word_to_guess:
        wronglyGuessedLetters.append(guess)
    guessedWords={
        'correct':CorrectlyGuessedLetters,
        'wrong':wronglyGuessedLetters
    }
    return guessedWords


def hangman():
    word_to_guess = choose_word().lower()
    guessed_letters = []
    CorrectlyGuessedLetters=[]
    wronglyGuessedLetters=[]
    attempts = 6

    while attempts >0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        if guess not in word_to_guess:
            attempts -= 1
            print(draw_hangman(attempts))
            
            print(guess,"is not there in the word")
        guessed_letters.append(guess)
        guessedWords=classifyLetter(guess,word_to_guess,CorrectlyGuessedLetters,wronglyGuessedLetters)
        if set(guessedWords['correct']) == set(word_to_guess):            
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

hangman()





