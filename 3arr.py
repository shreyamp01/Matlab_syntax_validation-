#FINAL Construct 
import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = [
    'ID',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMICOLON',
    'NUMBERS',
]

# Regular expressions for tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_NUMBERS = r'\d+'
t_ignore = ' \t'  # Ignore spaces and tabs

# Parsing rules
def p_array_declaration(p):
    '''
    array_declaration : ID EQUALS LBRACKET array_elements RBRACKET
    '''
    p[0] = "Valid Array Declaration: " + p[1]

def p_array_elements(p):
    '''
    array_elements : array_element
                  | array_elements array_element
    '''
    pass

def p_array_element(p):
    '''
    array_element : NUMBERS
                  | NUMBERS COMMA
                  | NUMBERS SEMICOLON
    '''
    pass

def p_error(p):
    pass

lexer = lex.lex()
parser = yacc.yacc()

def validate_array_declaration(declaration):
    try:
        result = parser.parse(declaration, lexer=lexer)
        return result
    except Exception as e:
        return "Invalid Array Declaration"

if __name__ == "__main__":
    while True:
        declaration = input("Enter a MATLAB array declaration (or 'exit' to quit): ")
        if declaration.lower() == 'exit':
            break

        result = validate_array_declaration(declaration)
        print(result)
