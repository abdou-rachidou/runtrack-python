def verification(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        return f"Le nombre {nombre} est pair." if nombre % 2 == 0 else f"Le nombre {nombre} est impair."
    else:
        return "Veuillez entrer un nombre entier positif."

valeur1 = 5
valeur2 = 100
valeur3 = 7
valeur4 = 11

results = [verification(valeur1), verification(valeur2), verification(valeur3), verification(valeur4)]

print("\n".join(results))