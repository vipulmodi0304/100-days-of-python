import random

def play_game(chances):
    number = random.randint(1,100)
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Correct guess!")
            return
        elif guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        chances -= 1
    print(f"No chances left. You lose :( The number was {number}!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")

if difficulty == 'easy':
    play_game(10)
elif difficulty == 'hard':
    play_game(5)
else:
    print("Invalid input")
