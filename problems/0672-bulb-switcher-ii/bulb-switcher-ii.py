# Matematycznie krótko
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        if presses == 0:
            return 1                      # nic nie naciskamy: jeden układ
        if presses == 1:
            return [2, 3, 4][n - 1]       # jeden przycisk: 4 układy (dla n=1 i n=2 część się zlewa)
        if presses == 2:
            return [2, 4, 7][n - 1]       # dwa przyciski: 7 układów, bo nie da się samego przycisku 4
        return [2, 4, 8][n - 1]           # 3 i więcej: wszystkie 8 układów



# Fakty, na których opiera się rozwiązanie
# Liczy się tylko parzystość naciśnięć każdego przycisku. Dwa naciśnięcia tego samego przycisku się znoszą, a kolejność nie ma znaczenia. Dla każdego przycisku jest więc tylko wybór "naciśnięty parzyście (0) albo nieparzyście (1) razy".
# Przycisk 1 jest zbędny jako osobna operacja. Przełączenie wszystkich żarówek to to samo, co przełączenie parzystych i nieparzystych razem (każda żarówka jest jednym z tych dwóch rodzajów). Zostają trzy niezależne przełączniki (II, III, IV), czyli co najwyżej 2³ = 8 różnych wyglądów pokoju.
# Wystarczą pierwsze 3 żarówki. Przełączenia II, III i IV wpływają na żarówki 1, 2, 3 jako trzy różne wzorce (żarówka 2 reaguje tylko na II, żarówka 3 tylko na III, żarówka 1 na III i IV), więc ich stan jednoznacznie wyznacza wybór przełączników, a każda dalsza żarówka jest funkcją tych trzech. Dlatego przyjmujemy n = min(n, 3).
# Które układy przycisków są dozwolone przy presses naciśnięciach: wybierasz zestaw przycisków naciśniętych nieparzyście razy. Jeśli ma w elementów, to musi zachodzić w ≤ presses i presses − w parzyste (resztę naciśnięć marnujesz w znoszących się parach).




# Matematycznie dłużej opisane
# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#         # Tylko pierwsze 3 żarówki mają znaczenie (reszta jest od nich zależna).
#         liczba_zarowek = min(n, 3)

#         # Co robi każdy przycisk z żarówkami 1, 2, 3 (1 = przełącza, 0 = nie rusza).
#         przyciski = [
#             [1, 1, 1],   # przycisk 1: wszystkie
#             [0, 1, 0],   # przycisk 2: parzyste (wśród 1..3 tylko żarówka 2)
#             [1, 0, 1],   # przycisk 3: nieparzyste (żarówki 1 i 3)
#             [1, 0, 0],   # przycisk 4: 1, 4, 7, ... (wśród 1..3 tylko żarówka 1)
#         ]

#         mozliwe_wygladu = set()   # wszystkie różne układy żarówek, które da się uzyskać

#         # Każdy przycisk jest naciśnięty parzyście (0) albo nieparzyście (1) razy: 2^4 = 16 możliwości.
#         for p1 in (0, 1):
#             for p2 in (0, 1):
#                 for p3 in (0, 1):
#                     for p4 in (0, 1):
#                         wybrane = [p1, p2, p3, p4]
#                         ile_przyciskow = sum(wybrane)   # ile różnych przycisków naciskamy nieparzyście razy

#                         # Zmieścimy się w liczbie naciśnięć, a resztę zmarnujemy parami.
#                         if ile_przyciskow <= presses and (presses - ile_przyciskow) % 2 == 0:
#                             wyglad = []
#                             for zarowka in range(liczba_zarowek):
#                                 # Ile razy ta żarówka zostanie przełączona przez wybrane przyciski?
#                                 przelaczenia = 0
#                                 for nr_przycisku in range(4):
#                                     przelaczenia += wybrane[nr_przycisku] * przyciski[nr_przycisku][zarowka]
#                                 # Parzysta liczba przełączeń: bez zmiany (0). Nieparzysta: zmiana (1).
#                                 wyglad.append(przelaczenia % 2)
#                             mozliwe_wygladu.add(tuple(wyglad))

#         # Zbiór nie trzyma duplikatów, więc jego rozmiar to liczba różnych układów.
#         return len(mozliwe_wygladu)





# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#         # Żarówka nr i i żarówka nr i+6 zachowują się tak samo (zależy to tylko od parzystości
#         # i od reszty z dzielenia przez 3), więc wystarczy symulować co najwyżej 6 żarówek.
#         liczba_zarowek = min(n, 6)

#         # Każdy przycisk to lista jedynek i zer: pozycja 0 to żarówka nr 1, pozycja 1 to żarówka nr 2...
#         # 1 oznacza "ten przycisk przełącza tę żarówkę", 0 oznacza "nie rusza jej".
#         przycisk_1 = []   # wszystkie żarówki
#         przycisk_2 = []   # żarówki parzyste (2, 4, 6, ...)
#         przycisk_3 = []   # żarówki nieparzyste (1, 3, 5, ...)
#         przycisk_4 = []   # żarówki 1, 4, 7, 10, ... (reszta 1 z dzielenia przez 3)
#         for numer in range(1, liczba_zarowek + 1):
#             przycisk_1.append(1)
#             przycisk_2.append(1 if numer % 2 == 0 else 0)
#             przycisk_3.append(1 if numer % 2 == 1 else 0)
#             przycisk_4.append(1 if numer % 3 == 1 else 0)
#         przyciski = [przycisk_1, przycisk_2, przycisk_3, przycisk_4]

#         # Naciśnięcie przycisku: dla każdej żarówki, którą przycisk rusza, zamień 1 na 0 (albo 0 na 1).
#         def nacisnij(stan, przycisk):
#             nowy_stan = []
#             for i in range(liczba_zarowek):
#                 if przycisk[i] == 1:
#                     nowy_stan.append(1 - stan[i])   # przełącz: 1 -> 0, 0 -> 1
#                 else:
#                     nowy_stan.append(stan[i])       # bez zmian
#             return tuple(nowy_stan)                 # krotka, bo tylko takie można wkładać do zbioru

#         # Na początku wszystkie żarówki są włączone.
#         stan_poczatkowy = tuple([1] * liczba_zarowek)

#         # Zbiór wszystkich układów żarówek, które można mieć po tylu naciśnięciach, ile już zrobiliśmy.
#         mozliwe_stany = {stan_poczatkowy}

#         # Każde powtórzenie pętli to jedno naciśnięcie dla WSZYSTKICH możliwych układów naraz.
#         for _ in range(presses):
#             nowe_stany = set()
#             for stan in mozliwe_stany:
#                 for przycisk in przyciski:
#                     nowe_stany.add(nacisnij(stan, przycisk))
#             mozliwe_stany = nowe_stany   # stare układy odrzucamy: musimy zrobić DOKŁADNIE presses naciśnięć

#         # Zbiór nie trzyma duplikatów, więc jego rozmiar to liczba różnych układów.
#         return len(mozliwe_stany)