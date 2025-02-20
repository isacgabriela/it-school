#1) Avem 2 numere intregi. Sa se afiseze catul si restul impartirii numerelor.

# Citim cele doua numere intregi
a = int(input("Introduceți primul număr: "))
b = int(input("Introduceți al doilea număr: "))

# Calculăm câtul și restul împărțirii
catul = a // b
restul = a % b

# Afișăm rezultatele
print("Câtul împărțirii lui", a, "la", b, "este:", catul)
print("Restul împărțirii lui", a, "la", b, "este:", restul)

#2) Avem 2 numere intregi. Sa se afiseze rezultatele ridicarii la putere a celor doua numere.

# Citim cele doua numere intregi
a = int(input("Introduceți primul număr: "))
b = int(input("Introduceți al doilea număr: "))

# Calculăm rezultatele ridicării la putere
putere1 = a ** b
putere2 = b ** a

# Afișăm rezultatele
print(a, "ridicat la puterea", b, "este:", putere1)
print(b, "ridicat la puterea", a, "este:", putere2)

#3) Avem 2 numere intregi. Sa se afiseze daca cel de al doilea numar este divizibil cu primul.

# Citim cele doua numere intregi
a = int(input("Introduceți primul număr: "))
b = int(input("Introduceți al doilea număr: "))

# Verificăm dacă b este divizibil cu a
if b % a == 0:
    print(b, "este divizibil cu", a)
else:
    print(b, "nu este divizibil cu", a)

#4) Avem un numar aleatoriu. Sa se afiseze daca numarul este par sau impar.

# Citim numarul aleatoriu
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul este par sau impar
if numar % 2 == 0:
    print(numar, "este un număr par.")
else:
    print(numar, "este un număr impar.")

#5) Se citeste de la tastatura un numar. Sa se verifice daca numarul se afla in intervalul 100-150.

# Citim numarul de la tastatura
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul este în intervalul 100-150
if 100 <= numar <= 150:
    print(numar, "se află în intervalul 100-150.")
else:
    print(numar, "nu se află în intervalul 100-150.")

#6) Se citeste un numar de la tastatura. Sa se verifice daca numarul este mai mic decat 50 sau mai mare decat 100.

# Citim numarul de la tastatura
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul este mai mic decât 50 sau mai mare decât 100
if numar < 50 or numar > 100:
    print(numar, "este mai mic decât 50 sau mai mare decât 100.")
else:
    print(numar, "nu este mai mic decât 50 sau mai mare decât 100.")

#7) Se citesc doua numere de la tastatura. Sa se determine tipul celor doua numere int/float si sa se afiseze rezultatele verificarii.

# Citim cele doua numere
nr1 = input("introdu primul numar: ")
nr2 = input("introdu al doilea numar: ")

# Verificăm dacă primul numar este int/float
if "." in nr1:
    nr1 = float(nr1)
else:
    nr1 = int(nr1)
print(nr1)

# Verificăm dacă al doilea numar este int/float
if "." in nr2:
    nr2 = float(nr2)
else:
    nr2 = int(nr2)
print(nr2)

#8) Se citesc doua numere de la tastatura. Sa se determine care dintre cele doua este mai mare si sa se afiseze un mesaj corespunzator.

# Citim cele doua numere de la tastatura
numar1 = float(input("Introduceți primul număr: "))
numar2 = float(input("Introduceți al doilea număr: "))

# Determinăm care dintre cele două numere este mai mare
if numar1 > numar2:
    print(numar1, "este mai mare decât", numar2)
elif numar2 > numar1:
    print(numar2, "este mai mare decât", numar1)
else:
    print("Ambele numere sunt egale")

#9) Se citesc doua string-uri de la tastatura. Sa se determine daca primul string se regaseste in cel de al doilea string.

# Citim cele doua string-uri de la tastatura
string1 = input("Introduceți primul string: ")
string2 = input("Introduceți al doilea string: ")

# Verificăm dacă primul string se regăsește în cel de-al doilea string
if string1 in string2:
    print("Primul string se regăsește în cel de-al doilea string.")
else:
    print("Primul string nu se regăsește în cel de-al doilea string.")

#10) Se da urmatorul string: "Ana are 10 mere si 5 pere.". Sa se extraga cuvantul "pere" din propozitie si sa se afiseze.

# Definim string-ul dat
propozitie = "Ana are 10 mere si 5 pere."

# Căutăm cuvântul "pere" în propoziție
cuvant = "pere"
if cuvant in propozitie:
    print("Cuvântul extras este:", cuvant)
