import sys
X = float(sys.stdin.readline())
N = int(sys.stdin.readline())
pessoas = list(map(float, sys.stdin.readline().split()))
elevador = 0
viagens = 0
for peso in pessoas:
    elevador += peso
    if elevador >= X:
        viagens += 1
        elevador = 0
print(viagens)
