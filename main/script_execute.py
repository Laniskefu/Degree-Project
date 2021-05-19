import os, sys
from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter
from main.exceptions.interpret_exception import InterpretException,InterpretException2


def script_execute(path, print_tokens=False, print_ast=False, print_var=False):
    """
    path: relative path from current working directory to the script
    print_tokens: whether to print lexical analysis result or not
    print_ast: whether to print syntactic analysis result or not
    print_var: whether to print executing result or not
    """
    with open(path, "r") as file:
        program = file.read()

    try:
        # lexical analysis
        token_list = lexer(program)
        if print_tokens:
            TokenListPrinter.print(token_list)

        # syntactic analysis
        ast_root = Parser(token_list).parse_statement_list()
        interpreter = Interpreter()
        if print_ast:
            ASTTreePrinter().print(ast_root)

        # semantic analysis and execution
        interpreter.interpret_statement_list(ast_root)
        if print_var:
            print(interpreter.get_variables())
    except (InterpretException, InterpretException2) as e:
        if sys.platform == 'darwin':
            print(os.getcwd() + '/' + path)
        else:
            print(os.getcwd() + '\\' + path.replace('/', '\\'), end=' ')
        print(e, end='')


if __name__ == "__main__":
    script_execute("../test_interpreter/test_cases/error_handling/iii_semantic_error/test_10_vertcat_matrix.m")
