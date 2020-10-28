import pickle
import os
import time
##zdefiniowanie funkcji do czyszczenia ekranu
clear = lambda: os.system('cls')

print("Witaj w księdze imion.")
try:
    with open('bazadanych.txt','rb') as x:
        bazadanych = pickle.load(x)
except:
    bazadanych=[]

while 1:
    time.sleep(1)
    clear()
    print("Opcje:")
    print("1-Dodaj imie")
    print("2-Usuń imie")
    print("3-Pokaż liste imion")
    print("4-Zapisz zmiany i zamknij program")
    
    odp=input()

    if odp == ("1"):
        imie=input("Tutaj możesz wpisac swoje imie:")
        bazadanych.append(imie)
        time.sleep(1)
        clear()

    elif odp == ("2"):
        imie=input("Jakie imie chcesz usunąć:")
        if imie in bazadanych:
            bazadanych.remove(imie)
        else:
            clear()
            print("Nie ma takiego imienia na liście")
            time.sleep(1)

    elif odp == ("3"):
        clear()
        print("To twoja lista imion:")
        z=1
        for z, imie in enumerate(bazadanych):
            z+=1
            print("-------")
            print(z,imie)
        print("-------")
        programPause = input("Aby wrócić do menu wciśnij enter")

    elif odp == ("4") :
        with open('bazadanych.txt','wb') as y:
            pickle.dump(bazadanych,y)
        break
    
    else:
        clear()
        print("Nie ma takiej opcji")
        time.sleep(2)