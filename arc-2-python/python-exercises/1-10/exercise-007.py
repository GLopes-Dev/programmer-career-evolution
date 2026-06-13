#Desafio 007 - Develop a program that reads a student's two grades, calculates, and shows their average
print('=' * 10, '[Challenge 007]', '=' * 10)
n1 = float(input('First Grade: '))
n2 = float(input('Second Grade: '))
print('=' * 20)
def average(g1, g2):
    med = (g1 + g2) / 2
    print(f"The student's average is {med}")
    print('=' * 20)
average(n1, n2) 


#Learned how to define and use functions in Python. The function 'average' takes two parameters (g1 and g2), calculates their average, and prints the result in a formatted string.
#Learned it from TikTok