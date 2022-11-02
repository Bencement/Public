import random
import json
import datetime

current_time = datetime.datetime.now()

print(current_time)

with open("score_list3.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list_items = len(score_list)

secret = random.randint(0, 30)
attempt = 0
# Rendezés mutató-lista segítségével

mutat = []
mutatrend = []
for score_dict in score_list:
    mutat = mutat.append(score_dict["attempts"])

mutatrend = mutat.sort()
if score_list_items > 2:
    for i in mutatrend:
        poz = mutatrend[i]
        sor = mutat.index(poz)
        print("Név:" + str(score_list[sor]["player_name"]) + " titkos szám: " + str(score_list[sor]["secret_num"]) +
              " kísérletek száma: " + str(score_list[sor]["attempts"]) + " dátum: " + str(score_list[sor]["date"]))
        print("Rossz találatok: " + str(score_list[sor]["wrong_guesses"]))
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

with open("score_list3.json", "w") as score_file:
    score_file.writelines(json.dumps(score_list))
