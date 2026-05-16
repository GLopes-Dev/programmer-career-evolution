/////////Is able to drive?
/////////Ask actual years and birth year
/////////Considering 18 years as the majority, >=18 can drive, <18 can't drive

algoritmo "Able to drive?"
var
    year_actual: inteiro
    year_birth: inteiro
    age: inteiro
inicio
    escreval("----------------------------------")
    escreval("        TRANSIT DEPARTMENT        ")
    escreval("----------------------------------")
    escreva("What year is now? ")
    leia(year_actual)
    escreva("What's your birth year? ")
    leia(year_birth)
    age <- year_actual - year_birth
    escreval("-------- STATUS --------")
    escreval(" AGE: ", age)
    se (age >= 18) entao
        escreval("YOU'RE ABLE TO GET A DRIVER LICENSE")
    senao
        escreval("YOU'RE NOT ABLE TO GET A DRIVER LICENSE")
    fimse
    escreval("------------------------")
fimalgoritmo



///////Aproved or Failed?
///////Ask first note and second note,
///////Considering 7 as the minimium to pass

algoritmo "Approved or Failed?"
var
    grade1, grade2: real
    totalGrade: real
inicio
    escreval("-----------------------------------")
    escreval("  Oscar Macedo Soares High School  ")
    escreval("-----------------------------------")
    escreval("First grade: ")
    leia(grade1)
    escreval("Second grade: ")
    leia(grade2)
    totalGrade <- (grade1 + grade2) / 2
    escreval("-----------------------------------")
    escreval(" Final Average: ", totalGrade)
    se (totalGrade >= 7) entao
        escreval(" APPROVED ")
    senao
        escreval(" FAILED ")
    fimse
    escreval("-----------------------------------")
fimalgoritmo


//////////Movie Theater
///// A movie theater has a special price for children and seniors
///Adult price: R$30,00. Discount price (Children/Seniors): R$15,00
//// Write a program in Portugol that asks for the user's age.
////Children age: <12. Senior age: >65

algoritmo "Movie Theater"
var
    age: inteiro
inicio
    escreval("----------------------------------------")
    escreval("    WELCOME TO BACAXÁ MOVIE THEATER!")
    escreval("----------------------------------------")
    escreval("Informations:")
    escreval("The tickets price for Adults and Teens is R$30,00.")
    escreval("Childrens and Seniors have discout, pays only RS$15,00.")
    escreval("----------------------------------------")
    escreval("What's your age?")
    leia(age)
    escreval("----------------------------------------")
    escreval("Age: ", age)
    se (age <= 12) ou (age >= 65) entao
        escreval("The ticket price is: R$15,00.")
    senao
        escreval("The ticket price is: R$30,00.")
    fimse  
fimalgoritmo



/////////////////Student Perfomance
///Considering: 
//A = 10 - 9
//B = 8.9 - 8
//C = 7.9 - 7
//D = 6.9 - 6
//E = 5.9 - 5
//F = <500


algoritmo "Student Perfomance"
var
    note1, note2, finalNote: real

inicio
        escreval("------------------------------------------")
        escreval("      OSCAR MACEDO SOARES HIGH SCHOOL     ")
        escreval("------------------------------------------")
        escreval("First grade: ")
         leia(note1)
        escreval("Second grade: ")
         leia(note2)
         finalNote <- (note1 + note2) / 2
        escreval("------------------------------------------")
        escreval(" AVERAGE: ", finalNote)
        se (finalNote <= 10) e (finalNote >= 9) entao
            escreval(" PERFOMANCE: A")
        senao
            se (finalNote <= 8.9) e (finalNote >= 8) entao
                escreval(" PERFOMANCE: B")
            senao
                se (finalNote <= 7.9) e (finalNote >= 7) entao
                    escreval(" PERFOMANCE: C")
                senao
                    se (finalNote <= 6.9) e (finalNote >= 6) entao
                        escreval(" PERFOMANCE: D")
                    senao
                        se (finalNote <= 5.9) e (finalNote >= 5) entao
                            escreval(" PERFOMANCE: E")
                        senao
                            escreval(" PERFOMANCE: F")
                        fimse
                    fimse
                fimse
            fimse
        fimse       
fimalgoritmo






/////Football Round
/////Create a program that asks for how many goals each team made, calculate the difference between the goals, and according to the difference, 
//tells if it was a draw, normal round or a goleada
//Considering: 0 difference between the goals = a draw
// 5 difference between the goals = goleada
// Difference <5 between the goals = normal round

algoritmo "Football round"
var
    score1, score2, diff: inteiro
inicio
        escreval(" ---------------------------------- ")
        escreval("|          FOOTBALL MATCH          |")
        escreval("|          BRASIL X FRANCE         |")
        escreval("|              (FINAL)             |")
        escreval(" ---------------------------------- ")
        escreval("How many goals BRASIL scored? ")
            leia(score1)
        escreval("How many goals FRANCE scored? ")
            leia(score2)
        se (score1 > score2) entao
            diff <- score1 - score2
        senao
            diff <- score2 - score1
        fimse
        escreval("------------------------------------")
        escreval(" GOALS DIFFERENCE: ", diff)
        escreval("")
        escolha diff
         caso 0
            escreval(" STATUS: TIED")
         caso 1, 2, 3, 4
            escreval(" STATUS: NORMAL MATCH")
         outrocaso
            escreval(" STATUS: GOLEADA")
        fimescolha
        se (score1 > score2) entao
            escreval(" WINNER: BRASIL")
        senao
            escreval(" WINNER: FRANCE")
        fimse
fimalgoritmo