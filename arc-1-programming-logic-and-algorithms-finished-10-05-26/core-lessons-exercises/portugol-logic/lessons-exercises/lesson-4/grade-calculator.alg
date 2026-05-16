algoritmo "Grade Calculator"
var
   nome: caractere
   n1: real
   n2: real
   m: real
inicio
  Escreval("Hello, good afternoon! What is your name? ")
  Leia(nome)
  Escreval("Welcome ", nome, "!", " To calculate your average grade, please tell me your first grade: ")
  Leia(n1)
  Escreval("Please, tell me your second grade : ")
  Leia(n2)
  m <- (n1 + n2)/2
  Escreva("Congratulations ", nome, "!", " Your final average is ", m)
fimalgoritmo