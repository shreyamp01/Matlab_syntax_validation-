#final construct 
import ply.lex as lex
import ply.yacc as yacc

# Define reserved keywords
reserved = {
    'function': 'FUNCTION',
    'end': 'END',
}

# List of token names
tokens = [
    'LPAREN',
    'RPAREN',
    'ID',
    'EQUALS',
    'COMMA',
    'LSQUARE',
    'RSQUARE',
] + list(reserved.values())

# Token definitions
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_COMMA = r','
t_LSQUARE = r'\['
t_RSQUARE = r'\]'

# Define a rule for IDs
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Ignore whitespace
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Parsing rules
def p_function_declaration(p):
    '''
    function_declaration : FUNCTION output  EQUALS ID parameter_list END
                       | FUNCTION  ID LSQUARE output RSQUARE  EQUALS ID parameter_list END
                       | FUNCTION ID LSQUARE RSQUARE EQUALS ID parameter_list END
    '''
    p[0] = f"Valid function declaration: {p[3]}"

def p_output(p):
    '''
    output : ID
    | ID COMMA output
    '''
    pass

def p_parameter_list(p):
    '''
    parameter_list : LPAREN parameters RPAREN
    | LPAREN RPAREN
    '''
    pass

def p_parameters(p):
    '''
    parameters : ID
               | ID COMMA parameters
    '''
    pass

def p_error(p):
    print("Syntax error")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        declaration = input("Enter a MATLAB-like function declaration (or 'exit' to quit): ")
        if declaration.lower() == 'exit':
            break

        result = parser.parse(declaration)
        if result:
            print(result)
        else:
            print("Invalid function declaration. Please enter a valid one.")
