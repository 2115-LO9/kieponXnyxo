import os
import time
clear = lambda: os.system('cls')
while 1:
    print("Witaj, w programie bez nazwy")
    print("1-zarejestruj się")
    print("2-zaloguj się")
    print("3-zamknij program")
    odp1=input()
    odp1=int(odp1)
    clear()
    time.sleep(1)
    plik = open("bazadanych.txt",'r+')
    if odp1 == 1:
        odp2=input("Podaj login: ")
        if x!= odp2:
            print("Nie poprawny login")
        elif x==odp2:
            odp3=input("Podaj hasło:")
            if y==odp2:
                break
    elif odp1==2:
        while 1:
            x=input("Podaj login: ")
            try:
                if x in bazav2:
                    print("Login zajęty")
                    clear()
                    time.sleep(1)
                else:
                    plik = open("bazadanych.txt",'r+')
                    break
        while 1:
            odp2=input("Podaj hasło: ")
            odp3=input("Podaj hasło ponownie: ")
            if odp2 == odp3:
                print("Zostałeś zarejetrowany")
                plik=write("bazadanych",'a+')
                bazav2={x:login,y:hasło}
                break
            else:
                print("Hasła nie są takie same")         
    elif odp1==3:
            plik.close()
            break
    else:
        print("Nie ma takiej opcji")
