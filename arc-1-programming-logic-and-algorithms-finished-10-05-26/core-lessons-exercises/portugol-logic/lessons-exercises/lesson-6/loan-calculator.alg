algoritmo "loan"
var
    loanAmount: real
    installments: inteiro
    fees: real
    loanTotal: real
    installmentsAmount: real
inicio
            escreva("What is the loan amount? (There's a 20% increase to pay over the requested loan amount) ")
            leia(loanAmount)
            escreva("How many installments?")
            leia(installments)
            fees <- (loanAmount * 20) / 100
            loanTotal <- loanAmount + fees
            installmentsAmount <- loanTotal / installments
            escreval("You gonna pay ", installments, " installments of R$", installmentsAmount)
fimalgoritmo 







/////Situação: Creuza had to get a loan at the bank. While talking with the manager, she got the loan
/////Considering 20% fees and paying in installments
/////Exercise: Create a program for Creuza. She's gonna say how much loan she wants (Exemple: R$1000,00 or US$1000,00). There will be an 20% increase over the loan because of the
/////fees. So for exemple if she wants a loan amount of R$1000,00, because of the loan fees, there will be a 20% increase, so she will need to pay R$1200,00 
////(This is an hipotetical situation). And she can pay in installments, so she will say how many installments she will pay, and the program gonna divide the
//// total loam amount and the installments she said.