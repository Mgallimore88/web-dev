from random import randint

"""
guessing game - run python3 code_breaker.py in terminal then start guessing.
Nonesense clues will guide you to the winning combination!
"""
target = [randint(0, 9) for n in range(3)]

def return_target_numbers(target):
    numstring = ""
    for letter in str(target):
        if letter.isdigit():
            numstring += letter
        else:
            continue
    return numstring

target_numbers = str(return_target_numbers(target))

print("Hi, please guess a 3 digit number")

won = False
i = 0

while won == False:
    i+=1
    print(f"Enter guess({i})")
    guess = str(input())
    print(f"you guessed {guess}")

    if len(guess) != 3:
        print("guess a 3 digit number")
        continue

    if guess == target_numbers:
        print("You win!")
        won = True
        continue
    for n,number in enumerate(guess):
        if number == target_numbers[n]:
            print("Eggs for breakfast")
    if number in target_numbers:
        print("The wind blows strongly to the west")
print(f"Well done, you took {i} tries")
