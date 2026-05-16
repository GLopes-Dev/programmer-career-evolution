**Python ------- Arco 1**

Commands:
print()
input()
int()
float()
if
else
elif
.format() "Formats a variable to fit within the quotation marks of a text."


==============
**Lesson 4 [=====]**
==============

PRINT function
------------
Quotation marks in characters are primarily used to display text on the screen.
Numbers are mostly used for calculations, without the need for quotation marks ("/').
To join messages, simply place (+) between them.
To make the print below not continue on the next line, but instead continue on the same line as the print above, simply use (, end='').

Variables
---------
All variables in Python are OBJECTS
To assign something to a variable, simply use the symbol (=)
Example:

Name = 'Gabriel'

(Variable name RECEIVES text 'Gabriel')


"Input" is an input command, where the computer receives a value or character that the user types and stores it in a specific variable.

=============
**Lesson 6 [=====]****
=============
Primitive Types

int() - Integers (7, 5, -15, 9786)
bool() - Logical values ​​(True & False)
str() - Character type ('Ball' - 'Notebook' - 'Any text between quotation marks')
float() - Real numbers (-15.4444 - 3.141516414 - 5.34 - 9.0)


The `.format` function

The `.format` command replaces the curly braces `{}` within a string in the print statement:
`print('The value of {}'.format(s))`
The `.format` function will take the content within its parentheses `.format(here)` and place it inside the curly braces within the previous string:
`print('The sum is {here}'.format(sum))`

The `Type` function:
Shows the primitive type of a variable:
`print(type(n1))`


The `is()` function:

`.isnumeric()` Displays whether the content entered by the user is numeric or not and returns True or False.
`.isalpha()` Displays whether the content entered by the user is alphabetic or not (if it only has letters) and returns True or False.
`.isalnum()` Displays whether the content entered by the user is alphabetic and numeric (if it has letters or numbers) and returns True or False.
`.isupper()` Displays whether the content entered by the user has only UPPERCASE letters and returns True or False.

Example:
n = input('Type anything: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())





=============
**Lesson 7 [=====]**
=============
Arithmetic Operators and Order of Precedence
Equality Symbol in Python: ==

*Operators:*
(+ and -) Addition and Subtraction
(*) Multiplication
(/) Division
(**) Exponentiation/Power
(//) Integer Division
(%) Modulus/Remainder of Division

pow() Exponentiation
Square root = number**(1/2)
Cube root = number**(1/3)

*Order:*

() Parentheses
(**) Exponentiation/Power
(*, /, //, %) Multiplication, Division, Integer Division, Modulus/Remainder of Division
(+, -) Addition and Subtraction

**Space Formatting:**

print('Nice to meet you') {}'.format(name))
{:20} Twenty spaces
{:>20} Twenty spaces to the right
{:<20} Twenty spaces to the left
{:^20} Twenty spaces to both sides
{:=^20} Twenty centered spaces filled with any symbol after the :

**Decimal Place Formatting:**

{:.3f} The number is the number of decimal places you want to appear, the F means floating point, float which is real in Python



==========
**Lesson 8 [----]**
==========
**Python Modules**

*How to import modules/libraries?*
`import libraryname` - it imports all the functions inside this library

*How to import a SPECIFIC function from a library?*

`from libraryname import functionname` - it imports the specified function from the chosen library
`from libraryname import functionName, functionName` - it imports two or more functions from the chosen library

**Standard Libraries:**

`import math` - It's a mathematics library, it comes with a lot of extras functions like:

`ceil()` - Makes a round up.
`floor()` - Makes a round down
`trunc()` - Removes numbers from the decimal point onwards
`pow()` - Calculates the power of two numbers.
`sqrt()` - Calculates the Square Root of a number.
`factorial` - Calculates the Factorial of a number.
