N = int(input())
minefield = list(map(int, input().split()))
if N == 1:
    print(minefield)
else:
    new_minefield = [0] * N
    for i in range(N):
        soma = minefield[i]
        if i == 0:
            soma += minefield[i+1]
        elif i == N-1:
            soma += minefield[i-1]
        else:
            oma += minefield[i-1] + minefield[i+1]
        new_minefield[i] = soma
    print(new_minefield)
