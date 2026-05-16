algoritmo "BiDevOs"
var
    //Menu Var's
    num, num1, num2, num3, num4: inteiro
    //Calculator SumSys Var's
    cNum, qtd, bck: inteiro
    sum, usNum: real
    //Calculator SubSys Var's
    qtd1, bck1: inteiro
    sum1, usNum1, uNum1: real
procedimento Menu()
inicio
    limpatela
    escreval(" ==============[03-05-26]============== ")
    escreval("|               Welcome!               |")
    escreval("|  [1] App Hub            [2] Info     |")
    escreval("|  [3] Donate             [4] Leave    |")
    escreval(" ====================================== ")
fimprocedimento
procedimento AppHub()
inicio
    limpatela
    escreval(" =========[App Hub]========= ")
    escreval("| [1] Calculator            |")
    escreval("| [2] Register App          |")
    escreval("| [3] Age Checker           |")
    escreval("| [4] Back...               |")
    escreval(" =========================== ")
fimprocedimento
procedimento Info()
inicio
    limpatela
    escreval(" ========================= ")
    escreval("| Program Name: BiDevOS   |")
    escreval("| Program Version: 3.5.26 |")
    escreval("| Creation Date: 03/05/26 |")
    escreval("| Scripted by GabrielDev  |")
    escreval(" ========================= ")
    escreval(" [1] Back...")
fimprocedimento
procedimento Donate()
inicio
    limpatela
    escreval(" =========[Donate]========= ")
    escreval("| [1] To donate $5        |")
    escreval("| [2] To donate $10       |")
    escreval("| [3] To donate $20       |")
    escreval("| [4] To donate $50       |")
    escreval("| [5] Back...             |")
    escreval(" ========================= ") 
    escreva(" Select Option: ")
fimprocedimento
procedimento Calculator()
inicio
    limpatela
    escreval(" ========================================== ")
    escreval("   W E L C O M E  TO  C A L C U L A T O R   ")
    escreval(" ========================================== ")
    escreval("|               O P T I O N S              |")
    escreval("|------------------------------------------|")
    escreval("| [1] Sum (+)         |   [2] Subtract (-) |")
    escreval("| [3] To divide (÷)   |   [4] Multiply (X) |")
    escreval("| [5] Square Root     |   [6] Power        |")
    escreval("| [7] Back...")
    escreval("|------------------------------------------|")
fimprocedimento
procedimento CalculatorSumSys(q, b: inteiro; s, n: real)
var
    i: inteiro
inicio
    repita
        limpatela
        escreval("==============")
        escreval("  SUM SYSTEM  ")
        escreval("==============")
        escreval("How many numbers do you want to sum? ")
        leia(q)
        escreval("--------------")
        para i de 1 ate q faca
            escreval("Type the ", q, "º number: ")
            leia(n)
            s <- s + n
        fimpara
        escreval("--------------")
        escreval("The sum between the numbers is ", s)
        escreval("--------------")
        escreval("[1] Continue")
        escreval("[2] Back...")
        leia(b)
        s <- 0
    ate (b = 2)
fimprocedimento
procedimento CalculatorSubSys(q, b: inteiro; n, n1, s: real)
inicio
    repita
        limpatela
        escreval("===================")
        escreval("  SUBTRACT SYSTEM  ")
        escreval("===================")
        escreval("Type the first number: ")
        leia(n)
        escreval("Type the second number: ")
        leia(n1)
        s <- n - n1
        escreval("-------------------")
        escreval("The result is ", s)
        escreval("-------------------")
        escreval("[1] Continue")
        escreval("[2] Back")
        leia(b)
        s <- 0
    ate (b = 2)
fimprocedimento
procedimento RegisterApp()
inicio

fimprocedimento
procedimento RegisterAppSys()
inicio

fimprocedimento
procedimento AgeChecker()
inicio

fimprocedimento
procedimento AgeCheckerSys()
inicio

fimprocedimento
inicio
        repita
            Menu()
            escreva("Select Option: ")
            leia(num)
            escolha (num)
                caso 1
                    repita
                        AppHub()
                        escreval("Select Option: ")
                        leia(num1)
                        escolha (num1)
                            caso 1
                                repita
                                    Calculator()
                                    escreva("Select Option: ")
                                    leia(cNum)
                                    escolha (cNum)
                                        caso 1
                                            CalculatorSumSys(qtd, bck, sum, usNum)
                                        caso 2
                                            CalculatorSubSys(qtd1, bck1, usNum1, uNum1, sum1 )
                                    fimescolha
                                ate (cNum = 7)
                            caso 2
                        fimescolha
                    ate (num1 = 4)
                caso 2
                    Info()
                    leia(num2)
                caso 3
                    repita
                        Donate()
                        leia(num3)
                        escolha (num3)
                            caso 1
                                escreval("You donated $5. Thank you!")|
                                escreval("==========================")
                                escreval("[1] Continue")
                                leia(num4)
                            caso 2
                                escreval("You donated $10. Thank you!")
                                escreval("==========================")
                                escreval("[1] Continue")
                                leia(num4)
                            caso 3
                                escreval("You donated $20. Thank you!")
                                escreval("==========================")
                                escreval("[1] Continue")
                                leia(num4)
                            caso 4
                                escreval("You donated $50. Thank you!")
                                escreval("==========================")
                                escreval("[1] Continue")
                                leia(num4)
                        fimescolha
                    ate (num3 = 5)
            fimescolha
        ate (num = 4)
        limpatela
        escreval(" =========[03-05-26]======== ")
        escreval("| Turning Off...            |")
        escreval("| Thank you!                |")
        escreval(" ==========[BiDevOS]=========")
fimalgoritmo