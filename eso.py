#Faragó Csaba, 2022-11-09

print("Faragó Csaba, 2022-11-09")
print("Csapadék mennyisége miliméterben:")
actual = int(input("Aktuális heti csapadék: "))
prev = int(input("Előző heti csapadék: "))

if actual > prev:
    print("Több csapadék")
elif actual < prev:
    print("Kevesebb csapadék")
else:
    print("Nem változott a csapadék mennyisége")