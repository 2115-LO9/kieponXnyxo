import os

clear = lambda: os.system('cls')


print("Testowa baza danych")
x=input("Podaj swój login")
imie=input("A teraz wpisz swoje imie")
testowabaza = {x: imie}
clear()
print("Jeśli chcesz wczytać listę imion podaj swój login ")
loginTest= input()
if loginTest == x:
    print(testowabaza[x])
