import pickle

print("Oto program bez nazwy")
try:
    with open('bazadanych.txt','rb') as x:
        bazadanych = pickle.load(x)
except:
    bazadanych=[]

while 1:
    print("Opcje:")
    print("1-Dodaj imie")
    print("2-Usuń imie")
    print("3-Pokaż liste imion")
    print("4-Zapisz zmiany i zamknij program")
    
    odp=input()

    if odp == ("1"):
        imie=input("Tutaj możesz wpisac swoje imie:")
        bazadanych.append(imie)

    elif odp == ("2"):
        imie=input("Jakie imie chcesz usunąć:")
        if imie in bazadanych:
            bazadanych.remove(imie)
        else:
            print("Nie ma takiego imienia na liście")

    elif odp == ("3"):
        print("To twoja lista imion:")
        z=1
        for z, imie in enumerate(bazadanych):
            z+=1
            print("-------")
            print(z,imie)
        print("-------")

    elif odp == ("4") :
        with open('bazadanych.txt','wb') as y:
            pickle.dump(bazadanych,y)
        break
    
    else:
        print("Nie ma takiej opcji")