"""Program ksiegowy
W menu glownym mozna wybrac 8 opcji:

Obsluga kredytow (1)
    W tej części można zaciągać i spłacać kredyty, co znajduje odzwierciedlenie w stanie konta firmy. W przypadku spłaty
    kredytu w kwocie przewyższającej stan konta, program zglośi błąd.
    Akcje wykonane w tej części są zapamiętywane w historii.

Saldo, stan konta i operacje gotowkowe (2)
    W tej części można zrobic podgląd stanu finansów firmy i wartości zapasów zgromadzonych w magazynie. Można też
    wpłacić środki własne na konto, bądź też je wypłacić. W przypadku wypłaty w kwocie przewyższającej stan konta,
    program zglośi błąd. Akcje wykonane w tej części są zapamiętywane w historii.

Stan magazynu (dane calosciowe, wprowadzanie i wykreslanie towarow) (3)
    W tej części można prześledzić całą listę stanu magazynu. Można dodawać nowe produktu do magazynu (inne niż
    zakupione), bądź też tworzyć nowe kategorie produktów, dodając towary i wpisując ilość "zero".
    Akcje wykonane w tej części są zapamiętywane w historii.

Znajdz produkt w magazynie (4)
    Wyszukiwarka produktów. Tutaj można sprawdzić, czy jakiś produkt jest w magazynie.

Sprzedaz (5)
    Tutaj można sprzedawać produkty znajdujące się w magazynie. Jeśli wpiszę produkt nie istniejący w magazynie, program
    zgłosi błąd. Jeśli wpiszę ilość sprzedawanego towaru większą niż zapasy w magazynie, program zgłosi błąd.
    Jeśli wpiszę sprzedaż po cenie zakupu, program wykreśli odpowiednią ilość produktu z magazynu, zmieni
    jego wartość w magazynie i uzyskane ze sprzedaży pieniądze doda na konto.
    Jeśli wpiszę cenę sprzedaży po cenie innej niż cena zakupu, program wykona wcześniej wymienione akcje, a także
    czy jaki zysk (bądź stratę) uzyskałem ze sprzedaży tej partii towaru.
    Akcje wykonane w tej części są zapamiętywane w historii.

Zakup (6)
    Są dwie opcje zakupu - towarów, które są w magazynie i towarów, których dotąd w magaynie nie było. Jeśli wpiszę towar
    który w magayzynie już był, ale w innej cenie niż kupowana, program zgłosi błąd i wskaże, że ten towar
    powininnem wpisać jako nowy.
    Jeśli będę chciał kupić towary o wartości przekraczającej stan konta, program zgłosi błąd.
    Akcje wykonane w tej części są zapamiętywane w historii.

Historia zdarzen - wpisz: 7
    Na liście gromadzone są dane o czynnościach przeprowadzonych w poprzednich częściach. Listę można wyświetlać w
    całości, bądź w odpowiednim, wskazanym zakresie.

Wyjscie z programu - wpisanie słowa 'koniec', kończy program.

Program uwzględnia ewentualne błędy użytkownika, w tym wpisywanie towarów wielkimi bądź małymi literami, dodawanie
    spacji, wpisywanie słów zamiast wartości przy cenach i ilości.
"""

"""zmienne do czesci 1 i 2 (Obsluga kredytow i saldo, stan konta, operacje gotowkowe)"""
import os
class Manager:
    def __init__ (self):
        self.funkcje = {}

    def przypisz_funkcje (self, nazwa):
        def dekorator(funkcja):
            self.funkcje[nazwa] = funkcja
        return dekorator

    def wykonaj (self, nazwa, *args, **kwargs):
        if nazwa not in self.funkcje:
            print("Action not defined")
        else:
            self.funkcje[nazwa](self, *args, **kwargs)

class Hurtownia(Manager):

    pliki_w_folderze = os.listdir()
    def __init__ (self):
        self.saldo = 0
        self.historia = list()
        self.konto = float(0)
        self.zadluzenie = float(0)
        self.stan_magazynu = {}
        self.wartosc_zapasow = float(0)
        super().__init__()

