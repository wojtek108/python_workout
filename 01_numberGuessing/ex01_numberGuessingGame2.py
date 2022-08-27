
import random

def guessing_game():
    answer = random.randint(0, 100)
    n = 0
    while n < 3:
        user_guess = int(input('What is your guess?\n'))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')
        n = n + 1
    else:
        print('You are out of chances!')
guessing_game()

