N, M = map(int, input().split())
array = list(map(int, input().split()))
def binary(x):
    left = 0
    right = len(array) - 1
    answer = -1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == x:
            answer = middle
            right = middle - 1
        elif array[middle] > M:
            right = middle - 1
        else:
            left = middle + 1
    left = 0
    right = len(array) - 1
    answer2 = -1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == x:
            answer2 = middle
            left = middle + 1
        elif array[middle] > M:
            right = middle - 1
        else:
            left = middle + 1

    return (answer, answer2)

print(*binary(M))