fm = Hurtownia()

@fm.przypisz_funkcje("kredyty")
def kredyty (fm, zadluzenie):
    while True:
        print("Obsluga kredytow - Aktualny stan zadluzenia wynosi {} zl\n".format(zadluzenie))
        print("""Wprowadzenie wartosci uruchomionego kredytu - wpisz: 1
Splata kredytu - wpisz: 2
Powrot do glownego menu  - wpisz: 3""")
        odp1 = input()
        if odp1 != "1" and odp1 != "2" and odp1 != "3":
            print("Wybrales zla opcje!\n")
            fm.wykonaj("kredyty", zadluzenie=fm.zadluzenie)
        if odp1 == "1":
            kredyt = input("Wpisz wartosc udzielonego Ci kredytu:  \n")
            if not kredyt.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            kredyt = float(kredyt)
            fm.zadluzenie += kredyt
            print("Stan zadluzenia po zmianie wynosi {} zl\n\n".format(fm.zadluzenie))
            wpis_1_1 = ("Zaciagniety kredyt w wysokosci: {} zl".format(kredyt))
            fm.historia.append(wpis_1_1),
            fm.konto = fm.konto + kredyt
            fm.wykonaj("kredyty", zadluzenie=fm.zadluzenie)
        if odp1 == "2":
            splata = input("Wpisz kwote splaconego kredytu:")
            if not splata.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            splata = float(splata)
            if splata > fm.konto:
                print("Nie masz wystarczajacych srodkow na koncie\n\n")
                continue
                wybor == "1"
            if splata <= fm.konto:
                fm.zadluzenie -= splata
                fm.konto -= splata
                print("Stan zadluzenia po zmianie wynosi {} zl\n".format(fm.zadluzenie))
                wpis_1_2 = ("Splata kredytu w wysokosci: {} zl".format(splata))
                fm.historia.append(wpis_1_2)
                fm.wykonaj("kredyty", zadluzenie=fm.zadluzenie)
        if odp1 == "3":
            break

@fm.przypisz_funkcje("finanse")
def finanse (fm, konto, zadluzenie, wartosc_zapasow):
    while True:

        print("Saldo magazynu, stan konta i operacje gotowkowe\n")
        print("Wartosc towarow w magazynie wynosi: {} zl".format(fm.wartosc_zapasow))
        print("Stan konta: {} zl".format(fm.konto))
        print("Wysokosc zadluzenia wynosi: {} zl".format(fm.zadluzenie))
        print("Saldo firmy (aktywa - pasywa) wynosi: {} zl\n".format(fm.wartosc_zapasow+fm.konto-fm.zadluzenie))
        print(" --------- Wybierz opcję:\n")
        print("""Jesli chcesz wplacic srodki na konto - wpisz: 1
Jesli chcesz wyplacic srodki z konta - wpisz: 2
Powrot do menu glownego - wpisz: 3\n""")
        wybor2=input()
        if wybor2=="1":
            wplata=input("Podaj kwote wplaty na konto w PLN:   ")
            if not wplata.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            wplata=float(wplata)
            fm.konto = fm.konto+wplata
            print("\nStan konta wynosi: {}".format(fm.konto))
            wpis_2=("Wplata wlasna na konto: {} zl".format(wplata))
            fm.historia.append(wpis_2)
            fm.wykonaj("finanse", konto = fm.konto, zadluzenie = fm.zadluzenie, wartosc_zapasow=self.wartosc_zapasow)
        if wybor2=="2":
            wyplata = input("Podaj kwote do wyplacenia z konta w PLN:   ")
            if not wyplata.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            wyplata = float(wyplata)
            if wyplata > fm.konto:
                print("Nie masz wystarczajaco srodkow na koncie!\n")
                continue
            if wyplata < fm.konto:
                fm.konto = fm.konto - wyplata
                print("\nStan konta wynosi: {}".format(fm.konto))
                wpis_2 = ("Wyplata z konta: {} zl".format(wyplata))
                fm.historia.append(wpis_2)
                fm.wykonaj("finanse", konto = fm.konto, zadluzenie = fm.zadluzenie, wartosc_zapasow=fm.wartosc_zapasow)
        if wybor2 == "3":
            break
        else:
            print("Wybrales zla opcje\n")
            continue

