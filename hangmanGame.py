guessed = []
#1
def input_letter():
    #allow the user to input a single letter as a guess.
    while True:
        letter = input("enter a letter: ").upper()

        if len(letter) > 1:
            print("please enter only a single letter. ")
        elif letter.isnumeric():
            print("please enter only a letter.")
        else:
            return letter

###2
def check_letter(letter):
    #checks to see if the letter has been guessed already.
    if letter in guessed:
        print("you have already guessed that letter. ")
    else:
        print("you have guessed the letter %s" % letter)
        guessed.append(letter)

#3
def check_word(letter):
    #checks to see if the users letter is in the given word.
    if letter in word:
        print("you have guessed CORRECTLY")
    else:
        print("you have guessed WRONGLY")
    

#1a
while True:
    print("*************************")
    print("you have guessed the following letters: ")
    for i in guessed:
        print(i, end="  ")
    print("\n************************")

    letter = input_letter()
    #guessed.append(letter)
    check_letter(letter)
    check_word(letter)
    response = input("\n\npress <ENTER> to continue, <Q> to quit: ").upper()
    if response == "Q":
        break

