N = int(input())
mines = [int(input()) for _ in range(N)]

for i in range(N):
    minas = mines[i]
    if i > 0:
        minas += mines[i - 1]
    if i < N - 1:
        minas += mines[i + 1]
    print(minas)