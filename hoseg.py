#Faragó Csaba, 2022-11-09

def checkTemp(num):                     # létrehozok egy függvényt aminek átadok egy paramétert /ez esetben egy számot/
    if num >= 0:                        # ha nagyobb mint 0...
        return False                    # ...akkor False /hamis/ értéket küldök vissza
    else:                               # egyébként...
        return True                     # ...True /igaz/ értéket küld
    
data = 0                                # beállítom a kezdőértékét a változónak amit figyel majd a ciklus
temp = 0                                # a temp változónak is adok kezdőértéket /ebben tárolom majd a hőmérsékletet/
while data != "vege":                   # addig megy a ciklus amíg nem kap 'vége' jelet
     data = input("Hő: ")               # bekérem a hőmérsékleti adatot és eltárolom a data változóban
     if data != "vege":                 # ellenőrzöm hogy a felhasználó nem 'vege' adatot adott meg
            temp = int(data)            # bekérem a hőmérsékleti adatot amit a temp változóban tárolok
            check = checkTemp(temp)     # a check változó a függvény visszatérési értékét veszi fel, aminek átadtam az adatot vizsgálatra
            if check == False:          # ellenőrzöm a függvény visszatérési értékét, ha hamis akkor...
                print("Nem volt fagy")  # ...kiírom a neki megfelelő üzenetet
            else:                       # ha nem hamis akkor...
                print("Fagy volt")      # ...az ennek megfelelő üzit írom ki


        
