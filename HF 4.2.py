import random
import json
import datetime

current_time = datetime.datetime.now()

print(current_time)

with open("score_list2.json", "r") as score_file:
    score_list = json.loads(score_file.read())

secret = random.randint(0, 30)
attempt = 0
for score_dict in score_list:
    print("Név: " + score_dict["player_name"] + " titkos szám: " + str(score_dict["secret_num"]) + " kísérletek száma: "
          + str(score_dict["attempts"]) + " dátum: " + score_dict.get("date"))
    print("Rossz tippek:  ", score_dict["wrong_guesses"])

name = input("Add meg a neved: \t")

guess_list = []

while True:
    guess = int(input("Mi a titkos szám? (1 és 30 között)"))
    attempt += 1
    if guess == secret:
        print("Talált! A titkos szám " + str(secret))
        print("A kisérletek száma " + str(attempt))
        break
    elif guess > secret:
        print(f"Nem talált! A titkos szám kisebb.")
        guess_list.append(guess)
    elif guess < secret:
        print(f"Nem talált! A titkos szám nagyobb.")
        guess_list.append(guess)

if guess == secret:
    score_list.append({"player_name": name,
                       "attempts": attempt,
                       "secret_num": secret,
                       "date": str(datetime.datetime.now()),
                       "wrong_guesses": guess_list})

with open("score_list2.json", "w") as score_file:
    score_file.writelines(json.dumps(score_list))
