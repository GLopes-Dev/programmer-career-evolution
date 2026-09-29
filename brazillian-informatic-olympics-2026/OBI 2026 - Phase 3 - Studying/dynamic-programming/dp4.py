N, C = map(int, input().split())
equipamentos = []
for _ in range(N):
    P, V = map(int, input().split())
    equipamentos.append((P, V))

dp = [[0] * (C+1) for _ in range(N+1)]

for i in range(1, N+1):
    peso, valor = equipamentos[i-1]
    for j in range(1, C+1):
        if peso > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-peso] + valor, dp[i-1][j])

print(dp[N][C])
