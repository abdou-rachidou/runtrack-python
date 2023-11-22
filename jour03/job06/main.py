def vérifier_statut(nombre):
    if nombre > 0:
        return "positif"
    elif nombre < 0:
        return "negatif"
    else:
        return "nul"

resultat = vérifier_statut(-1)
print(resultat)