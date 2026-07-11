accounts = [[1,2,3],[3,2,1]]
richest = 0
for client in accounts:
    wealth = sum(client)
    if wealth > richest:
        richest = wealth
print(wealth)