#FINAL 
import ply.lex as lex
import ply.yacc as yacc

# Define the lexer (tokenizer)
tokens = (
    'ID',
    'ASSIGN',
    'STRING',
    'SEMICOLON',
)

t_ASSIGN = r'='
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

def t_STRING(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the parser rules for MATLAB string declarations
def p_string_declaration(p):
    '''string_declaration : ID ASSIGN STRING SEMICOLON'''
    p[0] = (p[1], p[3])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

while True:
    # Read user input
    input_string = input("Enter a MATLAB string declaration (or type 'exit' to quit): ")

    if input_string.lower() == 'exit':
        break

    # Parsing the user input
    try:
        result = parser.parse(input_string)
        if result:
            print(f"Valid string declaration: {result[0]} = '{result[1]}'")
        else:
            print("Invalid string declaration")
    except SyntaxError:
        print("Invalid string declaration")
