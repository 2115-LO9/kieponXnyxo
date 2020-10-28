import os
import time
clear = lambda: os.system('cls')
while 1:
    print("Witaj, w programie bez nazwy")
    print("1-zaloguj się")
    print("2-zarejestruj się")
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
                bazav2={login:rlogin,password:rpassword}
                print("Login zajęty")
                clear()
                time.sleep(1)
            else:
                plik.write(rlogin)
                rpassword=input("Podaj hasło: ")
                rpasswordAgree=input("Podaj hasło ponownie: ")
                if rpassword == rpasswordAgree:
                    print("Zostałeś zarejetrowany")
                else:
                    print("Hasła nie są takie same")
            break
    elif choice==2:
    login=input("Podaj login: ")
        if login != rlogin:
            print("Nie poprawny login")
        elif password != rpassword:
            password=input("Podaj hasło:")
            if password == rpassword:
                break
        print("Zalogowano pomyślnie")
    elif choice==3:
            try:
                plik.close()
            except:
                break
    else:
        print("Nie ma takiej opcji")