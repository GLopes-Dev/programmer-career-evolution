bNum = 0
sm = 0
for i in range(5):
    num = int(input())
    sm += num
    if num > bNum:
        bNum = num
print(f'Numbers sum {sm}')
print(f'Biggest number {bNum}')