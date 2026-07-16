valores = [10, 20, 15, 30, 25]
valores.insert(0, -1)
valores.append(-1)
#[-1, 10, 20, 15, 30, 25, -1]
# 0   1   2   3   4   5    6

tamanho = len(valores)
for n in range(1, tamanho - 1):
    if valores[n] > valores[n-1] and valores[n] > valores[n+1]:
        print(f"{valores[n]} é maior que seus vizinhos")
print(valores)