@fm.przypisz_funkcje("obsluga_magazynu")
def obsluga_magazynu (fm, stan_magazynu):
    while True:
        print("----- Stan magazynu - wybierz opcje ------")
        print("""\nWyswietl stan magazynu - wpisz: 1
Dodaj nowy produkt - wpisz: 2
Wykresl produkt z magazynu - wpisz: 3
Wroc do menu glownego - wpisz: 4\n""")
        wybor3=input()
        wybor3 = wybor3.lower()
        if wybor3 != "1" and wybor3 != "2" and wybor3 != "3" and wybor3 != "4":
            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
            continue
        if wybor3=="1":
            number = 0
            for row in fm.stan_magazynu.items():
                number += 1
                print(number, row)
            powrot=input('Powrot do menu "Stan magazynu" - wybierz "Q":   ')
            powrot = powrot.lower()
            if powrot == "q":
                fm.wykonaj("obsluga_magazynu", fm.stan_magazynu)
        if wybor3 == "2":
            while True:
                produkt = input("\nWpisz nazwe nowego produktu:  ").strip()
                produkt = produkt.lower()
                ilosc = input("Wpisz ilosc produktu:   ")
                if not ilosc.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                ilosc = float(ilosc)
                cena = input("Wpisz cene produktu:  ")
                if not cena.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                cena = float(cena)
                wartosc = ilosc * cena
                wartosc = float(wartosc)
                fm.stan_magazynu[produkt] = {"ilosc": ilosc, "cena": cena, "wartosc": wartosc}
                print("Wprowadzono towar: {}, w ilosci: {}, w cenie: {}, laczna wartosc: {}".format(produkt, ilosc,
                                                                                                        cena, wartosc))
                wpis_3_1 = ("Wprowadzono do magazynu {}, w ilosci {}, po cenie {} zl".format(produkt, ilosc, cena))
                fm.historia.append(wpis_3_1)
                print("\nCzy chcesz wprowadzic kolejny produkt? t/n")
                odp2 = input()
                odp2 = odp2.lower()
                if odp2 == "t":
                    continue
                elif odp2 == "n":
                    break
                    wybor3 = input()
                else:
                    print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                    continue
        if wybor3 == "3":
            while True:
                produkt = input("\nWpisz nazwe produktu do wykreslenia:  ").strip()
                produkt = produkt.lower()
                if produkt not in fm.stan_magazynu:
                    print("Nie ma takiego produktu w magazynie")
                    print("\nCzy chcesz wykreslic inny produkt? t/n")
                    odp3_1 = input()
                    odp3_1 = odp3_1.lower()
                    if odp3_1 == "t":
                        continue
                    if odp3_1 == "n":
                        break
                        wybor == 3
                if produkt in fm.stan_magazynu:
                    print(fm.stan_magazynu[produkt])
                    potwierdzenie=input("\nCzy na pewno chcesz wykrelic ten produkt? t/n   ")
                    potwierdzenie=potwierdzenie.lower()
                    if potwierdzenie == "t":
                        wpis_3_2 = ("Ze stanu magazynu magazynu zdjeto {} - {}".format(produkt, stan_magazynu[produkt]))
                        fm.historia.append(wpis_3_2)
                        del fm.stan_magazynu[produkt]
                        print("\nCzy chcesz wykreslic kolejny produkt? t/n")
                        odp3_2 = input()
                        odp3_2 = odp3_2.lower()
                        if odp3_2 == "t":
                            continue
                        if odp3_2 == "n":
                            break
                            wybor3 = input()
                    if potwierdzenie == "n":
                        break
                        wybor3 = input()
                    else:
                        print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                        continue

        if wybor3 == "4":
            break
        else:
            print("Wybrales zla opcje\n")
            continue
