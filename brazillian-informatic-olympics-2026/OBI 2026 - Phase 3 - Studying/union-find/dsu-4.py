import sys
N, M = map(int, sys.stdin.readline().split())
connections = [n for n in range(N+1)]
def connect(a, b):
    network_A = search(a)
    network_B = search(b)

    if network_A != network_B:
        connections[network_A] = network_B

def search(x):
    if connections[x] == x:
        return x

    connections[x] = search(connections[x])
    return connections[x]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    connect(A, B)

for i in range(1, N+1):
    search(i)

groups = set(connections)
print(len(groups) - 1)