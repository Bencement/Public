import random
import json
import datetime

def filenyitas():
    with open("score_list_def.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

def veletlen_tartomany(mina=0, minb=30):
    secret = random.randint(mina, minb)
    return secret

attempt = 0

def adat_kiir():
    global score_dict
        for score_dict in score_list:
        print("Név: " + score_dict["player_name"] + " titkos szám: " + str(score_dict["secret_num"]) + " kísérletek száma: "
          + str(score_dict["attempts"]) + " dátum: " + score_dict.get("date"))
        print("Rossz tippek:  ", score_dict["wrong_guesses"])

def adat_beker():
    global name
    name = input("Add meg a neved: \t")

def talalgatas():
    global secret, attempt
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

def fileiras():
    with open("score_list_def.json", "w") as score_file:
        score_file.writelines(json.dumps(score_list))

filenyitas()
veletlen_tartomany()
adat_kiir()
adat_beker()
talalgatas()
fileiras()
