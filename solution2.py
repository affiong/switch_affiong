max_attempts = 5
WORD_LIST = ["car","plane","train","ship","boat"]

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
def evaluate_guess (word,attempts):
    while attempts > 0:
        guess = get_guess()
        if guess != word:
            attempts -=1
            print("wrong attepts, you have", attempts, "left")

            evaluate_guess(word,attempts)
        else:
            print("your guess is correct")
            return True
            break
    
    else:
        print("you have used up your attempt")
        return False
       
def play_game(game_count):
    game_count+=1
    word = pick_word(WORD_LIST)
    print("welcome to word guess game")
    print()
    while evaluate_guess(word,5):
        ask = input("do you want to continue: ")
        if ask == "yes":
            game_count +=1
            play_game(game_count)
        else:
            print("you played", game_count, "game")
            print("goodbye")
            exit()
    else:
        print("oops you missed that one")
        retry = input("do you want to try another one: ")
        if retry == "yes":
            play_game(game_count)
        else:
            print("goodbye")

play_game(0)

##order of execution 4,3,1,2
