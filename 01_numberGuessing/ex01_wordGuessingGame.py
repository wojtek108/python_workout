import random


dic = []
with open('oxford3000.txt', 'r') as a_file:
    for line in a_file:
        stripped_line = line.strip()
        dic.append(stripped_line)

dic2 = [item for item in dic if len(item) <= 5 and len(item) >= 2]

# The solution of Reuven is very nice. Great example of list comprehension. 
# 
# WORDS = [one_word.strip()
#          for one_word in open('words.txt')]
# 

def word_guessing():
    sel_word = random.choice(dic2)
    print(sel_word)

    while True:
        user_guess =input('Give me a word with 2-5 letters: ')

        if user_guess == sel_word:
            print(f'Your guess of {user_guess} is correct!')
            break
        if user_guess < sel_word:
            print('Start with a later letter')
        if user_guess > sel_word:
            print('Start with an earlier letter')

word_guessing()
