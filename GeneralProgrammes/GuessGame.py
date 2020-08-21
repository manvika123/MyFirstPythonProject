# generate a random number 1-10
from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# take input from the user


# check if the input is in range of 1 - 10
while True:
    try:
        guess = int(input('guess a number 1-10  '))

        if 0 <= guess <= 10:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey bozo, I said 1-10')
    except ValueError:
        print('Please enter a number')
        continue

# check if it is the correct guess. Otherwise ask again

