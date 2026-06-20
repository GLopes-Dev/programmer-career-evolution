#Challenge 043 - Develop a logic that reads a person's weight and height, calculates their BMI and displays their status, according to the table below
#Below 18.5: Underweight
#Between 18.5 and 25: Ideal weight
#25 to 30: Overweight
#30 to 40: Obesity
#Above 40: Morbid Obesity

print('=' * 10, '[Challenge 043]', '=' * 10)
weight = float(input('Weight: '))
height = float(input('Height: '))
bmi = weight / height ** 2
print(f"This person's BMI is {bmi:.1f}.")
if bmi < 18.5:
    print("You're \033[1;37mUNDERWEIGHT")
elif bmi < 25:
    print("You're at your \033[1;36mIDEAL WEIGHT.  \033[;37m")
elif bmi < 30:
    print("You're \033[1;31mOVERWEIGHT.  \033[;37m")
elif bmi < 40:
    print("You're on \033[1;31mOBESITY.   \033[;37m")
else:
    print("You're on \033[1;35mMORBID OBESITY. \033[;37m")
