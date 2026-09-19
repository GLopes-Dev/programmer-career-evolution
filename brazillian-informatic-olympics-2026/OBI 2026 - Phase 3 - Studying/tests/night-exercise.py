N, C = map(int, input().split())
peso_pessoas = list(map(int, input().split()))
botes = 0
peso_pessoas.sort()
i = 0
j = len(peso_pessoas) - 1

while i <= j:
    if i == j:
        botes += 1
        break
    if peso_pessoas[j] + peso_pessoas[i] > C:
        j -= 1
        botes += 1
    else:
        j -= 1
        i += 1
        botes += 1

print(botes)

# [40, 50, 60, 90]
# 0    1   2   3

# C = 100
# maior = 
# menor = 
# botes =
i = 1
j = 1