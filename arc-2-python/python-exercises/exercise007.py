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
