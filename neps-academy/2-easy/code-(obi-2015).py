N = int(input())
sequence = list(map(int, input().split()))
tot = 0
for i in range(N-2):
    if sequence[i] == 1 and sequence[i+1] == 0 and sequence[i+2] == 0:
        tot += 1
print(tot)
