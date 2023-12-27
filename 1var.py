# FINAL 
import ply.lex as lex
import ply.yacc as yacc

# Define the lexer (tokenizer)
tokens = (
    'ID',
    'ASSIGN',
    'NUMBER',
    'SEMICOLON',
)

t_ASSIGN = r'='
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the parser rules for MATLAB variable declarations
def p_statement(p):
    '''statement : ID ASSIGN expression SEMICOLON'''
    p[0] = (p[1], p[3])

def p_expression(p):
    '''expression : NUMBER
                  | ID'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    # Read user input
    input_string = input("Enter a MATLAB variable declaration (or type 'exit' to quit): ")

    if input_string.lower() == 'exit':
        break

    # Parsing the user input
    lexer.input(input_string)
    valid_declaration = None

    for tok in lexer:
        try:
            result = parser.parse(input_string)
            valid_declaration = result if result else valid_declaration
        except SyntaxError:
            pass

    if valid_declaration:
        print(f"Valid variable declaration: {valid_declaration[0]} = {valid_declaration[1]}")
    else:
        print("Invalid variable declaration")
