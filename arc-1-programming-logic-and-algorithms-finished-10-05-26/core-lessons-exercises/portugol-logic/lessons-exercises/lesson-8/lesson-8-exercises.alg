algoritmo "IMC"
var
    weight, height, imc: real
inicio
        escreval("Your weight in KG: ")
        leia(weight)
        escreval("Your height in meters: ")
        leia(height)
        imc <- weight / (height ^ 2)
        escreval("Your IMC is: ", imc)
        se (imc <17) entao
            escreval("You're very underweight")
        senao
             se (imc >= 17.0) e (imc < 18.5) entao
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