#Challenge 040 - Make a program that reads two grades from a student and calculates their average, displaying a message at the end, according to the average achieved:
# - Average lower than 5.0: Failed.
# - Average between 5.0 and 6.9: Retake.
# - Average 7.0 or higher: Approved.

print('=' * 10, '[Challenge 040]', '=' * 10)
n1 = float(input('First grade: '))
n2 = float(input('Second grade: '))
avg = (n1 + n2) / 2
print(f"Having {n1} and {n2}, the student's average is {avg}")
if avg >= 7:
    print('The student has passed.')
elif avg >= 5:
    print('The student is in remedial classes.')
else:
    print('The student failed.')
    