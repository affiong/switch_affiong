WORD_LIST = ["name","car","plane","train","ship","boat"]

import random
##1
def pick_word(listword):
        ##list_word = random.choice(listword)
        word = random.choice(listword)
        ##print("the word is", word) used to cheat on the system
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
def evaluate_guess():
    print("running evaluate guess")
    word = pick_word(WORD_LIST)
    guess = get_guess()
    if guess == word:
        return True
    else:
        return False


##def play_game()
##    print("Hey Welcome!!!")
##    game_count = 5
##    attempts = 0
##    max_attempt = 5
##    while game_count > 0
##    game

##4
def play_game():
    if evaluate_guess() == True:
        print("your game is correct")
        resp = input("Do you want to play again : yes/no: ")
        if resp =="yes":
            play_game()
        else:
            print ("goodbye")
    else:
        evaluate_guess()

play_game()

##order of execution 4,3,1,2

    
