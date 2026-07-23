import sys
N = int(sys.stdin.readline())
caixas = list(map(int, sys.stdin.readline().split()))
unicas = list(dict.fromkeys(caixas))
print(*(unicas))