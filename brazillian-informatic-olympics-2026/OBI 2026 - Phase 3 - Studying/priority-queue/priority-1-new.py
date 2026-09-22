import heapq as hp
N = int(input())
fila = list(map(int, input().split()))
hp.heapify(fila)
for _ in range(N):
    print(hp.heappop(fila), end=" ")