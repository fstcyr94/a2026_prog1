print("allo")

a = 10 #variable entière
b = 3 # variable entière
c = 3.3 # variable flottante
d = "abc" # variable chaine de caractères (string)
e = True # variable booléenne
"""
a = a + 10 # ajout de 10 à a
a = a - 10 # soustraction de 10 à a
a = a * 10 # multiplication par 10
a = a / 10 # division par 10

a = a **b # a exposant b (qui est 3)
print(a) # donne 1000
a = a / b # a divisé par b (donc divisé par 3)
print(a) # donne 333.33333333333333 """
print(10/3) # va toujours donner un nombre float
print(10//3)

print(10%3) # équivaut à 10//3 qui donne 3 (donc 3 paquet de 3) DONC il me reste 1 entier qui n'est dans aucun paquet

print(1%2) # équivaut à 1//2 qui donne 0 car on ne peutpas faire aucun paquet de 2 MAIS il me reste 1 entier pareil

# débugger on met un point rouge en cliquant à gauche de la ligne. Ça nous donne l'état des variable AVANT d'exécuter la ligne ou le débugger est placé
a = a + 1
# OU ON PEUT FAIRE
a += 1
print(a)