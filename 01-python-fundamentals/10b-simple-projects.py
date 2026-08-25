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


# SIMPLE QUIZ GAME :

def quiz():
    score = 0

    questions = ["What is 5 + 5?", "What is 10 - 3?", "What is 4 * 2?"]

    answers = ["10", "7", "8"]

    for i in range(3):
        print(questions[i])

        answer = input("Your answer: ")

        if answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("Your score is:", score)


quiz()
