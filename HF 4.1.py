import random
import json
import datetime

current_time = datetime.datetime.now()

print(current_time)

with open("score_list1.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print(score_list)

secret = random.randint(0, 30)
attempt = 0
for score_dict in score_list:
    print("Név:" + score_dict["player_name"] + " titkos szám: " + str(score_dict["secret_num"]) + " kísérletek száma: "
          + str(score_dict["attempts"]) + " dátum: " + score_dict.get("date"))

name = input("Add meg a neved: \t")

while True:
    guess = int(input("Mi a titkos szám? (1 és 30 között)"))
    attempt += 1
    if guess == secret:
        print("Talált! A titkos szám " + str(secret))
        print("A kisérletek száma " + str(attempt))
        break
    elif guess > secret:
        print(f"Nem talált! A titkos szám kisebb.")
    elif guess < secret:
        print(f"Nem talált! A titkos szám nagyobb.")

if guess == secret:
    score_list.append({"player_name": name,
                       "attempts": attempt,
                       "secret_num": secret,
                       "date": str(datetime.datetime.now())})

with open("score_list1.json", "w") as score_file:
    score_file.writelines(json.dumps(score_list))
