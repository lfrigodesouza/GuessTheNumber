import random


def guess_the_number():
    print('Hello. What is yout name?')
    name = input()

    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    secret_number = random.randint(1, 20)

    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high')
        else:
            break

    if guess == secret_number:
        print('Good job, ' + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses')
    else:
        print('Nope, the number I was thinking of was ' + str(secret_number))


if __name__ == "__main__":
    guess_the_number()
