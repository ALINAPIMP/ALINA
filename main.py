from main2 import max_reisme

def maksimali_reiksme(skaiciai):
    return max(skaiciai)
print(maksimali_reiksme([5,22,15]))

# # mano komentaras
# '''
# ilgas
# komentaras
# '''
#
# '''
# norint viską užkomentuoti - spausti CTRL \
# '''
#
# vardas = 'Alina'
# metai = 37
# kaina = 1.5
# tiesa_arba_netiesa = True #Boolean True arba Folse
#
# print(f"Mano vardas {vardas} man yra {metai} metai")
# print(type(tiesa_arba_neriesa))

# vaisiai = ['obuolys', 'citrina', 'bananas', 'kivis']
#
# # print(vaisiai[-1]) - indeksuoja nuo 1
# # print(vaisiai[2]) - pradeda skaičiuoti nuo 0
# # print(len(vaisiai)) # skaičiuoja vnt
#
# vaisiai.append('Mangas')
# vaisiai.insert(2, 'avokadas')
# # vaisiai.remove('bananas') # remove element by value
# # vaisiai.pop(1) # remove element by index
#
# sliced_list = vaisiai[1:4]
# print(sliced_list)
# print(f' Vaisių sarašas:{vaisiai}')
# print(f' Mano vaisių saraše yra {len(vaisiai)} vaisiai')

# 1. Sukurkite sąrašą miestai su Lietuvos miestų pavadinimais: Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys.;
# 2. Pridėkite miestą "Druskininkai" į sąrašą;
# 3. Pašalinkite "Šiauliai" iš miestai sąrašo.
#4. Parašykite kodą, kuris atspausdintų, kiek elementų yra miestai sąraše.

# miestai = ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys']
# print(miestai)
# miestai.append('Druskininkai')
# print(miestai)
# miestai.remove('Šiauliai')
# print(miestai)
# print(len(miestai))


vaisiai = ['obuolys', 'citrina', 'bananas', 'kivis']
# for vaisius in vaisiai:
#   print(f" vaisius: {vaisius}")

# for index, vaisius in enumerate(vaisiai):
#     print(f'index): {vaisius}')

# for i in range(1, 11, 2):
# print(i)

# for vaisius in range(len(vaisiai)):
#     vaisiai[vaisius] = vaisiai[vaisius].lower()
# print('vaisiai mazosiomis raidemis:', vaisiai)

# for vaisius in vaisiai:
#     for raide in vaisius:
#         print(raide)
#     print("----")

# vaisiu_raides = [len(vaisius) for vaisius in vaisiai]
# print(vaisiu_raides)


# ilgiai = []
# for vaisius in vaisiai:
#
#     ilgis = len(vaisius)
#
#     ilgiai.append(ilgis)
#
# print(ilgiai)

# 1. Parašykite programą, kuri naudodama for ciklą, suskaičiuotų ir atspausdintų bendrą visų skaičių nuo 1 iki 50 sumą:
#  Naudokite for ciklą, kad suskaičiuotumėte bendrą sumą, pridedant kiekvieną skaičių nuo 1 iki 50(Naudokite += operatoriu)

# suma = 0
# for skaicius in range(1, 51):
#     suma += skaicius
# print(f"Skaičių nuo 1 iki 50 suma: {suma}")


#2. Parašykite programą, kuri atspausdintų kiekvieną raidę iš jūsų vardo 3 kartus;

# vardas = 'alina'
# for i in vardas:
#     print(3*i)


# if a < 0
# salyga
# elif if a > 0:
# else:
# print()

# age = 18
# if age <13:
#     print('Child')
# elif age < 18:
#     print('Teenager')
# else:
#     print('Adult')


# fruits = ['Apple', 'Cherry', 'Banana']
#
# if 'cherry' in fruits:
#     print('Cherry is in the list')
# else:
#      print('There is no fruit in the list')

# temperature = int(input('Iveskite temperatura:'))
# weather = input("Iveskite oru bukle(sauleta/debesuota/lietinga):")
#
# if temperature > 20 and weather == "sauleta":
#     print('Puiki diena pasivaiksciojimui!')
# elif temperature < 10 or weather == "lietinga":
#     print('Geriau likti namie!')
# else:
#     print("Gera diena knygos skaitimui")

# print('Hello World')
print('5' + '3')  # atsakymas 53
# a = '5'
# b = '3'
# result = a + b
#print(type(result))

# int() - # konvertuoja teksta i skaicius

# name = 'Bob'
# print(name)
