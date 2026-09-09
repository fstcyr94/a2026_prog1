# print(f"{"abcdef":-<27}") # va ajouter des "-" JUSQU'À ce qu'il y ait 27 caractères

# print(f"{"":-<27}")
# -----------------------------------------------------------------------------------------

# > plus grand
# < plus petit
# <= plus petit ou égal
# >= plus grand ou égal
# == égal pour les entiers, PAS POUR LES FLOATS (on ne peut pas mettre = qui lui est une affectation de variable ex : a = 10)
# != est différent

# a=10
# b=20

# print(a<b)

# a= 0.10+0.20
# b= 0.3

# print(a==b) #false car même si la rép. mat est pareil, quand c'est deux float, il va stocker l''info comme ex : a = 0.300000000000000001 et b = 0.30000000000000000

#si on veut que ce soit égal (pour plus d'infor allez dans docs.python.org)

# a= (0.10+0.20)
# b= 0.3

# import math
# print(math.isclose(a,b))
# print(a==b)

# != est différent

a=20
b=20

print (a==b)
print(not math.isclose(a,b))

