n1 = float(input('Grade 1: '))
n2 = float(input('Grade 2: '))
avg = (n1+n2) / 2
if avg > 8:
    print("You have been approved!")
elif avg > 6 and avg < 8:
    print("You barely missed it, but you have been approved!")
else:
    print("You failed!")
print(f"Your average: {avg:.1f}")