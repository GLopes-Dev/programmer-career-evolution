times = [
    ["Flamengo", 45, 14, 20],
    ["Palmeiras", 45, 15, 18],
    ["Botafogo", 48, 14, 22]
]

ranking = sorted(times, key=lambda x: (-x[1], -x[2], -x[3], x[0]))
print(ranking)