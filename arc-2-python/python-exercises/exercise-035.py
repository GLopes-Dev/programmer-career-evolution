#Challenge 035 - Create a program that reads the legths of the three sides of a triangle, and tells the user whether they can form a triangle or not


print("=" * 10, "[Challenge 035]", "=" * 10)
side1 = float(input("Side 1 size: "))
side2 = float(input("Side 2 size: "))
side3 = float(input("Side 3 size: "))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Can form a triangle.")
else:
    print("Can't form a triangle.")