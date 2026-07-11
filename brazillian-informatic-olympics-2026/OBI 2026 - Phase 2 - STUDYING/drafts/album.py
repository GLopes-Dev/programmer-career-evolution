import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
figs = set()
for l in range(M):
    fig = int(sys.stdin.readline())
    figs.add(fig)
print(N - len(figs))
