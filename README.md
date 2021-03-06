# A Python implemented MATLAB code interpreter

## Description
This is a Python implemented MATLAB code interpreter, 
supporting a subset of the functionalities of the MATLAB language:

- Operators and Elementary Operations
- Loops and Conditional Statements
- Matrices and Arrays
- Data Types

To get the full explanation of all the features realized,
please look at the [manual](MANNUL.md).  

To understand the background as well as the aims and expectations of the project, 
the implementation details including data structures, algorithms and tools applied, 
how unittest are carried out on the project,
or some possibles future work such as unsolved bugs, planed upgrade features, optimization direction, or research areas, 
please read the [report](REPORT.pdf) for this project.  

## Run
#### Environment
- Python
  - with version no lower than 3.7
  - numpy (futures)
- MATLAB (only for comparing outputs in the unittest module)
  - make sure that the root directory of MATLAB is added to system PATH
    - like "/Applications/MATLAB_R2021a.app/bin" in macOS
    - type "matlabroot" to print installation directory from MATLAB software
#### Command
###### Mac OS
```shell
python3 MiniMATLAB.py [-h] [-t T] [-a A] [-v V] [file]
```
###### Windows
```shell
python MiniMATLAB.py [-h] [-t T] [-a A] [-v V] [file]
```

## Examples
Like most interpreted language, two types of running methods namely interactive execute and script execute are supported.  
#### Show Help Information
```shell
 % python3 MiniMATLAB.py -h
usage: MiniMATLAB.py [-h] [-t T] [-a A] [-v V] [file]

positional arguments:
  file         program read from script file

optional arguments:
  -h, --help   show this help message and exit
  -t T, --t T  print tokens
  -a A, --a A  print abstract syntax tree
  -v V, --v V  print variables
```
#### Interactive Execute (REPL Execute)
If the filename after MiniMATLAB.py is not specified, 
the interpreter will execute commands from standard input. 
```
% python3 MiniMATLAB.py
>> 1 & 0 | 1 == 2 < 5 + 5

ans =

  logical

    1

>> --++--+-123*45++--++-+-ans

ans =

       -5534

>> >> a = 1+2; b = 3+4;
>> c = a*b, d = a/b

c =

     21


d =

     0.4286

>> if a < 10 a, end

a =

     3

>> while b < 10 b = b + 1, end

b =

     8


b =

     9


b =

     10

>> 1:5

ans =

     1     2     3     4     5

>> for a = 1:2:10 a, end

a =

     1


a =

     3


a =

     5


a =

     7


a =

     9

>> a = [1 2; 3 4]

a =

     1     2
     3     4

>> a'

ans =

     1     3
     2     4

>> b = [a a; a a]

b =

     1     2     1     2
     3     4     3     4
     1     2     1     2
     3     4     3     4

>> c = [1:4; 5 6 7 8]

c =

     1     2     3     4
     5     6     7     8

>> 
```

#### Script Execute
If the filename after MiniMATLAB.py is specified, the interpreter run the script. 
In this example the tokens and abstract syntax tree are printed
```
% python3 MiniMATLAB.py test_interpreter/test_cases/example.m -a=True -t=True
row =   1        col =   0        type = IDENTIFIER        text = 'a'
row =   1        col =   2        type = ASS               text = '='
row =   1        col =   4        type = NUMBER_LIT        text = '0'
row =   1        col =   5        type = EO_STMT           text = ';'
row =   1        col =   6        type = EO_STMT           text = '\n'
row =   2        col =   0        type = KEYWORD           text = 'while'
row =   2        col =   6        type = IDENTIFIER        text = 'a'
row =   2        col =   8        type = REL               text = '<'
row =   2        col =  10        type = NUMBER_LIT        text = '10'
row =   2        col =  12        type = EO_STMT           text = '\n'
row =   3        col =   4        type = IDENTIFIER        text = 'a'
row =   3        col =   5        type = EO_STMT           text = '\n'
row =   4        col =   4        type = IDENTIFIER        text = 'a'
row =   4        col =   6        type = ASS               text = '='
row =   4        col =   8        type = IDENTIFIER        text = 'a'
row =   4        col =  10        type = ADD               text = '+'
row =   4        col =  12        type = NUMBER_LIT        text = '1'
row =   4        col =  13        type = EO_STMT           text = ';'
row =   4        col =  14        type = EO_STMT           text = '\n'
row =   5        col =   0        type = KEYWORD           text = 'end'
row =   5        col =   3        type = EO_STMT           text = '\n'

STMT_LIST: None
  ├── ASS_STMT: None
  │     ├── ASS_EXP: '='
  │     │     ├── IDENTIFIER: 'a'
  │     │     └── NUMBER_LIT: '0'
  │     └── EO_STMT: ';'
  └── ITR_STMT: None
        ├── ITR_CLS: 'while'
        │     ├── BSO_EXP: '<'
        │     │     ├── IDENTIFIER: 'a'
        │     │     └── NUMBER_LIT: '10'
        │     └── STMT_LIST: None
        │           ├── EXP_STMT: None
        │           │     ├── IDENTIFIER: 'a'
        │           │     └── EO_STMT: '\n'
        │           └── ASS_STMT: None
        │                 ├── ASS_EXP: '='
        │                 │     ├── IDENTIFIER: 'a'
        │                 │     └── BSO_EXP: '+'
        │                 │           ├── IDENTIFIER: 'a'
        │                 │           └── NUMBER_LIT: '1'
        │                 └── EO_STMT: ';'
        └── EO_STMT: '\n'


a =

     0


a =

     1


a =

     2


a =

     3


a =

     4


a =

     5


a =

     6


a =

     7


a =

     8


a =

     9


```