import random


words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
result = list(len(random_word) * '-')


print("H A N G M A N")

for _x in range(8):
    print()
    print(''.join(result))
    guess = input("Input a letter: ")
    if guess in random_word:
        for letter_num in range(len(random_word)):
            if guess == random_word[letter_num]:
                result[letter_num] = guess
    else:
        print('No such letter in the word')

print()
print("Thanks for playing!")
print("We'll see how well you did in the next stage")