@fm.przypisz_funkcje("szukanie_towarow")
def szukanie_towarow (fm):
    while True:
        szukana = input("Wpisz szukany towar:  ").strip()
        szukana = szukana.lower()
        if szukana in fm.stan_magazynu:
            print(szukana, fm.stan_magazynu[szukana])
            powrot4 = input("Czy chcesz szukac innego towaru? t/n:    ")
            powrot4 = powrot4.lower()
            if powrot4 == "t":
                continue
            elif powrot4 == "n":
                break
                wybor = input()
            else:
                print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                continue
        if szukana not in fm.stan_magazynu:
            odp4 = input("""W magazynie nie odnaleziono takiego towaru!
    Czy chcesz szukac innego towaru? t/n:    """)
            odp4 = odp4.lower()
            if odp4 == "t":
                continue
            elif odp4 == "n":
                break
                wybor = input()
            else:
                print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                continue

@fm.przypisz_funkcje("sprzedawanie_towarow")
def sprzedawanie_towarow (fm):
    while True:
        print("""Sprzedaz - wpisz: 1
    Wroc do menu glownego - wpisz: 2""")
        odp_5 = input()
        if odp_5 == "1":
            przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ").strip()
            przedmiot_sprzadazy = przedmiot_sprzadazy.lower()
            if przedmiot_sprzadazy not in fm.stan_magazynu:
                print("Takiego towaru nie ma magazynie. Powrot do menu\n")
                continue
                przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ")
            if przedmiot_sprzadazy in fm.stan_magazynu:
                print("Aktualny stan w magazynie:\n")
                print(przedmiot_sprzadazy, fm.stan_magazynu[przedmiot_sprzadazy])
                ilosc_sprzedawana = input("Podaj ilosc sprzedawanego towaru:   ")
                if not ilosc_sprzedawana.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                ilosc_sprzedawana = float(ilosc_sprzedawana)
                cena_sprzedazy = input("Podaj cene sprzedazy:   ")
                if not cena_sprzedazy.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                cena_sprzedazy = float(cena_sprzedazy)
                wartosc_sprzedazy = ilosc_sprzedawana * cena_sprzedazy
                wartosc_sprzedazy = float(wartosc_sprzedazy)
                if ilosc_sprzedawana > fm.stan_magazynu[przedmiot_sprzadazy]["ilosc"]:
                    print("W magazynie nie masz takiej ilosci {}\n".format(przedmiot_sprzadazy))
                    continue
                    przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ")
                else:
                    if cena_sprzedazy == fm.stan_magazynu[przedmiot_sprzadazy]["cena"]:
                        fm.stan_magazynu[przedmiot_sprzadazy]["ilosc"] -= ilosc_sprzedawana
                        fm.stan_magazynu[przedmiot_sprzadazy]["wartosc"] -= wartosc_sprzedazy
                        print(przedmiot_sprzadazy, fm.stan_magazynu[przedmiot_sprzadazy])
                        wpis_5_1 = ("Sprzedano {}, w ilosci {}, po cenie {} zl"
                                    .format(przedmiot_sprzadazy, ilosc_sprzedawana, cena_sprzedazy))
                        fm.historia.append(wpis_5_1)
                        fm.konto = fm.konto + wartosc_sprzedazy
                        print("Sprzedales {} za laczno kwote {} zl".format(przedmiot_sprzadazy,
                                                                           wartosc_sprzedazy))
                        print("\nCzy chcesz sprzedac kolejny produkt? t/n")
                        odp5_1 = input()
                        odp5_1 = odp5_1.lower()
                        if odp5_1 == "t":
                            przedmiot_sprzadazy = input("Podaj nazwe towaru do sprzedazy:   ").strip()
                        elif odp5_1 == "n":
                            break
                            odp_5 = input()
                        else:
                            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                            continue
                    if cena_sprzedazy != fm.stan_magazynu[przedmiot_sprzadazy]["cena"]:
                        fm.stan_magazynu[przedmiot_sprzadazy]["ilosc"] -= ilosc_sprzedawana
                        stara_wartosc = ilosc_sprzedawana * fm.stan_magazynu[przedmiot_sprzadazy]["cena"]
                        fm.stan_magazynu[przedmiot_sprzadazy]["wartosc"] -= stara_wartosc
                        print("Aktualny stan w magazynie:", przedmiot_sprzadazy, fm.stan_magazynu[przedmiot_sprzadazy])
                        zysk = wartosc_sprzedazy - stara_wartosc
                        wpis_5_2 = ("Sprzedano {}, w ilosci {}, po cenie {} zl".format(przedmiot_sprzadazy,
                                                                                       ilosc_sprzedawana,
                                                                                       cena_sprzedazy))
                        fm.historia.append(wpis_5_2)
                        fm.konto = fm.konto + wartosc_sprzedazy
                        if zysk > 0:
                            print("Ze sprzedazy {} osignales zysk w wysokości {} zl.".format(przedmiot_sprzadazy, zysk))
                        if zysk < 0:
                            print("Sprzedaz {} zakonczyla sie strata w wysokości {} zl.".format(przedmiot_sprzadazy,
                                                                                                zysk))
                        print("\nCzy chcesz sprzedac kolejny produkt? t/n")
                        odp5_2 = input()
                        odp5_2 = odp5_2.lower()
                        if odp5_2 == "t":
                            continue
                        elif odp5_2 == "n":
                            break
                            odp_5 = input()
                        else:
                            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                            continue
        if odp_5 == "2":
            break
            wybor = input()
        else:
            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
            continue

