##max_attempts = 5
##def evaluate_guess(attempt_left):
##    guess = get_guess()
##    word = ""
##    if attempt_left ==5:
##        word = pick_word
##    if guess == word:
##        print("your guess is not correct")
##        retry = input("do you want to try again? Y/N")
##        if retry = "Y"
##            word = pick_word(WORD_LIST)
##        attempts_left -=1
##    else:
##        attempts_left -=1
##        print("wrong guess")
##        guess = get_guess()
##        evaluate_guess(attempts_left)





max_attempts = 5
WORD_LIST = ["name","car","plane","train","ship","boat"]

def evaluate_guess (word,attempts):
    while attempts > 0:
        guess = guess_guess()
        if guess != word:
            attempts -=1
            print("wrong attepts, you have", attempts, "left")

            evaluate_guess(word,attempt)
        else:
            print("your guess is correct")
            return True
    
    else:
        print("you have used up your attempt")
        return False

def play_game():
    game_count = 0
    word = pick_word(WORD_LIST)
    print("welcome to word guess game")
    print()
    while evaluate_guess(word,5):
        ask = input("do you want to continue")
        if ask == "Y":
            game__count +=1
            play_game()
        else:
            print("you played", game_count, "game")
            print("goodbye")
    else:
        print("oops you missed that one")
        retry = input("do you want to try another one")
        if retry == "Y":
            play_game()
        else:
            print("goodbye")


play_game()
