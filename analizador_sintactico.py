import ply.yacc as yacc
from analizador_lexico import tokens


# Definimos la precedencia y asociación de los operadores
precedence = ()

# Definimos la gramática
def p_program(p):
    '''program : PUBLIC CLASS ID LBRACE class_body RBRACE'''

def p_class_body(p):
    '''class_body : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statement RBRACE'''

def p_statement(p):
    '''statement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING_LITERAL RPAREN SEMICOLON
                 | SYSTEM DOT OUT DOT PRINTLN LPAREN ID RPAREN SEMICOLON'''

parse_error_message = None

def p_error(p):
    global parse_error_message 
    if p:
        parse_error_message = f"Syntax error at token {p.type} - {p.value}, line {p.lineno}"
    else:
        parse_error_message = "Syntax error at EOF"
        


parser = yacc.yacc()

