max_attempts = 5
WORD_LIST = ["name","car","plane","train","ship","boat"]

import random
##1
def pick_word(listword):
        word = random.choice(listword)
        print("the word is", word)
        return word


##2
def get_guess():
        guess = input("guess a word: ")
        if not guess =="":
            return guess


        else:
            print ("word cannot be empty")
            get_guess()

##3
def evaluate_guess(attempts_left):
##    print("running evaluate guess")
##    word = pick_word(WORD_LIST)
##    guess = get_guess()
##    if guess == word:
##        return True
##    else:
##        return False
    word = pick_word(WORD_LIST)
    if attempts_left != max_attempts:
        word = word
    else:
        word = pick_word(WORD_LIST)
    guess = get_guess()
    

##def play_game()
##    print("Hey Welcome!!!")
##    game_count = 5
##    attempts = 0
##    max_attempt = 5
##    while game_count > 0
##    game

##4
def play_game():
    attempts_left = max_attempts
    print(attempts_left)
    ##if evaluate_guess() == True:
    if evaluate_guess(attempts_left)== True:
        print("your game is correct")
        resp = input("Do you want to play again : yes/no: ")
        if resp =="yes":
            play_game()
        else:
            print ("goodbye")
    else:
        attempts_left -=1
        
        play_game()

play_game()

##order of execution 4,3,1,2