@fm.przypisz_funkcje("kupowanie_towarow")
def kupowanie_towarow (fm, konto):
    while True:
        print("Zakup towarow. Aktualny stan konta wynosi {} zl\n".format(konto))
        print("""Zakup towaru wystepujacego juz w magazynie - wpisz: 1
    Zakup towaru nie wystepujacego dotad w magazynie - wpisz: 2
    Powrot do menu glownego - wpisz: 3""")
        opcja_zakupu = input()
        if opcja_zakupu == "1":
            zakup = input("\nWpisz nazwe towaru:  ").strip()
            zakup = zakup.lower()
            if zakup not in fm.stan_magazynu:
                print("Takiego towaru nie ma magazynie. Sproboj jeszcze raz lub sprawdz stan magazynu\n")
                continue
                opcja_zakupu = input()
            if zakup in fm.stan_magazynu:
                print("Aktualny stan w magazynie:\n")
                print(zakup, fm.stan_magazynu[zakup])
                ilosc_kupowana = input("Podaj ilosc kupowanego towaru:   ")
                if not ilosc_kupowana.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                ilosc_kupowana = float(ilosc_kupowana)
                cena_kupna = input("Podaj cene kupna:   ")
                if not cena_kupna.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                cena_kupna = float(cena_kupna)
                wartosc_zakupu = ilosc_kupowana * cena_kupna
                wartosc_zakupu = float(wartosc_zakupu)
                if wartosc_zakupu > fm.konto:
                    print("\nNie masz wystarczajcych srodkow na koncie! Sproboj jeszcze raz.\n")
                    continue
                    opcja_zakupu = input()
                else:
                    if cena_kupna != fm.stan_magazynu[zakup]["cena"]:
                        print("{} w magazynie ma inna cene. Wprowadz kupowany towar jako nowa pozycja w magazynie\n"
                              .format(zakup))
                        continue
                        opcja_zakupu = input()
                    elif cena_kupna == fm.stan_magazynu[zakup]["cena"]:
                        fm.stan_magazynu[zakup]["ilosc"] += ilosc_kupowana
                        fm.stan_magazynu[zakup]["wartosc"] += wartosc_zakupu
                        print(zakup, fm.stan_magazynu[zakup])
                        wpis_6_1 = ("Zakupiono {}, w ilosci {}, po cenie {} zl"
                                    .format(zakup, ilosc_kupowana, cena_kupna))
                        fm.historia.append(wpis_6_1)
                        fm.konto = fm.konto - wartosc_zakupu
                        print("\nCzy chcesz zakupic kolejny produkt? t/n")
                        odp6_1 = input()
                        odp6_1 = odp6_1.lower()
                        if odp6_1 == "t":
                            continue
                        elif odp6_1 == "n":
                            break
                            wybor6 = input()
                        else:
                            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                            continue

        if opcja_zakupu == "2":
            produkt = input("\nWpisz nazwe nowego produktu:  ").strip()
            produkt = produkt.lower()
            if produkt in fm.stan_magazynu:
                print("Taki towar znajduje sie juz w magazynie. Powrot do menu\n")
                continue
                opcja_zakupu = input()
            if produkt not in fm.stan_magazynu:
                ilosc = input("Wpisz ilosc produktu:   ")
                if not ilosc.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                ilosc = float(ilosc)
                cena = input("Wpisz cene produktu:  ")
                if not cena.isdigit():
                    print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                    continue
                cena = float(cena)
                wartosc = ilosc * cena
                wartosc = float(wartosc)
                if wartosc > fm.konto:
                    print("Nie masz wystarczajcych srodkow na koncie\n")
                    continue
                    opcja_zakupu = input()
                else:
                    fm.stan_magazynu[produkt] = {"ilosc": ilosc, "cena": cena, "wartosc": wartosc}
                    print("Zakupiono towar :{}, w ilosci: {}, w cenie: {}, laczna wartosc: {}".
                          format(produkt, ilosc, cena, wartosc))
                    wpis_6_2 = ("Zakupiono {}, w ilosci {}, po cenie {} zl".format(produkt, ilosc, cena))
                    fm.historia.append(wpis_6_2)
                    fm.konto = fm.konto - wartosc
                    print("\nCzy chcesz zakupic kolejny produkt? t/n")
                    odp6_2 = input()
                    odp6_2 = odp6_2.lower()
                    if odp6_2 == "t":
                        continue
                    elif odp6_2 == "n":
                        break
                        wybor6 = input()
                    else:
                        print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
                        continue

        if opcja_zakupu == "3":
            break
            wybor = input()

