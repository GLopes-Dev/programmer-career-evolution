N = int(input())
tabela = [list(map(int, input().strip())) for _ in range(N)]
print(tabela)
for l in range(N):
    for c in range(N):
        if tabela[l][c] == 1:
            print("S")