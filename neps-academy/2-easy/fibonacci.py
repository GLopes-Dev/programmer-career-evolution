N = int(input())
tot1 = 1
tot2 = 1
if N == 0:
    print(1)
elif N == 1:
    print(1)
else:
    for i in range(2, N+1):
        tot3 = tot1 + tot2
        tot1 = tot2
        tot2 = tot3
    print(tot3)