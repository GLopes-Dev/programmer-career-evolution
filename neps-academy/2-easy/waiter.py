
N = int(input())
Tot = 0
for T in range(N):
    L, C = map(int, input().split())
    if L > C:
        Tot += C
print(Tot)