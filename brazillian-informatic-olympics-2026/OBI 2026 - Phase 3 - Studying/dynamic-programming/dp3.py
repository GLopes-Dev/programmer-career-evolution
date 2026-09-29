N = int(input())
creditos = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = creditos[0]

for i in range(2, N+1):
    credito = creditos[i-1]
    dp[i] = max(credito + dp[i-2], dp[i-1])

print(dp[N])