import ply.yacc as yacc
from analizador_lexico import tokens

# Definimos la precedencia y asociación de los operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE')
)

# Definimos la gramática
def p_program(p):
    '''program : PUBLIC CLASS ID LBRACE class_body RBRACE 
               | for_statement'''

def p_class_body(p):
    '''class_body : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statement_list RBRACE'''

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''

def p_statement(p):
    '''statement : SYSTEM DOT OUT DOT PRINTLN LPAREN expression RPAREN SEMICOLON
                 | declaration SEMICOLON
                 | for_statement'''

def p_for_statement(p):
    '''for_statement : INT ID SEMICOLON FOR LPAREN for_init SEMICOLON expression SEMICOLON for_update RPAREN LBRACE statement_list RBRACE'''

def p_for_init(p):
    '''for_init : declaration
                | expression
                | empty'''

def p_for_update(p):
    '''for_update : ID PLUS PLUS
                  | ID MINUS MINUS'''

def p_declaration(p):
    '''declaration : ID ASSIGN expression 
                   | type_specifier ID'''

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR'''

def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | ID ASSIGN expression 
                  | expression PLUS expression
                  | expression PLUS PLUS expression
                  | expression MINUS expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | STRING_LITERAL'''

def p_empty(p):
    'empty :'
    pass

# Manejo de errores
parse_error_message = None

def p_error(p):
    global parse_error_message 
    if p:
        parse_error_message = f"Syntax error at token {p.type} - {p.value}, line {p.lineno}"
    else:
        parse_error_message = "Syntax error at EOF"

parser = yacc.yacc()

def reset_parse_error():
    global parse_error_message
    parse_error_message = None
