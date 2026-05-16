algoritmo "Creuza01"
var
  ano_atual: inteiro
  ano_nasc: inteiro
  idade: inteiro
inicio
                escreval("What year is it? ")
                leia(ano_atual)
                escreval("In what year was I born? ")
                leia(ano_nasc)
                idade <- ano_atual - ano_nasc
                escreva("In  ", ano_atual, " you will have ", idade, " years old")
                Se (idade >= 21) entao
                    escreva(" and you will have reached the age of majority. ")
                senao
                    escreva(", but you will not have reached the age of majority yet.")
                FimSe
fimalgoritmo


//////////

algoritmo "ParOuImpar"
var
        N: inteiro
inicio
            ("Write any number: ")
            leia(N)
            Se (N % 2 = 0) entao
                escreval("The number ", N, " is PAIR")
            senao
                escreval("The number ", N, " is INPAIR")
            fimSe     
fimalgoritmo

///////////

algoritmo "Student"
var
    grade1, grade2, average: real
inicio
        escreva("First Grade: ")
         leia(grade1)
        escreva("Second Grade: ")
         leia(grade2)
         average <- (grade1 + grade2) / 2
        escreval("The student average is ", average:4:2)
         se (average >= 7) entao
            escreval("Student APPROVED.")
        senao
            se (average >= 5) e (average <7) entao
                escreval("Student in RECOVERY.")
            senao
                escreval("Student FAILED.")
            fimse
        fimse
fimalgoritmo


//////////////

algoritmo "IMC"
var
    weight, height, imc: real
inicio
        escreval("Your weight in KG: ")
        leia(weight)
        escreval("Your height in meters: ")
        leia(height)
        imc <- weight / (height ^ 2)
        escreval("Your IMC is: ", imc:3:1)
        se (imc <17) entao
            escreval("You're very underweight")
        senao
             se (imc >= 17) e (imc <18.5) entao
                escreval("You're underweight")
             senao
                  se (imc >= 18.5) e (imc <25) entao
                     escreval("You're in your ideal weight")
                  senao
                       se (imc >= 25) e (imc <30) entao
                          escreval("You're overweight")
                       senao
                            se (imc >= 30) e (imc <35) entao
                                escreval("You're on obesity")
                            senao
                                 se (imc >= 35) e (imc <40) entao
                                    escreval("You're on severe obesity")
                                 senao
                                      se (imc >= 40) entao
                                        escreval("You're on morbid obesity")
                                      fimse
                                 fimse
                            fimse
                        fimse
                    fimse
                fimse 
            fimse
        fimse
fimalgoritmo


////////////////

algoritmo "CriançaEsperança"
var
    donate: real
    userValue: real
inicio
        Escreval("--------------------------------")
        Escreval("        CRIANÇA ESPERANÇA       ")
        Escreval("--------------------------------")
        Escreval("    Muito obrigado por ajudar   ")
        Escreval(" [1] to donate R$10 ")
        escreval(" [2] to donate R$25 ")
        escreval(" [3] to donate R$50 ")
        escreval(" [4] to donate other values ")
        escreval(" [5] to cancel ")
        leia(donate)
        Escolha donate
            Caso 1
                escreval("You donated R$10 ")
            Caso 2
                escreval("You donated R$25 ")
            Caso 3
                escreval("You donated R$50 ")
            Caso 4
                escreval("Type how much do you want to donate: ")
                leia(userValue)
                escreval("You donated R$", userValue)
            Caso 5
                escreval("Canceled. Thanks for your time.")
        fimescolha 
fimalgoritmo

/////////////////

algoritmo "DependentesFuncionario"
var
    name: caractere
    salary: real
    dep: inteiro
    newSalary: real
inicio
        escreva("What's the employee name? ")
        leia(name)
        escreva("What's the employee salary? ")
        leia(salary)
        escreva("How many dependents the employee have? ")
        leia(dep)
        escolha dep
            caso 0
                newSalary <- salary + (salary*5/100)
            caso 1, 2, 3
                newSalary <- salary + (salary*10/100)
            caso 4, 5, 6 
                newSalary <- salary + (salary*15/100)
            outrocaso
                newSalary <- salary + (salary*18/100)
        fimescolha
        escreval(name, " new's salary is R$", newSalary:5:2)
fimalgoritmo



 
