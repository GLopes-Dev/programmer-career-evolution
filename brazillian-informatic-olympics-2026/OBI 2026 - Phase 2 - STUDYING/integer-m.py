# A = input()
# B = input()
# tamanho = max(len(A), len(B))
# A = A.zfill(len(tamanho))
# B = B.zfill(len(tamanho))
# for n in range(tamanho):
#     atualA = int(A[n])
#     atualB = int(B[n])
#     if atualA > atualB:
#         B = B[:n] + "-" + B[n+1:]
#     elif atualB > atualA:
#         A = A[:n] + "-" + A[n+1:]
#     else:
#         continue
# A = A.replace("-", "")
# B = B.replace("-", "")
# if A == "": 
#     A = -1 
# elif B == "": 
#     B = -1
# print(min(int(A), int(B)), max(int(A), int(B)))



A = input()
B = input()
tamanho = max(len(A), len(B))
A = A.zfill(tamanho)
B = B.zfill(tamanho)
res_A = []
res_B = []
for n in range(tamanho):
    atualA = int(A[n])
    atualB = int(B[n])

    if atualA > atualB:
        res_A.append(A[n])
    elif atualB > atualA:
        res_B.append(B[n])
    else:
        res_A.append(A[n])
        res_B.append(B[n])
        
res_A = "".join(res_A)
res_B = "".join(res_B)
res_A = int(res_A) if res_A != "" else -1
res_B = int(res_B) if res_B != "" else -1
print(min(res_A, res_B), max(res_A, res_B))

