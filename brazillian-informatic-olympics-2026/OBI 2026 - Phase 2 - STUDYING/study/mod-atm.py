mod = 10**9 + 7
N = int(input())
formas = 1
for f in range(2, N+1):
    formas = (2 * formas) % mod
print(formas)