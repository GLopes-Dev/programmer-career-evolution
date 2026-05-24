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
**Lesson 4 [2026-05-12]**
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
**Lesson 6 [2026-05-13]****
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
**Lesson 7 [2026-05-14]**
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

print('Nice to meet you') {}'.format(name)
{:20} Twenty spaces
{:>20} Twenty spaces to the right
{:<20} Twenty spaces to the left
{:^20} Twenty spaces to both sides
{:=^20} Twenty centered spaces filled with any symbol after the :

**Decimal Place Formatting:**

{:.3f} The number is the number of decimal places you want to appear, the F means floating point, float which is real in Python



==========
**Lesson 8 [2026-05-16]**
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


==========
**Lesson 9 [2026-05-19]**
==========
**Manipulating Strings**

**Slicing Strings**
`var = 'Hello, World'`
`var[5]` - Shows the letter associated with the position inside the brackets
`var[0:5]` - Displays the letters from the first specified position to the second specified position. 
`var[1:8:2]` - Displays the letters from the first specified position to the second specified position, but the last number determines how many letters will be skiped between them
`var[:6]` - Displays the letters from the FIRST POSITION to the specified position.
`var[3:]` - Displays the letters from the first specified position to the final of the phrase
`var[0::3]` - Displays the letters from the first specified position to the last phrase letter, and the last number determines how many letters will be skiped between them
*Example*
    `print(var)` - *Output:* Hello, World
    `print(var[5])` *Output:* ,
    `print(var[0])` *Output:* H
    `print(var[0:5])` *Output:* Hello    (',' doesn't appears because Python just count to the last specified position, but don't include they)
    `print(var[1:8:2])` *Output:* el,W
*Obs:* Python starts counting the first letter as 0.

**Analysis**
`var = "Hello, I'm Gabriel. I passed in the MEXT Exam and I'll travel to Japan in 2029."`
`len(var)` - Shows the phrase total length (total characters)
`.count('e')` - Shows how many times the specified letter appears within the sentence
`.count('e', 0, 70)` Shows how many times the specified letter appears within the sentence since the first specified position to the second specified position
`.find('MEXT')` - Search in what position the specified characters starts to appears within the sentence
`'MEXT' in var` - Search if the specified string or characters exists inside the sentence
*Example*
    `print(var)` *Output:* Hello, I'm Gabriel. I passed in the MEXT Exam and I'll travel to Japan in 2029.
    `print(len(var))` *Output:* 79 (var has 79 characters)
    `print(var.count('e'))` *Output:* 5  (uppercase "E" doesn't count as lowercase 'e')
    `print(var.count('e', 0, 50))` *Output:* 4
    `print(var.find('MEXT'))` *Output:* 36
    `print('MEXT' in var)` *Output:* True
    `print('dog' in var)` *Output:* False



**Transformation**

`var = "   My Programming Career   "`
`.replace('Career', 'Journey')` - Replaces the first specified character with the second one
`.upper()` - Transforms the whole sentence in Uppercase letters
`.lower()` - Transforms the whole sentence in Lowercase letters
`.capitalize()` - Capitalize the whole sentence (The first letter of the sentence will be shown in Uppercase and the rest will be shown in lowercase)
`.title()` - The first letter of all the words will be shown in Uppercase.
`.strip()` - Remove all the unnecessary whitespace at the beginning and end of the sentence.
`.rstrip()` - Remove all the unnecessary whitespace at the beginning and right side of the sentence.
`.lstrip()` - Remove all the unncessary whitespace at the beginning and left side of the sentence.

**Division**

`var = "  Hello, I'm Gabriel and I'm 15 years old."`
`.split()` - Split the whole sentence into individual lists
*Example:*
    `print(var.split())` *Output:* ['Hello,', 'I'm', 'Gabriel', 'and', 'I'm', '15', 'years', 'old.']
                                    [012345]   [012]  [0123456]  [012]  [012]  [01]  [01234]  [012]

**Junction**
`var = "  Hello, I'm Gabriel and I'm 15 years old."`
`'-'.join(var)` - Transforms the split sentence in a unique sentence, joining the words with the determined characters inside the single quotes.



==========
**Searchs & Solo Studying [2026-05-21]**
==========

* **Save data on .txt files**

`with open("file", "mode") as Name:` 
`   Name.write("N/A")              ` 

Opens the file where you want to save something, working depending on the mode your put after the filename in parentheses. 
The "as Name" save the filename as the name you put after the "as", but only save as it inside the code, it don't change the original filename

The function has "Name.write("N/A")" inside it. The Name.write writes what you want inside the selected file.


Modes
"w" - Deletes what was previously saved in the file and saves the last information entered.
"a" - Add the last information entered to the file and does not delete what was already in it
"r" - Read mode, displays the entire contents of the .txt file in the terminal


==========
**Lesson 10 [2026-05-23]**
==========
**Simple and compound Conditions**


* **Base Condition**

`if` *condition*:
    *True Block*

* **Compound Condition**

`if` *condition*:
    *True Block*
`else`
    *False Block*


* **Fast Condition**
print('*block*' if *object* <=3 else '*second block*')
