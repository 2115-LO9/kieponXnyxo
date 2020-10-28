import os
import time
clear = lambda: os.system('cls')
while 1:
    print("Witaj, w programie bez nazwy")
    print("1-zaloguj się")
    print("2-zarejestruj się")
    print("3-zamknij program")
    odp1=input()
    clear()
    time.sleep(1)
    if odp1 == 1:
        plik = open("bazadanych.txt",'r+')
        odp2=input("Podaj login: ")
        if x!= odp2:
            print("Nie poprawny login")
        elif x==odp2:
            odp3=input("Podaj hasło:")
            if y==odp2:
                break
    elif odp1==2:
        while 1:
            baza.v2={x:login,y:hasło}
            odp1=input("Podaj login: ")
            if odp1 in bazadanych.txt:
                print("Login zajęty")
                clear()
                time.sleep(1)
            else:
                plik=write("bazadanych.txt",'a+')
                break
            while 1:
                    odp2=input("Podaj hasło: ")
                    odp3=input("Podaj hasło ponownie: ")
                    if odp2 == odp3:
                        print("Zostałeś zarejetrowany")
                    else:
                        print("Hasła nie są takie same")
    elif odp1==3:
            plik.close()
            break
    else:
        print("Nie ma takiej opcji")

