N, X = map(int, input().split())
moedas = list(map(int, input().split()))


dp = [float("inf")] * (X + 1)
dp[0] = 0

for x in range(1, X+1):
    for m in moedas:
        if x - m >= 0:
            dp[x] = min(dp[x], dp[x-m] + 1)
if dp[X] == float("inf"):
    print(-1)
else:
    print(dp[X])