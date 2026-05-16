**Python ------- Arco 1**

Comandos:
print()
input()
int()
float()
if
else
elif
.format() "Formata uma variavel para caber dentro das aspas de um texto"


==============
**Aula 4 [=====]**
==============

Função PRINT
------------
Aspas em caracteres são usadas primordialmente para exibir um texto na tela
Numeros são usados na maioria das vezes para cálculos, sem necessidade das aspas ("/')
Para juntar mensagens basta colocar (+) entre elas.
Para o print abaixo não continuar na linha de baixo, mas sim continuar na mesma linha do print acima, basta colocar (, end='')

Variáveis
---------
Todas as variáveis em Python são OBJETOS
Para atribuir algo a uma variável basta utilizar o símbolo (=)
Exemplo:

Nome = 'Gabriel'
(Variável nome RECEBE texto 'Gabriel')


"input" é um comando de entrada, onde o computador recebe algum valor ou caractere que o usuário digita e guarda em determinada variável


=============
**Aula 6 [=====]****
=============
Tipos primitivos

int() - Numeros inteiros (7, 5, -15, 9786)
bool() - Valores lógicos (True & False)
str() - Tipo Caracteres ('Bola' - 'Caderno' - 'Qualquer texto que estiver entre aspas')
float() - Numeros reais (-15.4444 - 3.141516414 - 5.34 - 9.0)

Função .format

O comando .format substitui as chave {} que estiver dentro de uma string no print
print('O valor de {}'.format(s))
A função .format vai pegar o conteúdo que estiver dentro de seu parentêses .format(aqui) e vai jogá-lo dentro das chaves que está dentro do conteúdo da string anterior
print('O valor da soma é {aqui}'.format(soma))

Função Type
Mostra o tipo primitivo de uma váriavel
print(type(n1))


Funções is()

.isnumeric() Mostra se o conteudo digitado pelo usuario é númerico ou não e retorna True ou False
.isalpha() Mostra se o conteudo digitado pelo usuário é alfabético ou não (se possui somente letras) e retorna True ou False
.isalnum() Mostra se o conteúdo digitado pelo usuário é alfabético e númerico (se possui letras ou números) e retorna True ou False
.isupper() Mostra se o conteúdo digitado pelo usuário possui somente letras MAIÚSCULAS e retorna True ou False
Ex:
n = input('Type anything: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())






=============
**Aula 7 [=====]**
=============
Operadores Aritméticos e Ordem de precedência
Simbolo de Igualdade em Python: ==

*Operadores:*
(+ e -) Adição e Subtração
(*) Multiplicação
(/) Divisão
(**) Exponenciação/Potência
(//) Divisão Inteira
(%) Módulo/Resto da divisão

pow() Potenciação
Raiz quadrada = numero**(1/2)
Raiz cubica = numero**(1/3)

*Ordem:*

() Parênteses
(**) Exponenciação/Potência
(*, /, //, %) Multiplicação, Divisão, Divisão Inteira, Módulo/Resto da Divisão
(+, -) Adição e Subtração


**Formatação de Espaços:**

print('Prazer em te conhecer {}'.format(name))
{:20} Vinte espaços
{:>20} Vinte espaços para direita
{:<20} Vinte espaços para esquerda
{:^20} Vinte espaços pros dois lados
{:=^20} Vinte espaços centralizados preenchidos com qualquer simbolo depois do :

**Formatação de casas Decimais:**

{:.3f} O numero é a quantidade de casas decimais que você quer que apareça, o F significa flutuante, float que é real em Python






