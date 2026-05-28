#Challenge 028 - Create a program that make the computer pick a integer number between 0 and 5 and ask the user try to guess what number was chosen by the computer.
# The program may display on the screen whether the user won or lost
import random
print("=" * 10, "[Challenge 028]", "=" * 10)
num = int(random.randint(0, 5))
choice = int(input("Pick up a number between 0 and 5: "))
print(num)
if choice == num:
    print("Congratulations! You got it right! ")
else:
    print("You got it wrong. Try Again!")