import random
wordlist = "one two three four five six seven".upper().split()
random.shuffle(wordlist)

secret_word = wordlist.pop()
correct = []
incorrect = []

print("DEBUG: %s" % secret_word)
def display_word():
    #display random word
    for i in secret_word:
        if i in correct:
            print(i, end="  ")
        else:
            print("_", end="  ")
    print("\n\n")
    print("****MISSED LETTERS****")
    for i in incorrect:
        print(i, end="  ")
    print("\n*************************")

def user_guess():
    #allow user to take a guess. append that letter to correct or incorrect
    while True:
        guess = input("Guess a letter\n: ").upper()
        if guess in correct or guess in incorrect:
            print("you have already guessed that letter, Guess again.")
        elif guess.isnumeric():
            print("please enter only letters not numbers. Guess again.")
        elif len(guess) > 1:
            print("please enter only one letter at a time. Guess again.")
        elif len(guess) == 0:
            print("please enter your selection.")
        else:
            break
    if guess in secret_word:
         correct.append(guess)
    else:
          incorrect.append(guess)

def check_win():
    #if the gamer win or loss
    if len(incorrect) > 5:
        return "loss"
    for i in secret_word:
        if i not in correct:
           return "no win"
    return "win"

while True:
    display_word()
    user_guess()
    win_condition = check_win()

    if win_condition == "loss":
        print("GAME OVER!!! the word was ***%s***" % secret_word )
        break
    elif win_condition == "win":
        print("YOU WIN!!! the word was ***%s***" % secret_word)
    
    
              

