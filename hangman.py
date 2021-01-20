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

    result = list(len(selected_word) * '-') 
    remaningChance = int(8)    
   
    guessed_char_list = []
    
    while remaningChance > 0 :
        print()
        print(''.join(result))
        guess_char = input("Input a letter: ")
        
        if "-" not in result:
            print("""You guessed the word!
            You survived!""")
            break  
        
        elif len(guess_char) != 1:
            print("You should input a single letter")
            continue  
        
        elif guess_char.isupper() or guess_char.isalpha() == 0:
            print("Please enter a lowercase English letter")
            continue
        
        elif guess_char in guessed_char_list:
            print("You've already guessed this letter")
            
            if guessed_char_list.count(guess_char) <= int(2):
                continue    
            else:
                remaningChance -= 1 
                continue   
            
        if guess_char in selected_word:
            for letter_num in range(len(selected_word)):
                if guess_char == selected_word[letter_num]:
                    result[letter_num] = guess_char
            guessed_char_list.append(guess_char) 
                
        else:
            print('That letter doesn\'t appear in the word')
            remaningChance -= 1
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