else:
    print("Cuvântul", cuvant, "nu se regăsește în propoziție.")

#11) Se citeste un sir de numere de la tastatura separate prin virgula. Se citeste un numar de la tastatura. Sa se verifice daca numarul face parte din lista.

# Citim sirul de numere separate prin virgula
sir_numere = input("Introduceți un șir de numere separate prin virgulă: ")

# Transformăm sirul de numere într-o listă de întregi
lista_numere = [int(numar) for numar in sir_numere.split(",")]

# Citim numarul de la tastatura
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul face parte din lista
if numar in lista_numere:
    print(numar, "face parte din lista de numere.")
else:
    print(numar, "nu face parte din lista de numere.")


#12) Se citesc doua numere de la tastatura. Sa se determine care dintre cele doua numere este mai mic si daca este un numar par sa se afiseze un mesaj corespunzator.

# Citim cele doua numere de la tastatura
numar1 = float(input("Introduceți primul număr: "))
numar2 = float(input("Introduceți al doilea număr: "))

# Determinăm care dintre cele două numere este mai mic
if numar1 < numar2:
    mai_mic = numar1
    print(numar1, "este mai mic decât", numar2)
else:
    mai_mic = numar2
    print(numar2, "este mai mic decât", numar1)

# Verificăm dacă numărul mai mic este par
if mai_mic % 2 == 0:
    print(mai_mic, "este un număr par.")
else:
    print(mai_mic, "nu este un număr par.")


#13) Se citeste un numar de la tastatura. Sa se afiseze un mesaj corespunzator in cazul in care numarul este divizibil cu 3 sau cu 5.

# Citim numarul de la tastatura
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul este divizibil cu 3 sau cu 5
if numar % 3 == 0 and numar % 5 == 0:
    print(numar, "este divizibil atât cu 3, cât și cu 5.")
elif numar % 3 == 0:
    print(numar, "este divizibil cu 3.")
elif numar % 5 == 0:
    print(numar, "este divizibil cu 5.")
else:
    print(numar, "nu este divizibil nici cu 3, nici cu 5.")


#14) Se citeste un numar de la tastatura. Sa se afiseze "fizz" daca numarul e divizibil cu 3, sa se afiseze "buzz" daca numarul este divizibil cu 5 si "fizzbuzz" daca numarul este divizibil si cu 3 si cu 5.

# Citim numarul de la tastatura
numar = int(input("Introduceți un număr: "))

# Verificăm dacă numărul este divizibil cu 3, 5 sau ambele
if numar % 3 == 0 and numar % 5 == 0:
    print("fizzbuzz")
elif numar % 3 == 0:
    print("fizz")
elif numar % 5 == 0:
    print("buzz")
else:
    print(numar)

#15) Se da urmatorul string: "Nume: Daniel, Prenume: Neamtiu". Sa se extraga numele si prenumele din acest string si sa se afiseze de la tastatura.

# Definim string-ul dat
string = "Nume: Daniel, Prenume: Neamtiu"



#16) Se da urmatorul string: "mere, pere, mere, mere, pere, struguri". Sa se afiseze de cate ori apare cuvantul "pere" in string.

# Definim string-ul dat
string = "mere, pere, mere, mere, pere, struguri"

# Numărăm de câte ori apare cuvântul "pere" în string
numar_pere = string.count("pere")

# Afișăm rezultatul
print("Cuvântul 'pere' apare de", numar_pere, "ori în string.")


#17) Se da urmatorul string: "Ana are 10 mingi de fotbal intergalactic". Sa se stearga cuvantul intergalactic din string si sa se afiseze rezultatul.

# Definim string-ul dat
string = "Ana are 10 mingi de fotbal intergalactic"

# Eliminăm cuvântul "intergalactic" din string
string_modificat = string.replace("intergalactic", "").strip()

# Afișăm rezultatul
print("String-ul modificat este:", string_modificat)

#18) Sa citeste de la tastatura o parola. Sa se verifice daca parola introdusa are cel putin 10 caractere si nu contine spatiu. Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita sau mesajul "OK" in cazul in care parola respecta regulile.

# Citim parola de la tastatura
parola = input("Introduceți parola: ")

# Verificăm lungimea parolei și prezența spațiilor
if len(parola) < 10:
    print("Parola trebuie să aibă cel puțin 10 caractere.")
elif " " in parola:
    print("Parola nu trebuie să conțină spații.")
else:
    print("OK")
