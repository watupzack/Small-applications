import random

print("Welcome to the Guessing Number game.")
print("Try to guess the number that computer has chosen (from 1 to 30)\nYou will have just 5 attempts to do it.")
randomed_number = random.randint(1, 30)
attempts_remained = 5
attempts_done = 0

while attempts_remained:
    user_input = int(input())
    attempts_done += 1
    attempts_remained -= 1
    if user_input == randomed_number:
        print("Allright, you won!")
        print("It took you {0} attempt(s)".format(attempts_done))
        break
    if attempts_remained == 0:
        print("Game Over! The randomed number was -- {0}".format(randomed_number))
        break
    if randomed_number < user_input:
        print("Wrong. Try a smaller number. {0} attempt(s) left".format(attempts_remained))
    elif randomed_number > user_input:
        print("Wrong. Try a bigger number. {0} attempt(s) left".format(attempts_remained))
