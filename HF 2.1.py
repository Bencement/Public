# km -> mile átváltó program
print("Üdvözlöm. Ez a program a km-ben megadott távolságot mérföldre váltja.")
print("---------------------------------------------------------------------")

konv = 0.62137


while True:
    kilometer = float(input("Az adott távolság:\t"))
    merfold = konv*kilometer
    print(merfold)
    billentyu = input("Szeretne új adatot bevinni? Ha igen, nyomja meg az i billentyűt!")

    if billentyu != "i":
        break

print("Viszontlátásra! Köszönöm, hogy segíthettem!")
