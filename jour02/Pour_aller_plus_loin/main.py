def est_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Demander à l'utilisateur les longueurs des côtés du triangle
a = float(input("Entrez la longueur de la première côté (a) : "))
b = float(input("Entrez la longueur de la deuxième côté (b) : "))
c = float(input("Entrez la longueur de la troisième côté (c) : "))

# Vérifier si les longueurs peuvent former un triangle
if est_triangle(a, b, c):
    print("Les longueurs peuvent former un triangle.")
else:
    print("Les longueurs ne peuvent pas former un triangle.")
