#21) Sa se numere de cate ori apare o litera intr-un cuvant. (folositi for si while)
cuvant = 'python'

for litera in cuvant:
    if litera in numar_litere:
        numar_litere +=1
print (numar_litere)

#22) Sa se afiseze toate numerele pare pana la 100.

for numar in range(2, 101, 2):
    print(numar)

numar = 2
while numar <= 100:
    print(numar)
    numar += 2

#23) Sa se afiseze toate numerele impare pana la 50.

for numar in range(1, 51, 2):
    print(numar)

numar = 1
while numar < 50:
    print(numar)
    numar += 2

#24) Sa se afiseze toate puterile lui 2 mai mici decat 150.

putere = 1
for x in range(150):
    if putere >= 150:
        break
    print(putere)
    putere *= 2

putere = 1
while putere < 150:
    print(putere)
    putere *= 2

#25) Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.

for x in range(1, 10):
    putere = 3 ** x
    if putere >= 200 and putere <= 300:
        print(putere)

putere = 1
while putere < 200:
    putere *= 3
while putere <= 300:
    print(putere)
    putere *= 3

#26) Se citeste un numar de la tastatura. Sa se calculeze suma numerelor de la 1 pana la numarul citit.
#(folositi for si while)

numar = int(input("Introduceți un număr: "))
suma = 0
for x in range(1, numar + 1):
    suma += x
print(f"Suma numerelor de la 1 până la {numar} este: {suma}")
      
numar = int(input("Introduceți un număr: "))
suma = 0
x = 1
while x <= numar:
    suma += x
    x += 1
print(f"Suma numerelor de la 1 până la {numar} este: {suma}")

#27) Se citeste un numar de la tastatura. Sa se calculeze produsul numerelor de la 1 pana la numarul citit.
#(folositi for si while)

numar = int(input("Introduceți un număr: "))
produs = 1
for x in range(1, numar + 1):
    produs *= x
print(f"Produsul numerelor de la 1 până la {numar} este: {produs}")

numar = int(input("Introduceți un număr: "))
produs = 1
x = 1
while x <= numar:
    produs *= x
    x += 1
print(f"Produsul numerelor de la 1 până la {numar} este: {produs}")

#28) Se citeste un numar n de la tastatura. Sa se scrie un program care face o numaratoare inversa de la numarul 
#respectiv pana la 0.
#29) Se citeste un numar de la tastatura. Sa se afiseze toti divizorii acestuia.
#30) Se citeste un numar intreg de la tastatura. Sa se afiseze pe rand fiecare cifra a acestuia folosind un while.
#31) Sa se scrie un program care genereaza un numar aleator intre 1 si 100 
#(folositi modulul random cum am utilizat in sesiunile precedente). 
#Utilizatorul trebuie sa ghiceasca numarul generat introducand variante de la tastatura. 
#Programul trebuie sa ofere indicii utilizatorului daca nu ghiceste numarul 
#(Exemplu: numarul degenerat e 29. Daca noi introducem valoarea 7, trebuie sa ne spuna ca e gresit 
 #si ca trebuie sa alegem un numar mai mare. Daca introducem valoarea 55, atunci trebuie sa ne spuna ca 
 #numarul generat este mai mic decat valoarea introdusa de noi)

