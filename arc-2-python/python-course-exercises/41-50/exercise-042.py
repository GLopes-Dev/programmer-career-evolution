#Challenge 042 - Redo the "Challenge 035" with the triangles, adding the feature of showing what type of triangle will be formed:
# - Equilateral: All sides equal
# - Isosceles: Two sides equal
# - Scalene: All different sides.

print('=' * 10, '[Challenge 042]', '=' * 10)
s1 = int(input('Side 1: '))
s2 = int(input('Side 2: '))
s3 = int(input('Side 3: '))
if s1 + s2 <= s3 or s1 + s3 <= s2 or s3 + s2 <= s1:
    print('The segments above can not form a Triangle :(')
elif s1 == s2 and s1 == s3:
    print('The segments above can form an Equilateral Triangle!')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('The segments above can form an Isosceles Triangle! ')
elif s1 != s2 and s1 != s3 and s2 != s3:
    print('The segments above can form a Scalene Triangle!')