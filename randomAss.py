import random

word_list = ["father", "mother", "sister", "aunty", "family"]

word = random.choice(word_list)


print("You have 5 attempts at guessing words")
print("choose randomly from the following words, father, mother, sister, aunty, family")

def word_guess (word,word_list):

    guess = input("please guess a word: ")
    tries = 1
    
    while word != guess:
        while tries < 5:
            tries = tries+1
            guess = input("please try again >>>:::")
            if tries ==3:
                print("do you want a clue: ")
                answer = input("yes,no:")
                if answer =="yes":
                    print("clue : guess words that are family related")
            
        if guess == word:
            print("well done, you are a smart one")
            input("")
        else:
            print("LOOOOOOOOOOOOOOOSER")
            input("")
        

   
    
word_guess(word,word_list)
