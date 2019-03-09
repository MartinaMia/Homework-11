import json
import random

import datetime
current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print(score_dict["name"] + ": " +                               # im 2. Schritt festlegen, wie die neuen Dict.
          str(score_dict["attempts"]) + " attempts, date: " +        # Angaben ausgegeben werden sollen
          score_dict.get("date") + ", secret number: " +
          str(score_dict["secret number"]))

users_name = input("Please enter your name: ")                      # Aufforderung zur Namenseingabe vor der Schleife

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    if guess == secret:
        score_list.append({"attempts": attempts,
                           "date": str(datetime.datetime.now()),
                           "name": users_name,                      # im 1. Schritt zum Dict. hinzufügen
                           "secret number": str(secret)})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")