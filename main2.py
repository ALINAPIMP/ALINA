
#
# vartotojas = {
#     'vardas': 'Jonas',
#     'Amzius': 35,
#     'miestas': "Vilnius"
# }
# vartotojas['specialybe'] = "Vadovas"

# for  key in vartotojas:
#     print(key)

# for value in vartotojas.values():
#     print(value)

# for key, value in vartotojas.items():
#     print(key, value)


#1.Duotas žodynas {"vanduo": 1, "ugnis": 2, "žemė": 3, "oras": 4}.
#Parašykite kodą, kuris nuskaito vartotojo įvestą raktą ir atspausdina atitinkamą reikšmę.

# zodynas = {
#     "vanduo": 1,
#     "ugnis": 2,
#     "žemė": 3,
#     "oras": 4
# }
# ivestis = input("iveskite elementa(vanduo, ugnis, zeme, oras):")
# if ivestis in zodynas:
#     print(f' elemento {ivestis} reiksme yra: {zodynas[ivestis]}')
# else:
#     print(f'elementas {ivestis} zodyne nerastas')


#Turite žodyną, kuriame saugomi žmonių vardai ir jų amžiai.
# Parašykite programą, kuri leidžia vartotojui įvesti vardą ir naują amžių,
# o tuomet atnaujina šios asmenybės amžių žodyne.

# zodynas = {
#     'Jonas': 30, 'Algis':50, 'Ona': 20
# }
# Vardas = input('iveskite asmens varda:')
# naujas_amzius = int(input(f'iveskite {Vardas} nauja amziu:'))
# if Vardas in zodynas:
#     zodynas[Vardas] = naujas_amzius
#     print(f' atnaujintas {Vardas} amzius: {zodynas[Vardas]}')
# else:
#     print(f'asmuo vardu [vardas] zodyne nerastas')
# print('atnaujintas zodynas:', zodynas)


# def funkcijos_pavadinimas(argumentas1, argumentas2):
#         result = argumentas1 + argumentas2
#
#         return result
#
# manoFunkcija = funkcijos_pavadinimas(5, 15)
# print(manoFunkcija)


# def pasisveikinimas(vardas):
#     return "Sveiki" + vardas
#
# sveikintis = pasisveikinimas()
# print(sveikintis)

# def pilnas_vardas(vardas, pavarde):
#     return vardas + " " + pavarde
#
# fullName = pilnas_vardas(vardas="Antanas", pavarde="Antanavicius")
# print(fullName)

# def apversti_teksta(tekstas):
#     return tekstas[::-1]
#
# print(apversti_teksta("Mama noriu namo"))

# def skaiciu_vidurkis(skaiciai):
#     return sum(skaiciai)/len(skaiciai)
# print(skaiciu_vidurkis([15, 3, 35]))


# def maksimali_reiksme(skaiciai):
#     return max(skaiciai)
# print(maksimali_reiksme([5,6,15]))


# def sujungti_zodzius(zodziai, skyriklis):
#     return skyriklis.join(zodziai)
# print(sujungti_zodzius(['Labas', 'rytas'], ' '))

#atspausdinti daugybos lentele

# def daugybos_lentele(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(f'{i} x {j} = {i*j}')
#         print('-' * 10)
# daugybos_lentele(5)

#virtualus parduotuves asistentas

# 1. pasveikinti() - pasveikina vartotoją ir praneša apie parduotuvės paslaugas.
# 2. pasirinkti_preke() - leidžia vartotojui  pasirinkti prekę ir jos kiekį.
# 3. apibendrinti_pirkinius() - apibendrina vartotojo pirkinius ir pateikia galutinę kainą.
# 4. pagrindine_programa() - valdo pagrindinę programos logiką, naudodama kitas funkcijas.

# def pasisveikinti():
#     print('Sveiki atvyke i virtualia parduotuve')
#     print('Cia galite pasirinkti norimas prekes ir ju kainas\n')
# def pasirinkti_preke():
#     preke = input('Iveskite prekes pavadinima:')
#     kiekis = int(input(f'Kiek norite {preke}? Iveskite skaiciu:'))
#     return preke, kiekis
# def apibendrinti_pirkinius(pirkiniu_sarasas):
#     bendra_kaina = sum(kaina for _,kaina in pirkiniu_sarasas)
#     print('\nJusu pirkiniu sarasas:')
#     for preke,kaina in pirkiniu_sarasas:
#         print(f'{preke} - {kaina} €')
#     print(f'Bendra kaina: {bendra_kaina} €')
# def pagrindine_programa():
#     pasisveikinti()
#     pirkiniu_sarasas = []
#     while True:
#         preke,kiekis=pasirinkti_preke()
#         kaina=kiekis*5
#         pirkiniu_sarasas.append((preke,kaina))
#         testi=input('Ar norite testi pirkiniu pridejima?(taip/ne):')
#         if testi.lower()!='taip':
#             break
#     apibendrinti_pirkinius(pirkiniu_sarasas)
# pagrindine_programa()

# 1. pasveikinti() - pasveikina vartotoją ir informuoja apie bibliotekos sistemą.
# 2. prideti_knyga() - leidžia vartotojui pridėti naują knygą į kolekciją.
# 3. rodyti_knygas() - rodo visas kolekcijoje esančias knygas.
# 4. ieskoti_knygos() - ieško knygos pagal pavadinimą.
# 5 pagrindine_programa() - valdo pagrindinę programos logiką, naudodama kitas funkcijas.

