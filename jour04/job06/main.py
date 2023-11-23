def échange(L):
    if L:
        L[0], L[-1] = L[-1], L[0]

L = [1, 2, 3, 4, 5]
print(L)

échange(L)

print(L)