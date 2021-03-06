from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    # Program
    STMT_LIST = "STATEMENT LIST"

    # Statements
    EXP_STMT = "EXPRESSION STATEMENT"
    SEL_STMT = "SELECTION STATEMENT"
    ITR_STMT = "ITERATION STATEMENT"

    # Statement Components
    EO_STMT = "END OF STATEMENT"
    SEL_ClS = "SELECTION CLAUSE"
    ITR_CLS = "ITERATION CLAUSE"

    # Expressions
    ASS_EXP = "ASSIGNMENT EXPRESSION"
    CLN_EXP = "COLON EXPRESSION"
    UOP_EXP = "UNARY OPERATION EXPRESSION"
    BOP_EXP = "BINARY OPERATION EXPRESSION"
    NUMBER_LIT_EXP = "NUMBER LITERAL EXPRESSION"
    STRING_LIT_EXP = "STRING LITERAL EXPRESSION"
    VECTOR_LIT_EXP = "CHAR ARRAY LITERAL EXPRESSION"
    ARRAY_LIST_EXP = "ARRAY LIST EXPRESSION"
    INDEX_LIST_EXP = "INDEX LIST EXPRESSION"
    IDENT_LIST_EXP = "IDENTIFIER LIST EXPRESSION"
    IDENTIFIER_EXP = "IDENTIFIER EXPRESSION"