@fm.przypisz_funkcje("historia_sklepu")
def historia_sklepu (fm):
    while True:
        print("\n -------- Historia zdarzen --------\n")
        print("""Pelna historia zdarzen - wpisz: 1
    Wybor zakresu z histori zdarzen - wpisz: 2
    Powrot do glownego menu - wpisz: 3""")
        wybor7 = input()
        if wybor7 == "1":
            index = 0
            for cala_historia in fm.historia:
                index += 1
                print(index, cala_historia)
            powrot7 = input('Wpisz "Q" aby wrocic do menu "Historia zdarzen":   ')
            if powrot7 == "q":
                continue
                wybor7 = input()
            else:
                continue
                wybor7 = input()
        if wybor7 == "2":
            index = 0
            od = input("Wprowadz poczatkowy numer z listy:   ")
            if not od.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            od = int(od)
            od = od - 1
            do = input("Wprowadz koncowy numer z listy:    \n")
            if not do.isdigit():
                print("Wpisales inna wartosc niz liczba. Sproboj jeszcze raz\n\n")
                continue
            do = int(do)
            if od > len(fm.historia) or do > len(fm.historia):
                print("Wybrales liczby spoza zakresu listy. Sproboj jeszcze raz.\n\n")
                continue
            for zakres in range(od, do):
                index += 1
                print(index, fm.historia[zakres])
            powrot7 = input('Powrot do menu "Historia zdarzen" - wpisz: "q"\n\n')
            continue
        if wybor7 == "3":
            break
            wybor = input()
        else:
            print("Wybrales zla opcje! Sproboj jeszcze raz.\n")
            continue

