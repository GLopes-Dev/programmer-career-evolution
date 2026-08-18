niveis = []
for a in range(4):
    A = int(input())
    niveis.append(A)
niveis.sort()
t1 = niveis[0] + niveis[-1]
t2 = niveis[1] + niveis[2]
print(abs(t1 - t2))