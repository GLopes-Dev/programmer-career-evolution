N = int(input())
intervalos = []
qtd = 0
for i in range(N):
    a, b = map(int, input().split())
    intervalos.append((a, b))
intervalos = sorted(intervalos, key=lambda t: t[-1])
x = -(10**9) - 1
for i, f in intervalos:
    if x < i:
        x = f
        qtd += 1

print(qtd)

