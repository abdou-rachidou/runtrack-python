def est_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def type_triangle(a, b, c):
    if a == b == c:
        return "Équilatéral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Rectangle et Isocèle"
        else:
            return "Isocèle"
    else:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Rectangle"
        else:
            return "Quelconque"

a = float(input("Entrez la longueur de la première côté (a) : "))
b = float(input("Entrez la longueur de la deuxième côté (b) : "))
c = float(input("Entrez la longueur de la troisième côté (c) : "))

if est_triangle(a, b, c):
    type_tri = type_triangle(a, b, c)
    print(f"Les longueurs {a}, {b} et {c} peuvent former un triangle de type {type_tri}.")
else:
    print(f"Les longueurs {a}, {b} et {c} ne peuvent pas former un triangle.")
