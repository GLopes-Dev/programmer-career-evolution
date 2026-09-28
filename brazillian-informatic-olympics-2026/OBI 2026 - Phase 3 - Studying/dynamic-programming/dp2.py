N, C = map(int, input().split())
objetos = []
for _ in range(N):
    p, v = map(int, input().split())
    objetos.append((p, v))

dp = [[0] * (C+1) for _ in range(N+1)]

for i in range(1, N+1):
    peso, valor = objetos[i - 1]
    for j in range(1, C+1):
        if peso > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-peso] + valor
            )

print(dp[N][C])