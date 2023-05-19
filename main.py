#program ksiegowy

#zmienne do czesci 1 i 2 (Obsluga kredytow i saldo, stan konta, operacje gotowkowe)
saldo=0
konto=0
konto=float(konto)
zadluzenie = 0
zadluzenie = float(zadluzenie)

#zmienne i funkcje do stanu magazynu
stan_magazynu = dict()
def zapasy(stan_magazynu):
    suma = 0
    for v in stan_magazynu.values():
        suma += v["wartosc"]
    return suma

#zmienne do historii zdarzen
historia = []
historia_index=0


print("     Program księgowy      \n")
print("Aktualny stan konta wynosi:{} zl.\n".format(konto))

while True:
    print('''Wybierz opcje:
    Obsluga kredytow - wpisz: 1
    Saldo, stan konta i operacje gotowkowe - wpisz: 2
    Stan magazynu (dane calosciowe, wprowadzanie i wykreslanie towarow) - wpisz: 3
    Znajdz produkt w magazynie - wpisz: 4
    Sprzedaz - wpisz: 5
    Zakup - wpisz: 6
    Historia zdarzen - wpisz: 7
    Wyjscie z programu - wpisz: "koniec"''')
    wybor=input()
    if wybor=="1":
        while True:
            print("Obsluga kredytow - Aktualny stan zadluzenia wynosi {} zl\n".format(zadluzenie))
            print("""Wprowadzenie wartosci uruchomionego kredytu - wpisz: 1
Splata kredytu - wpisz: 2
Powrot do glownego menu  - wpisz: 3""")
            odp1=input()
            if odp1=="1":
                kredyt = input("Wpisz wartosc udzielonego Ci kredytu:")
                kredyt = float(kredyt)
                zadluzenie += kredyt
                print("Stan zadluzenia po zmianie wynosi {} zl".format(zadluzenie))
                historia_index = historia_index + 1
                wpis_1_1 = ("{}. Zaciagniety kredyt w wysokosci: {} zl".format(historia_index, kredyt))
                historia.append(wpis_1_1)
                konto = konto + kredyt
                continue
            if odp1=="2":
                kredyt = input("Wpisz kwote splaconego kredytu:")
                kredyt = float(kredyt)
                if kredyt > konto:
                    print("Nie masz wystarczajacych srodkow na koncie\n\n")
                    continue
                    wybor == "1"
                if kredyt <= konto:
                    zadluzenie -= kredyt
                    konto = konto - kredyt
                    print("Stan zadluzenia po zmianie wynosi {} zl\n".format(zadluzenie))
                    historia_index = historia_index + 1
                    wpis_1_2 = ("{}. Splata kredytu w wysokosci: {} zl".format(historia_index, kredyt))
                    historia.append(wpis_1_2)
                    continue
            if odp1=="3":
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
            print("Wysokosc zadluzenia wynosi {} zl".format(zadluzenie))
            print("Saldo firmy pomniejszone o wysokosc zadluzenia wynosi {} zl\n"
                  .format(wartosc_zapasow+konto-zadluzenie))
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
            print("Stan magazynu - wybierz opcje")
            print("""\nWyswietl stan magazynu - wpisz: 1
Dodaj nowy produkt - wpisz: 2
Wykresl produkt z magazynu - wpisz: 3
Wroc do menu glownego - wpisz: 4""")
            wybor3=input()
            wybor3 = wybor3.lower()
            if wybor3=="1":
                print(stan_magazynu)
                powrot=input('Powrot do menu "Stan magazynu" - wybierz "Q":   ')
                wybor == "3"
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
                    historia_index = historia_index + 1
                    wpis_3_1 = ("{}. Wprowadzono do magazynu {}, w ilosci {}, po cenie {} zl"
                                .format(historia_index, produkt, ilosc, cena))
                    historia.append(wpis_3_1)
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
                    if produkt not in stan_magazynu:
                        print("Nie ma takiego produktu w magazynie")
                        print("\nCzy chcesz wykreslic kolejny produkt? t/n")
                        odp3_1 = input()
                        odp3_1 = odp3_1.lower()
                        if odp3_1 == "t":
                            continue
                        if odp3_1 == "n":
                            break
                            wybor == 3
                    if produkt in stan_magazynu:
                        print(stan_magazynu[produkt])
                        potwierdzenie=input("\nCzy na pewno chcesz wykrelic ten produkt? t/n   ")
                        potwierdzenie=potwierdzenie.lower()
                        if potwierdzenie == "t":
                            historia_index = historia_index + 1
                            wpis_3_2 = ("{}. Ze stanu magazynu magazynu zdjeto {} - {}"
                            .format(historia_index, produkt, stan_magazynu[produkt]))
                            historia.append(wpis_3_2)
                            del stan_magazynu[produkt]
                            print("\nCzy chcesz wykreslic kolejny produkt? t/n")
                            odp3_2 = input()
                            odp3_2 = odp3_2.lower()
                            if odp3_2 == "t":
                                continue
                            if odp3_2 == "n":
                                break
                                wybor==3
                        if potwierdzenie == "n":
                            continue
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
                elif powrot4 == "n":
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
        while True:
            print("""Sprzedaz - wpisz: 1
Wroc do menu glownego - wpisz: 2""")
            odp_5 = input()
            if odp_5 == "1":
                przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ")
                if przedmiot_sprzadazy not in stan_magazynu:
                    print("Takiego towaru nie ma magazynie. Powrot do menu\n")
                    continue
                    przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ")
                if przedmiot_sprzadazy in stan_magazynu:
                    print("Aktualny stan w magazynie:\n")
                    print(przedmiot_sprzadazy, stan_magazynu[przedmiot_sprzadazy])
                    ilosc_sprzedawana = input("Podaj ilosc sprzedawanego towaru:   ")
                    ilosc_sprzedawana = float(ilosc_sprzedawana)
                    cena_sprzedazy = input("Podaj cene sprzedazy:   ")
                    cena_sprzedazy = float(cena_sprzedazy)
                    wartosc_sprzedazy = ilosc_sprzedawana * cena_sprzedazy
                    wartosc_sprzedazy = float(wartosc_sprzedazy)
                    if ilosc_sprzedawana > stan_magazynu[przedmiot_sprzadazy]["ilosc"]:
                        print("W magazynie nie masz takiej ilosci {}\n".format(przedmiot_sprzadazy))
                        continue
                        przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ")
                    else:
                        if cena_sprzedazy == stan_magazynu[przedmiot_sprzadazy]["cena"]:
                            stan_magazynu[przedmiot_sprzadazy]["ilosc"] -= ilosc_sprzedawana
                            stan_magazynu[przedmiot_sprzadazy]["wartosc"] -= wartosc_sprzedazy
                            print(przedmiot_sprzadazy, stan_magazynu[przedmiot_sprzadazy])
                            historia_index = historia_index + 1
                            wpis_5_1 = ("{}. Sprzedano {}, w ilosci {}, po cenie {} zl"
                            .format(historia_index, przedmiot_sprzadazy, ilosc_sprzedawana, cena_sprzedazy))
                            historia.append(wpis_5_1)
                            konto = konto + wartosc_sprzedazy
                            print("\nCzy chcesz sprzedac kolejny produkt? t/n")
                            odp5_1 = input()
                            odp5_1 = odp5_1.lower()
                            if odp5_1 == "t":
                                continue
                            elif odp5_1 == "n":
                                break
                                odp_5 = input()
                            else:
                                print("Wybrales zla opcje")
                                continue
                        if cena_sprzedazy != stan_magazynu[przedmiot_sprzadazy]["cena"]:
                            stan_magazynu[przedmiot_sprzadazy]["ilosc"] -= ilosc_sprzedawana
                            stara_wartosc = ilosc_sprzedawana * stan_magazynu[przedmiot_sprzadazy]["cena"]
                            stan_magazynu[przedmiot_sprzadazy]["wartosc"] -= stara_wartosc
                            print("Aktualny stan w magazynie:", przedmiot_sprzadazy, stan_magazynu[przedmiot_sprzadazy])
                            zysk = wartosc_sprzedazy - stara_wartosc
                            print("Ze sprzedazy {} osignales zysk w wysokości {} zl.".format(przedmiot_sprzadazy, zysk))
                            historia_index = historia_index + 1
                            wpis_5_2 = ("{}. Sprzedano {}, w ilosci {}, po cenie {} zl"
                            .format(historia_index, przedmiot_sprzadazy, ilosc_sprzedawana, cena_sprzedazy))
                            historia.append(wpis_5_2)
                            konto = konto + wartosc_sprzedazy
                            print("\nCzy chcesz sprzedac kolejny produkt? t/n")
                            odp5_2 = input()
                            odp5_2 = odp5_2.lower()
                            if odp5_2 == "t":
                                continue
                            elif odp5_2 == "n":
                                break
                                odp_5 = input()
                            else:
                                print("Wybrales zla opcje")
                                continue
            if odp_5 == "2":
                break
                wybor = input()
            else:
                print("Wybrales zla opcje")
                continue
    if wybor=="6":
        while True:
            print("Zakup towarow. Aktualny stan konta wynosi {} zl\n".format(konto))
            print("""Zakup towaru wystepujacego juz w magazynie - wpisz: 1
Zakup towaru nie wystepujacego dotad w magazynie - wpisz: 2
Powrot do menu glownego - wpisz: 3""")
            opcja_zakupu = input()
            if opcja_zakupu == "1":
                zakup = input("\nWpisz nazwe towaru:  ")
                if zakup not in stan_magazynu:
                    print("Takiego towaru nie ma magazynie. Powrot do menu\n")
                    continue
                    opcja_zakupu = input()
                if zakup in stan_magazynu:
                    print("Aktualny stan w magazynie:\n")
                    print(zakup, stan_magazynu[zakup])
                    ilosc_kupowana = input("Podaj ilosc kupowanego towaru:   ")
                    ilosc_kupowana = float(ilosc_kupowana)
                    cena_kupna = input("Podaj cene kupna:   ")
                    cena_kupna = float(cena_kupna)
                    wartosc_zakupu = ilosc_kupowana * cena_kupna
                    wartosc_zakupu = float(wartosc_zakupu)
                    if wartosc_zakupu > konto:
                        print("Nie masz wystarczajcych srodkow na koncie\n")
                        continue
                        opcja_zakupu = input()
                    else:
                        if cena_kupna != stan_magazynu[zakup]["cena"]:
                            print("{} w magazynie ma inna cene. Wprowadz kupowany towar jako nowa pozycja w magazynie"
                            .format(zakup))
                            continue
                            opcja_zakupu = input()
                        elif cena_kupna == stan_magazynu[zakup]["cena"]:
                            stan_magazynu[zakup]["ilosc"] += ilosc_kupowana
                            stan_magazynu[zakup]["wartosc"] += wartosc_zakupu
                            print(zakup, stan_magazynu[zakup])
                            historia_index = historia_index + 1
                            wpis_6_1 = ("{}. Zakupiono {}, w ilosci {}, po cenie {} zl"
                                     .format(historia_index, zakup, ilosc_kupowana, cena_kupna))
                            historia.append(wpis_6_1)
                            konto = konto - wartosc_zakupu
                            print("\nCzy chcesz zakupic kolejny produkt? t/n")
                            odp6_1 = input()
                            odp6_1 = odp6_1.lower()
                            if odp6_1 == "t":
                                continue
                            elif odp6_1 == "n":
                                break
                                wybor6 = input()
                            else:
                                print("Wybrales zla opcje")
                                continue
            if opcja_zakupu == "2":
                produkt = input("\nWpisz nazwe nowego produktu:  ")
                if produkt in stan_magazynu:
                    print("Taki towar znajduje sie juz w magazynie. Powrot do menu\n")
                    continue
                    opcja_zakupu = input()
                if produkt not in stan_magazynu:
                    ilosc = input("Wpisz ilosc produktu:   ")
                    ilosc = float(ilosc)
                    cena = input("Wpisz cene produktu:  ")
                    cena = float(cena)
                    wartosc = ilosc * cena
                    wartosc = float(wartosc)
                    if wartosc > konto:
                        print("Nie masz wystarczajcych srodkow na koncie\n")
                        continue
                        opcja_zakupu = input()
                    else:
                        stan_magazynu[produkt] = {"ilosc": ilosc, "cena": cena, "wartosc": wartosc}
                        print("Zakupiono towar :{}, w ilosci: {}, w cenie: {}, laczna wartosc: {}".
                            format(produkt, ilosc, cena, wartosc))
                        historia_index = historia_index + 1
                        wpis_6_2 = ("{}. Zakupiono {}, w ilosci {}, po cenie {} zl"
                            .format(historia_index, produkt, ilosc, cena))
                        historia.append(wpis_6_2)
                        konto = konto - wartosc
                        print("\nCzy chcesz zakupic kolejny produkt? t/n")
                        odp6_2 = input()
                        odp6_2 = odp6_2.lower()
                        if odp6_2 == "t":
                            continue
                        elif odp6_2 == "n":
                            break
                            wybor6 = input()
                        else:
                            print("Wybrales zla opcje")
                            continue
            if opcja_zakupu == "3":
                break
                wybor = input()
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
            else:
                print("Wybrales zla opcje")
                continue
    if wybor=="koniec":
        break
    else:
        print("Wybrales zla opcje")
        continue


