import random

n = random.randint(0, 100)
while True:
    a = int(input('Guess: '))
    if a == n:
        print('Great!')
        break
    elif a > n:
        print('You did not guess! The number is greater than guessed one!')
    else:
        print('You did not guess! The number is less than guessed one!')
