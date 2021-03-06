from main.exceptions.interpret_exception import *


class ArrayIndexError(SemanticException):
    message = {
        'darwin': "Array indices must be positive integers or logical values.\n",
        'win32': "Array indices must be positive integers or logical values."
    }


class ComparisonError(SemanticException):
    message = {
        'win32': f"Error using placeholder\nComparison between placeholder and placeholder is not supported.",
        'darwin': f"Error using placeholder\nComparison between placeholder and placeholder is not supported.\n"
    }


class ConcatenationError(SemanticException):
    message = {
        'win32': f"Error using placeholder\nDimensions of arrays being concatenated are not consistent.",
        'darwin': f"Error using placeholder\nDimensions of arrays being concatenated are not consistent.\n"
    }


class ConversionError1(SemanticException):
    message = {
        'darwin': "Operands to the logical and (&&) and or (||) operators must be convertible to\n"
                  "logical scalar values.\n",
        'win32': "Operands to the logical and (&&) and or (||) operators must be convertible to "
                 "logical scalar values.",
    }


class ConversionError2(SemanticException):
    message = {
        'darwin': "Conversion to logical from string is not possible.\n",
        'win32': "Conversion to logical from string is not possible."
    }


class ConversionError3(SemanticException):
    message = {
        'darwin': "NaN values cannot be converted to logicals.\n",
        'win32': "NaN values cannot be converted to logicals."
    }


class DivisionError(SemanticException):
    message = {
        'win32': f"Error using placeholder\nArguments must be numeric, char, or logical.",
        'darwin': f"Error using placeholder\nArguments must be numeric, char, or logical.\n"
    }


class IncompatibleSizeError(SemanticException):
    message = {
        'darwin': "Arrays have incompatible sizes for this operation.\n",
        'win32': "Arrays have incompatible sizes for this operation."
    }


# windows平台此处message过长，出现180列换行问题，需要修改
class IncorrectDimensionError(SemanticException):
    message = {
        'win32': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of "
                 "columns in the first matrix matches the number of rows in the second matrix. To "
                 "perform elementwise\nmultiplication, use '.*'.",
        'darwin': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of\n"
                  "columns in the first matrix matches the number of rows in the second matrix. To\n"
                  "perform elementwise multiplication, use '.*'.\n",
    }


class OperatorError(SemanticException):
    message = {
        'win32': f"Operator placeholder is not supported for operands of type 'string'.",
        'darwin': f"Operator placeholder is not supported for operands of type 'string'.\n"
    }


class RecognitionError(SemanticException):
    message = {
        'win32': f"Unrecognized function or variable placeholder.",
        'darwin': f"Unrecognized function or variable placeholder.\n"
    }


class UnaryOperatorError(SemanticException):
    message = {
        'win32': f"Unary operator placeholder is not supported for operand of type 'string'.",
        'darwin': f"Unary operator placeholder is not supported for operand of type 'string'.\n"
    }