# def pasisveikinti():
#     print('Sveiki atvyke i biblioteka')
#     print('Cia galite tvarkyti savo knygu kolekcija')
#
# def prideti_knyga(biblioteka):
#     pavadinimas = input('Iveskite knygos pavadinima:')
#     autorius = input('Iveskite autoriaus varda:')
#     biblioteka.append((pavadinimas, autorius))
#     print(f'knyga "{pavadinimas}" prideta')
#
# def rodyti_knyga(biblioteka):
#     if biblioteka:
#         print('Bibliotekos knygos:')
#         for nr,(pavadinimas, autorius) in enumerate(biblioteka, start=1):
#             print(f'{nr}. {pavadinimas}, autorius - {autorius}')
#     else:
#         print('Biblioteka tuscia')
#
# def ieskoti_knygos(biblioteka):
#     paieskos_zodis=input('Iveskite knygos pavadinimo dali:')
#     rasta = False
#     for pavadinimas, autorius in biblioteka:
#         if paieskos_zodis.lower() in pavadinimas.lower():
#             print(f'rasta: {pavadinimas}, autorius - {autorius}')
#             rasta = True
#     if not rasta:
#         print('Knygu nerasta')
#
# def pagrindine_programa():
#     biblioteka=[]
#     pasisveikinti()
#     while True:
#         pasirinkimas = input('Pasirinkite veiksma: [P]rideti, [R]odyti, [I]eskoti, [B]aigti:').lower()
#         if pasirinkimas == 'p':
#             prideti_knyga(biblioteka)
#         elif pasirinkimas == 'r':
#             rodyti_knyga(biblioteka)
#         elif pasirinkimas == 'i':
#             ieskoti_knygos(biblioteka)
#         elif pasirinkimas == 'b':
#             break
#         else:
#             print('Neatpazintas veiksmas, bandykite dar karta')
# pagrindine_programa()

 # Parašykite funkciją ar_pirminis, kuri patikrina, ar duotas skaičius yra pirminis.

# def ar_pirminis(skaicius):
#     if skaicius <= 1:
#         return False
#     for i in range(2,skaicius):
#         if skaicius % i == 0:
#             return False
#     return True
# print(ar_pirminis(11))

 # 2. Parašykite funkciją gauti_inicialus, kuri priima vardą ir pavardę, ir grąžina jų inicialų eilutę
# def inicialai(vardas, pavarde):
#     return vardas[0].upper() + pavarde[0].upper()
# inicialai = inicialai(vardas="jonas", pavarde="antanavicius")
# print(inicialai)

#3. Sukurkite funkciją ar_teisingas_el_pastas, kuri tikrina, ar elektroninio pašto adresas yra teisingo formato.

# def ar_teisingas_el_pastas(email):
#     if '@' in email and '.com' in email:
#         return True
#     return False
# print(ar_teisingas_el_pastas('alina.nepikta@gmail.com'))


# skaicius = 0
# while skaicius <= 5:
#     print(skaicius)
#     skaicius +=1

# ivestis = ""
# while ivestis != "stop":
#     ivestis = input("Iveskite teksta(iveskite 'stop' noredami uzbaigti)_>")
#     print("Jusu ivestas tekstsa:" + ivestis)


# skaicius = 7
# speliojimas = True
# while speliojimas:
#     vartotojo_ivestis = int(input("Spekite skiciu nuo 1 iki 10_>"))
#     if  vartotojo_ivestis == skaicius:
#         print("sveikiname! Atspejote skaiciu!")
#         speliojimas = False
#
#     else:
#         print("Neteisingas skaicius. Bandykite dar karta!")


#Ar slaptazodis teisingas

# teisingas_slaptazodis = "P@ssw0rd"
# slaptazodis = ""
#
# while slaptazodis != teisingas_slaptazodis:
#     slaptazodis = input("Iveskite slaptazodi_>")
#     if slaptazodis != teisingas_slaptazodis:
#         print("Neteisingas slaptazodis! Prasome bandyti dar karta!")
# print("Sveikiname sekmingai prisijungete prie savo paskyros!")

# sukurkite paprasta skaičiuotuva, kuris veikia,
# kol vartotojas nenusprendžia baigti darbo su juo, naudokikite while cikla.
#
# testi = True
# while testi:
#     skaicius1 = float(input('Prasome ivesti pirmaji skaiciu:'))
#     skaicius2 = float(input('Prasome ivesti antraji skaiciu:'))
#     operacija = input('Pasirinkite operacija(+,-,*,/):')
#     if operacija == '+':
#         Rezultatas = skaicius1 + skaicius2
#     elif operacija == '-':
#         Rezultatas = skaicius1 - skaicius2
#     elif operacija == '*':
#         Rezultatas = skaicius1 * skaicius2
#     elif operacija == '/':
#         Rezultatas = skaicius1 / skaicius2
#     else:
#         print('Neteisinga operacija')
#         continue
#     print(f'Rezultatas:{Rezultatas}')
#     testi = input('Ar norite testi?(taip/ne):') == 'taip'

