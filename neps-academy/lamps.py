N = int(input())
L = list(map(int, input().split()))
A = 0
B = 0
for I in L:
    if I == 1:
        if A == 0:
            A = 1
        else:
            A = 0
    else:
        if A == 0 and B == 0:
            A = 1
            B = 1
        elif A == 1 and B == 1:
            A = 0
            B = 0
        elif A == 1 and B == 0:
            A = 0
            B = 1
        else:
            A = 1
            B = 0
print(A)
print(B)
