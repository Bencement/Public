# Szamologep
print("Számológép")
szam1 = int(input("Add meg az első egész számot:\t"))
szam2 = int(input("Add meg a második egész számot:\t"))
print("Add meg a műveletet: (+, -, *, /)")
muvelet = input()
if muvelet == "+":
    print(szam1 + szam2)
elif muvelet == "-":
    print(szam1 - szam2)
elif muvelet == "*":
    print(szam1 * szam2)
elif muvelet == "/":
    print(szam1 / szam2)
else:
    print("Hiba!")
