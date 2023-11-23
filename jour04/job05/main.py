# 'S' comme Stage en Anglais, définie juste les étapes. D'où : S2, S3 et S4
L= ["1", "2", "3", "4", "5"]
print(L)

#Affichage de la deuxième valeur de la liste.
S2 = L[1]
print(S2)

def S3(L):
    L[3] = L[2] + L[4]

S3(L)
print(L)

S4= L[-1]
print(S4)