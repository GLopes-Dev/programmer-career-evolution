import sys
N, C = map(int, sys.stdin.readline().split())
estabulos = list(map(int, sys.stdin.readline().split()))
estabulos.sort()

def consegue_encaixar(estabulos, C, d):
    ultima_pos = estabulos[0]
    C -= 1
    for e in range(1, N):
       if C == 0:
           break
       if estabulos[e] - ultima_pos >= d:
           ultima_pos = estabulos[e] 
           C -= 1

    return C

def search(estabulos, C):
    left = 0
    right = max(estabulos) - min(estabulos)
    while left <= right:
        d = (left + right) // 2
        if consegue_encaixar(estabulos, C, d) <= 0:
            ans = d
            left = d + 1
        else:
            right = d - 1

    return ans

distancia_max = search(estabulos, C)
print(distancia_max)

