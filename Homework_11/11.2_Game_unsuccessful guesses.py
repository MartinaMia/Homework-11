import json
import random

import datetime
current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []                                  # Liste für falsche Versuche vor der Schleife

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:                       # Verbesserte Schreibweise der Ergebnisausgabe
    score_text = "{0}: {1} attempts, date: {2}, secret number: {3}, wrong guesses: {4}".format(score_dict["name"],  #{0}
          str(score_dict["attempts"]),      #{1}
          score_dict.get("date"),           #{2}
          str(score_dict["secret number"]), #{3}
          str(score_dict["wrong guesses"])) #{4}
    print(score_text)

users_name = input("Please enter your name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    wrong_guesses.append(guess)                     # Falsche Versuche in Liste sammeln
    if guess == secret:
        score_list.append({"attempts": attempts,
                           "date": str(datetime.datetime.now()),
                           "name": users_name,
                           "secret number": str(secret),
                           "wrong guesses": wrong_guesses}) # dem Dict. hinzufügen
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")