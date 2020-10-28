import os
import time
clear = lambda: os.system('cls')
while 1:
    print("Witaj, w programie bez nazwy")
    print("1-zarejestruj się")
    print("2-zaloguj się")
    print("3-zamknij program")
    choice=input()
    choice=int(choice)
    clear()
    time.sleep(1)
    plik = open("bazadanych.txt",'r+')
    if choice == 1:
        while 1:
            rlogin=input("Podaj login: ")
            if rlogin in ("bazadanych.txt"):
                print("Login zajęty")
                clear()
                time.sleep(1)
            else:
                rpassword=input("Podaj hasło: ")
                rpasswordAgree=input("Podaj hasło ponownie: ")
                if rpassword == rpasswordAgree:
                    print("Zostałeś zarejetrowany")
                    plik.write(rlogin)
                    plik.write(rpassword)
                else:
                    print("Hasła nie są takie same")
                    print("Spróbuj ponownie")
            break        
    elif choice==2:
        login=input("Podaj login: ")
        if login == rlogin:
            password=input("Podaj hasło:")
            if password == rpassword:
                print("Zalogowano pomyślnie")
            else:
                print("Hasło jest nie poprawne")
        else:
            print("Nie poprawny login")
            if password == rpassword:
                break

        bazav2={login:rlogin,password:rpassword}
    elif choice==3:
            try:
                plik.close()
                break
            except:
                break
    elif choice != 1 or choice != 2 or choice != 3:
        print("Nie znam tej funkcji, wybierz proszę od 1 - 3")
        time.sleep(1)
        clear()


