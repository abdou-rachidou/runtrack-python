def si_chaîne_contient_caractère_e(chaine):
    return 'e' in chaine or 'E' in chaine

chaine = "Ma maman va bien"

if si_chaîne_contient_caractère_e(chaine):
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
