import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ['python', 'computer', 'programming', 'developer', 'keyboard', 'mouse']
    word_to_guess = random.choice(words)
    scrambled_word = scramble_word(word_to_guess)
    
    print("Welcome to the Word Scramble Game!")
    print(f"The scrambled word is: {scrambled_word}")
    
    attempts = 0
    while True:
        guess = input("Guess the word: ").lower()
        attempts += 1
        
        if guess == word_to_guess:
            print(f"Correct! The word is '{word_to_guess}'. You guessed it in {attempts} attempts.")
            break
        else:
            print("Wrong guess, try again.")

word_scramble_game()
