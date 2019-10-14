from random import randint
#GET GUESS
def get_guess():
    return list(input("what is your guess?"))


# GENERATE COMP CODE
def generate_code():
    digits = []
    for n in range(3):
        digits.append(str(randint(0,9)))
    return list(digits)
code = generate_code()
print(code)

# GENERATE CLUES
def generate_clues(code, user_guess):
    if user_guess == code:
        return"CODE CRACKED!"
    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("MATCH")
        elif num in code:
            clues.append("CLOSE")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN GAME LOGIC
print("Welcome to Code Breaker!")
secret_code = generate_code()
clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()
    print(guess)
    clue_report = generate_clues(secret_code,guess)
    print("here is the result of your guess: ")

    for clue in clue_report:
        print(clue)