@fm.przypisz_funkcje("zakonczenie")
def zakonczenie (fm, stan_magazynu, historia, konto, zadluzenie):
    with open("stan_magazynu.txt", "w") as plik:
        for k, v in fm.stan_magazynu.items():
            ilosc = fm.stan_magazynu[k]["ilosc"]
            cena = fm.stan_magazynu[k]["cena"]
            wartosc = fm.stan_magazynu[k]["wartosc"]
            v = ilosc, cena, wartosc
            k = k.replace(" ", "_")
            plik.write(f"{k} {ilosc} {cena} {wartosc}\n")
    with open("konto.txt", "w") as plik:
        plik.write(f"{fm.konto}")
    with open("zadluzenie.txt", "w") as plik:
        plik.write(f"{fm.zadluzenie}")
    with open("historia.txt", "w") as plik:
        for linia in fm.historia:
            plik.write(f"{linia}")
            plik.write(f"\n")





fm.wykonaj("glowny_panel", fm.konto)
pliki_w_folderze = os.listdir()

if "konto.txt" in pliki_w_folderze:
    with open("konto.txt", "r") as plik:
        for linia in plik:
            fm.konto = float(linia)
else:
    fm.konto = float(0)

if "zadluzenie.txt." in pliki_w_folderze:
    with open("zadluzenie.txt", "r") as plik:
        for linia in plik:
            fm.zadluzenie = float(linia)
else:
    fm.zadluzenie = float(0)

with open("stan_magazynu.txt", "r") as plik:
    for linia in plik:
        linia = linia.split()
        produkt, ilosc, cena, wartosc = linia
        produkt = str(produkt)
        produkt = produkt.replace("_", " ")
        fm.stan_magazynu[produkt] = {}
        ilosc = float(ilosc)
        cena = float(cena)
        wartosc = float(wartosc)
        fm.stan_magazynu[produkt] = {"ilosc": ilosc, "cena": cena, "wartosc": wartosc}

    def zapasy(stan_magazynu):
        suma = 0
        for v in fm.stan_magazynu.values():
            suma += v["wartosc"]
        return suma

    fm.wartosc_zapasow = zapasy(fm.stan_magazynu)

with open("historia.txt", "r") as plik:
    for linia in plik:
        linia = linia.strip('\n')
        fm.historia.append(linia)

while True:

    print(" ------------- Program księgowy -------------\n")
    print(f"\nAktualny stan konta wynosi:{fm.konto} zl.\n")
    print('''Wybierz opcje:
        Obsluga kredytow - wpisz: 1
        Saldo, stan konta i operacje gotowkowe - wpisz: 2
        Stan magazynu (dane calosciowe, wprowadzanie i wykreslanie towarow) - wpisz: 3
        Znajdz produkt w magazynie - wpisz: 4
        Sprzedaz - wpisz: 5
        Zakup - wpisz: 6
        Historia zdarzen - wpisz: 7
        Wyjscie z programu - wpisz: "koniec"\n''')

    wybor = input()

    if wybor == "1":
        fm.wykonaj("kredyty", zadluzenie=fm.zadluzenie)
    if wybor == "2":
        fm.wykonaj("finanse", konto=fm.konto, zadluzenie=fm.zadluzenie, wartosc_zapasow=fm.wartosc_zapasow)
    if wybor == "3":
        fm.wykonaj("obsluga_magazynu", fm.stan_magazynu)
    if wybor == "4":
        fm.wykonaj("szukanie_towarow")
    if wybor == "5":
        fm.wykonaj("sprzedawanie_towarow")
    if wybor == "6":
        fm.wykonaj("kupowanie_towarow", fm.konto)
    if wybor == "7":
        fm.wykonaj("historia_sklepu")
    if wybor == "koniec":
        fm.wykonaj("zakonczenie", stan_magazynu=fm.stan_magazynu, historia=fm.historia, konto=fm.konto, zadluzenie=fm.zadluzenie)
        break
