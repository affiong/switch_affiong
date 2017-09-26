

import random
##import random funtion library

possible_options=['one','two','three','four','five','six','seven']
##list from where the user can pick their options


picked_value = random.choice(possible_options)
##assign one random value from the list to the variable picked_value 

def guessing_game(picked_value,possible_options): ##guessingame() function initialization
    
    print('HERES YOUR GUESS LIST : ', possible_options)##print out the values from the list for user to see
    tries= 1 
    1    print()
    guess=input('Please guess a text from the options : ') 
    print()
    
    while picked_value!=guess:   ##while the user entry is not correct ask the user to try again
        tries=tries+1           ##increase the trial count by 1 every call
        print('wrong value, please try again : ')
        print()
        guess=input('Please guess a text from the options : ')
            

    print('Viola you are a genius monsieur  (',tries  ,' ) : tries')
    print()
    

guessing_game(picked_value,possible_options) ##function call
