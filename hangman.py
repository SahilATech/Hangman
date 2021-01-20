import random

print("H A N G M A N")
choice = input("Type \"play\" to play the game, \"exit\" to quit:")

if choice == "play":
    condition = True
elif choice == "exit":
    condition = False
        
while condition:
    
    wordslist = ['python', 'java', 'kotlin', 'javascript']
    selected_word = random.choice(wordslist)

    result = list(len(selected_word) * '-')                                     #initial result is ------
    remaningChance = int(8)    
   
    guessed_char_list = []                                                       #managed list for gussing characters
    
    while remaningChance > 0 :
        print()
        print(''.join(result))
        guess_char = input("Input a letter: ")
        
        if "-" not in result:                                                    #guess the all Characters of Word then exit
            print("""You guessed the word!  
            You survived!""")
            break  
        
        elif len(guess_char) != 1:
            print("You should input a single letter")                             #check entered exactly one letter
            continue  
        
        elif guess_char.isupper() or guess_char.isalpha() == 0:
            print("Please enter a lowercase English letter")           #check to make sure the player entered an English lowercase letter
            continue
        
        elif guess_char in guessed_char_list:
            print("You've already guessed this letter")
            
            if guessed_char_list.count(guess_char) <= int(2):
                continue                                                #user enters the same letter twice, then the program should output
            else:
                remaningChance -= 1                                        #enters the same letter greater then twice, then reduce Chances
                continue   
            
        if guess_char in selected_word:
            for letter_num in range(len(selected_word)):
                if guess_char == selected_word[letter_num]:                           #letter in word
                    result[letter_num] = guess_char
            guessed_char_list.append(guess_char) 
                
        else:
            print('That letter doesn\'t appear in the word')
            remaningChance -= 1                                                       #wrong character
            guessed_char_list.append(guess_char)
            
           
    #inside while loop over (for 8 chances)
                
    if "-" in result:
        print("You lost!")
        
    while True:
        choice = input("Type \"play\" to play the game, \"exit\" to quit:")
        if choice == "play":
            condition = True
            break
        elif choice == "exit":
            condition = False
            break 
