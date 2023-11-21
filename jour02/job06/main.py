def Les_nombres_premiers_de_1000(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

for nombre in range(2, 1001):
    if Les_nombres_premiers_de_1000(nombre):
        print(nombre)
