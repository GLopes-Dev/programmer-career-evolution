S = int(input())
A = int(input())
B = int(input())
tot = 0
for i in range(A, B + 1):
    n = str(i)
    lista_int = [int(caractere) for caractere in n]
    soma = sum(lista_int)
    if soma == S:
        tot += 1
    soma = 0
print(tot)
