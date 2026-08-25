# simple programs of topics from 01-intro.py to 10-local-and-global-variables.py

# NUMBER GUESSING GAME :

def guessing_game():
    number = 7
    attempts = 0

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess == number:
            print("Correct!")
            print("Attempts:", attempts)
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

guessing_game()

