import pprint
saldo=0
konto=0
konto=float(konto)
linia_kredytowa = 0
linia_kredytowa = float(linia_kredytowa)
stan_magazynu = dict()
#zmienic potem debet na zmienna
debet = 100
print("     Program księgowy      \n")
print("Aktualny stan konta wynosi:{} zl.\n".format(konto))

#pprint.pprint()

while True:
    print('''Wybierz opcje:
    Linia kredytowa - wpisz: 1
    Saldo i operacje na koncie - wpisz: 2
    Stan magazynu (dane calosciowe) - wpisz: 3
    Znajdz produkt w magazynie - wpisz: 4
    Sprzedaz - wpisz: 5
    Zakup - wpisz: 6
    Historia zdarzen - wpisz: 7
    Wyjscie z programu - wpisz: "koniec"''')
    wybor=input()
    #wpisac zabezpieczenie przed bledem
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
        print("Wybierz opcje?")
        while True:
            print("""\nWyswietl stan magazynu - wpisz: 1
Dodaj nowy produkt - wpisz: 2
Wykresl produkt z magazynu - wpisz: 3
Wroc do menu glownego - wpisz: 4""")
            #dodac odnajdywanie produktow
            wybor2=input()
            wybor2 = wybor2.lower()
            if wybor2=="1":
                print(stan_magazynu)
                powrot=input('Powrot do menu "Stan magazynu" - wybierz "Q":   ')
            if wybor2 == "2":
                while True:
                    produkt1 = input("\nWpisz nazwe nowego produktu:  ")
                    ilosc = input("Wpisz ilosc produktu:   ")
                    ilosc = float(ilosc)
                    cena = input("Wpisz cene produktu:  ")
                    cena = float(cena)
                    wartosc = ilosc * cena
                    wartosc = float(wartosc)
                    stan_magazynu[produkt1] = ilosc, cena, wartosc
                    print(stan_magazynu)
                    print("\nCzy chcesz wprowadzic kolejny produkt? t/n")
                    odp2 = input()
                    odp2 = odp2.lower()
                    if odp2 == "t":
                        continue
                    elif odp2 == "n":
                        break
                        wybor2 = input()
                    else:
                        print("Wybrales zla opcje")
                        continue
            if wybor2 == "3":
                while True:
                    produkt2 = input("\nWpisz nazwe nowego produktu do wykreslenia:  ")
                    #moze dac pytanie "Czy na pewno chcesz wykreslic?"
                    del stan_magazynu[produkt2]
                    print(stan_magazynu)
                    print("\nCzy chcesz wykreslic kolejny produkt? t/n")
                    odp3 = input()
                    odp3 = odp3.lower()
                    if odp2 == "t":
                        continue
                    elif odp2 == "n":
                        break
                        wybor2 = input()
                    else:
                        print("Wybrales zla opcje")
                        continue
            if wybor2 == "4":
                break
                wybor = input()
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


