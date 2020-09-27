# noinspection PyUnreachableCode
def multiply_all_except_me(L):
    Multiply_L = []
    for l in L:
        k=L.index(l)
        L1 = L[:k]
        L2 = L[k + 1:]

        M1 = 1
        M2 = 1

        if L1:
            for l1 in L1:
                M1 = M1 * l1
        else:
            M1 = 1

        if L2:
            for l2 in L2:
                M2 = M2 * l2
        else:
            M2 = 1

        M = M1 * M2
        Multiply_L.append(M)

    return Multiply_L


L = [1, 2, 3, 4, 5]
K = multiply_all_except_me(L)
print(K)
