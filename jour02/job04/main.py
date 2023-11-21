def tables_multiplication(N):
    if N <= 0:
        print("Veuillez saisir un entier supérieur à zéro.")
        return
    
    for i in range(1, N+1):
        print("\nTable de multiplication de {} :".format(i))
        for j in range(1, 11):
            produit = i * j
            print("{} x {} = {}".format(i, j, produit))

try:
    N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
    tables_multiplication(N)
except ValueError:
    print("Veuillez saisir un nombre entier valide.")
