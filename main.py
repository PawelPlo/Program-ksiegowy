#import pprint
saldo=0
konto=0
konto=float(konto)
linia_kredytowa = 0
linia_kredytowa = float(linia_kredytowa)
stan_magazynu = dict()
#zmienic potem debet na zmienna
debet = 100
def zapasy(stan_magazynu):
    suma = 0
    for v in stan_magazynu.values():
        suma += v["wartosc"]
    return suma
historia = []
historia_index=0
print("     Program księgowy      \n")
print("Aktualny stan konta wynosi:{} zl.\n".format(konto))

while True:
    print('''Wybierz opcje:
    Linia kredytowa - wpisz: 1
    Saldo, stan konta i operacje gotowkowe - wpisz: 2
    Stan magazynu (dane calosciowe, wprowadzanie i wykreslanie towarow) - wpisz: 3
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
        while True:
            print("Saldo magazynu\n")
            wartosc_zapasow=zapasy(stan_magazynu)
            print("Wartosc towarow w magazynie wynosi: {} zl".format(wartosc_zapasow))
            print("Stan konta: {} zl".format(konto))
            print("Wysokosc zadluzenia wynosi {} zl".format(debet))
            print("Saldo firmy pomniejszone o wysokosc zadluzenia wynosi {} zl\n".format(wartosc_zapasow+konto-debet))
            print("""Jesli chcesz wplacic srodki na konto - wpisz: 1
Jesli chcesz wyplacic srodki z konta - wpisz: 2
Powrot do menu glownego - wpisz: 3""")
            wybor2=input()
            if wybor2=="1":
                wplata=input("Podaj kwote wplaty na konto w PLN:   ")
                wplata=int(wplata)
                konto = konto+wplata
                print("\nStan konta wynosi: {}".format(konto))
                historia_index=historia_index + 1
                wpis_2=("{}. Wplata wlasna na konto: {} zl".format(historia_index,wplata))
                historia.append(wpis_2)
                continue
            if wybor2=="2":
                pass
            if wybor2 == "3":
                break
                wybor = input()
            else:
                print("Wybrales zla opcje")
                continue
#rozwinac wybor2
    if wybor=="3":
        while True:
            print("Stan magazynu\n")
            print("Wybierz opcje?")
            print("""\nWyswietl stan magazynu - wpisz: 1
Dodaj nowy produkt - wpisz: 2
Wykresl produkt z magazynu - wpisz: 3
Wroc do menu glownego - wpisz: 4""")
            wybor3=input()
            wybor3 = wybor3.lower()
            if wybor3=="1":
                print(stan_magazynu)
                powrot=input('Powrot do menu "Stan magazynu" - wybierz "Q":   ')
            if wybor3 == "2":
                while True:
                    produkt = input("\nWpisz nazwe nowego produktu:  ")
                    ilosc = input("Wpisz ilosc produktu:   ")
                    ilosc = float(ilosc)
                    cena = input("Wpisz cene produktu:  ")
                    cena = float(cena)
                    wartosc = ilosc * cena
                    wartosc = float(wartosc)
                    stan_magazynu[produkt] = {"ilosc": ilosc, "cena": cena, "wartosc": wartosc}
                    print("Wprowadzono towar :{}, w ilosci: {}, w cenie: {}, laczna wartosc: {}".format(produkt, ilosc, cena, wartosc))
                    print("\nCzy chcesz wprowadzic kolejny produkt? t/n")
                    odp2 = input()
                    odp2 = odp2.lower()
                    if odp2 == "t":
                        continue
                    elif odp2 == "n":
                        break
                        wybor3 = input()
                    else:
                        print("Wybrales zla opcje")
                        continue
            if wybor3 == "3":
                while True:
                    produkt = input("\nWpisz nazwe nowego produktu do wykreslenia:  ")
#moze dac pytanie "Czy na pewno chcesz wykreslic?"
                    del stan_magazynu[produkt]
                    print(stan_magazynu)
                    print("\nCzy chcesz wykreslic kolejny produkt? t/n")
                    odp3 = input()
                    odp3 = odp3.lower()
                    if odp3 == "t":
                        continue
                    elif odp3 == "n":
                        break
                        wybor3 = input()
                    else:
                        print("Wybrales zla opcje")
                        continue
            if wybor3 == "4":
                break
                wybor = input()
    if wybor=="4":
        while True:
            szukana=input("Wpisz szukany towar:  ")
            if szukana in stan_magazynu:
                print(szukana, stan_magazynu[szukana])
                powrot4 = input("Czy chcesz szukac innego towaru? t/n:    ")
                powrot4 = powrot4.lower()
                if powrot4 == "t":
                    continue
                elif powrot == "n":
                    break
                    wybor4 = input()
                else:
                    print("Wybrales zla opcje")
                    continue
            if szukana not in stan_magazynu:
                odp4=input("""W magazynie nie odnaleziono takiego towaru!
Czy chcesz szukac innego towaru? t/n:    """)
                odp4 = odp4.lower()
                if odp4=="t":
                    continue
                elif odp4=="n":
                    break
                    wybor = input()
                else:
                    print("Wybrales zla opcje")
                    continue
    if wybor=="5":
        print("Sprzedaz")
    if wybor=="6":
        print("Zakup towarow")
    if wybor=="7":
        while True:
            print("Historia zdarzen\n")
            print("""Pelna historia zdarzen - wpisz: 1
Wybor zakresu z histori zdarzen - wpisz: 2
Powrot do glownego menu - wpisz: 3""")
            wybor7 = input()
            if wybor7 == "1":
                print(historia)
                powrot7=input('Wpisz "Q" aby wrocic do menu "Historia zdarzen":   ')
                powrot7=powrot7.lower()
                if powrot7=="q":
                    continue
                    wybor7 = input()
                else:
                    continue
                    wybor7 = input()
            if wybor7 == "2":
                od=input("Wprowadz poczatkowy numer z listy:   ")
                od = int(od)
                od = od-1
                do=input("Wprowadz koncowy numer z listy:    ")
                do = int(do)
                do=do+1
                for zakres in range(od, do):
                    print(historia[zakres])
                powrot7=input('Powrot do menu "Historia zdarzen" - wpisz: "q"')
            if wybor7 == "3":
                break
                wybor = input()
    if wybor=="koniec":
        break


