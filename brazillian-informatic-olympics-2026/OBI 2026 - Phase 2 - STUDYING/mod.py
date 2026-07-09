mod = (10**9) + 7

N = int(input())
moedas = 1
for p in range(2, N+1):
    moedas = (2 * moedas) % mod
print(moedas)
