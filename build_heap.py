# python3

def build_heap(a):
    swaps = []  
    #Izveido sarakstu, kur glabājas apmaiņu operācijas
    
    n = len(a)  
    #Iegūst masīva garumu

    for i in range(1, n):
        #Veic "sift-up" operāciju, apmainot mezglu ar tā parent
        
        while i > 0 and a[(i - 1) // 2] > a[i]:  #Pārbauda, vai vecāks ir lielāks par pašreizējo mezglu
            a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]  #Apmaina mezglu ar vecāku
            swaps.append(((i - 1) // 2, i))  #Pievieno apmaiņas operāciju sarakstam
            i = (i - 1) // 2  #Atjauno indeksu nākamajai iterācijai

    #Atgriež apmaiņu operāciju sarakstu       
    return swaps  
   
#Izlasīt ievadi
n = int(input())  #Elementu skaits
a = list(map(int, input().split()))  #Masīva elementi

#Veidot koku un iegūt apmaiņu operācijas
swaps = build_heap(a)

#Izvadīt apmaiņu operāciju skaitu
print(len(swaps))

#Izvadīt apmaiņu operācijas
for swap in swaps:
    print(swap[0], swap[1])
