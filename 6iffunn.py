import ply.yacc as yacc
import ply.lex as lex

# Define reserved words
reserved = {
    'if': 'IF',
    'disp': 'DISP',
    'end': 'END',
}

# Define the tokens
tokens = [
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'ASSIGN',
    'NUMBER',
    'STRING',
    'LT',
    'SEMICOLON',
    'GT',
    'PIPE',
    'AMPERSAND',
] + list(reserved.values())

# Token definitions
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_STRING = r'\"[A-Za-z\d\s\$\/\\!@#%\^&\*\(\)\-_\+=\{\}|\']+\"'
t_LT = r'<'
t_GT = r'>'
t_PIPE = r'\|'
t_AMPERSAND = r'&'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

t_NUMBER = r'\d+'

# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Parsing rules for the "if" condition
def p_statement_if(p):
    'statement : IF condition END'
    p[0] = f'if {p[2]} \nend'

def p_condition(p):
    '''condition : expression LT expression
                | expression GT expression
                | expression ASSIGN expression
                | expression PIPE expression
                | expression AMPERSAND expression'''
    p[0] = f'{p[1]} {p[2]} {p[3]}'

def p_expression(p):
    '''expression : IDENTIFIER
                | NUMBER
                | STRING'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input('Enter an "if" condition (or type "exit" to quit): ')
    except EOFError:
        break

    if not s:
        continue

    if s.lower() == 'exit':
        break

    result = parser.parse(s)
    if result:
        print("Valid input")
        print("Generated code:\n")
        print(result)
    else:
        print("Invalid input. Please enter a valid 'if' condition.")
