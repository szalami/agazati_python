#Faragó Csaba, 2022-11-09

def checkTemp(num):
    if num >= 0:
        return False
    else:
        return True
    
data = 0
temp = 0
while data != "vege":
     data = input("Hő: ")
     if data != "vege": 
            temp = int(data)
            check = checkTemp(temp)
            if check == False:
                print("Nem volt fagy")
            else:
                print("Fagy volt")


        
