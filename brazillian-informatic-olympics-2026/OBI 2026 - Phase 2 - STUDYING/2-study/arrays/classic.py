n = int(input())
numeros = list(map(int, input().split()))
tamanho = len(numeros)
for n in range(tamanho):
    eh_maior = True

    if n > 0 and numeros[n] <= numeros[n-1]:
        eh_maior = False
    if n < tamanho - 1 and numeros[n] <= numeros[n+1]:
        eh_maior = False
    if eh_maior:
        print(f"{numeros[n]} é um pico")