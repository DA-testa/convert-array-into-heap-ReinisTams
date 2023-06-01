# python3

def build_heap(data):
    #Saraksts, kur glabāt apmaiņas operācijas
    swaps = []  
    #Iegūst datu saraksta elementu skaitu
    n = len(data)  
    for i in range(n // 2 - 1, -1, -1):  #Ciklē no pēdējā vecākā mezgla līdz pirmajam (no augšas uz leju)
        sift_down(data, i, n, swaps)  # Izsauc funkciju sift_down, lai saglabātu koku

    return swaps

def sift_down(data, i, n, swaps):
    #Pieņem, ka pašreizējais mezgls ir vismazākais
    index = i  
    #Aprēķina kreisā bērna mezgla indeksu
    left = 2 * i + 1  
    #Aprēķina labā bērna mezgla indeksu
    right = 2 * i + 2  

    # Salīdzina kreiso bērnu ar pašreizējo vismazāko mezglu
    if left < n and data[left] < data[index]:
        index = left

    # Salīdzina labo bērnu ar pašreizējo vismazāko mezglu
    if right < n and data[right] < data[index]:
        index = right

    # Ja pašreizējais mezgls nav vismazākais, to nomaina ar vismazāko bērnu
    if i != index:
        data[i], data[index] = data[index], data[i]  # Nomaina mezglus vietām
        swaps.append((i, index))  # Reģistrē apmaiņas operāciju
        sift_down(data, index, n, swaps)  # Rekursīvi turpina apstrādāt apmainīto mezglu


def main():
    choice = input("Ievadiet 'I', lai ievadītu datus interaktīvi, vai 'F', lai ievadītu datus no faila: ")
    if choice == "I":  #ievade
        n = int(input("Ievadiet elementu skaitu: "))  #Ievada elementu skaitu
        data = list(map(int, input("Ievadiet elementus, atdalot tos ar atstarpēm: ").split()))  #Ievada elementus
        assert len(data) == n  #Pārbauda ka elementu skaits atbilst norādītajam
    elif choice == "F":  #Faila ievade
        file_path = input("Ievadiet faila ceļu: ")  #Ievada faila ceļu
        
        with open(file_path, 'r') as file:  #Atver failu
            n = int(file.readline())  #Nolasa elementu skaitu no pirmās rindas
            data = list(map(int, file.readline().split()))  #Nolasa elementus no otrās rindas
            assert len(data) == n  #Pārliecinās, ka elementu skaits atbilst norādītajam
    else:
        print("Nederīga ievade. Lūdzu, ievadiet 'I' vai 'F'.")
        return

    swaps = build_heap(data)  #Veido three un iegūst apmaiņas operācijas
    assert len(swaps) <= 4 * n  #Pārliecinās ka apmaiņas operāciju skaits ir pareizā ierobežojumā
    print("Apmaiņas operāciju skaits:", len(swaps))  #Izdrukā veiktās apmaiņas operācijas skaitu
    for i, j in swaps:
        
        print(i, j)  #Izdrukā apmainīto elementu indeksus


if __name__ == "__main__":
    main()
== "__main__":
    main()

