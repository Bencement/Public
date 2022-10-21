# FIZZ-BUZZ program

szam = int(input("Adjon meg egy egész számot 1-tól 100-ig!"))

for i in range(1, szam+1):
    if i%3 != 0 and i%5 != 0:
        print(i)
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    else:
        if i%3 == 0:
            print("fizz")
        if i%5 == 0:
            print("buzz")

# programvég
