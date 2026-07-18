tot1 = 0
tot2 = 1
tot3 = 0
print(tot1)
print(tot2)
while tot1 + tot2 < 1000:
    tot3 = tot2 + tot1
    print(tot3)
    tot1 = tot2
    tot2 = tot3