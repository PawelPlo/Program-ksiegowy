import pprint
saldo=0
konto=0
konto=float(konto)
linia_kredytowa = 0
linia_kredytowa = float(linia_kredytowa)
#zmienic potem debet na zmienna
debet = 100
print("     Program księgowy      \n")
print("Aktualny stan konta wynosi:{} zl.\n".format(konto))

#pprint.pprint()

while True:
    print('''Wybierz opcje:
    Linia kredytowa - wpisz: 1
    Saldo (operacje na koncie) - wpisz: 2
    Stan magazynu (dane calosciowe) - wpisz: 3
    Znajdz produkt w magazynie - wpisz: 4
    Sprzedaz - wpisz: 5
    Zakup - wpisz: 6
    Historia zdarzen - wpisz: 7
    Wyjscie z programu - wpisz: "koniec"''')
    wybor=input()
    if wybor=="1":
        print("Linia kredytowa")
        print("Linia kredytowa wynosi {} zl".format(linia_kredytowa))
        print("Dostepna linia kredytowa wynosi {} zl".format(linia_kredytowa-debet))
        print("Aktualny stan zadluzenia wynosi {} zl".format(debet))
        while True:
            print("Czy chcesz wprowadzic wartosc udzielonego kredytu? t/n")
            print("n - powrot do glownego menu")
            odp1=input()
            odp1 = odp1.lower()
            if odp1=="t":
                kredyt = input("Wpisz wartosc udzielonego kredytu obrotowego:")
                kredyt = float(kredyt)
                linia_kredytowa += kredyt
                print("Linia kredytowa wynosi {} zl".format(linia_kredytowa))
                print("Dostepna linia kredytowa wynosi {} zl".format(linia_kredytowa - debet))
                print("Aktualny stan zadluzenia wynosi {} zl".format(debet))
            elif odp1=="n":
                break
                wybor = input()
            else:
                print("Wybrales zla opcje")
                continue
    if wybor=="2":
        print("Saldo magazynu")
    if wybor=="3":
        print("Stan magazynu")
    if wybor=="4":
        print("Wpisz nazwe produktu")
    if wybor=="5":
        print("Sprzedaz")
    if wybor=="6":
        print("Zakup")
    if wybor=="7":
        print("Historia zdarzen")
    if wybor=="koniec":
        break


