import random

def guessing_game():
    answer = random.randint(0, 100)
    new_base = random.choice((2, 8, 10, 16))
    while True:
        user_guess = int(input('What is your guess?\n'), new_base)

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')


guessing_game()


