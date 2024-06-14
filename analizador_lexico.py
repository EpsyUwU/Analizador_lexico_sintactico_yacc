import ply.lex as lex

# Definición de palabras reservadas
reserved = {
    'public': 'PUBLIC',
    'class': 'CLASS',
    'main': 'MAIN',
    'System': 'SYSTEM',
    'out': 'OUT',
    'println': 'PRINTLN',
    'String': 'STRING',
    'args': 'ARGS',
    'static': 'STATIC',
    'void': 'VOID',
    'for': 'FOR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'number': 'NUMBER',
    'if': 'IF',
    'else': 'ELSE'
}

# Lista de tokens
tokens = [
    'ID', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 
    'STRING_LITERAL', 'SEMICOLON', 'DOT', 'ASSIGN', 'PLUS', 'MINUS', 'NUMBER',
    'LE', 'LT', 'GE', 'GT', 'EQ', 'NE'
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_LE = r'<='
t_LT = r'<'
t_GE = r'>='
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='

# Reglas para tokens con acciones adicionales
def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Eliminar las comillas del inicio y del final
    return t

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica las palabras reservadas
    return t

# Regla para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejar nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_SPACE(t):
    r'\s+'
    pass

# Regla para manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Función para tokenizar una cadena de código
def tokenize(code):
    """
    Tokeniza el código de entrada y devuelve una lista de tokens.
    """
    print("Código de entrada:", code)  # Imprime el código de entrada completo
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("Token encontrado:", tok)  # Imprime cada token encontrado
        tokens.append(tok)
    return tokens

# Construir el analizador léxico
lexer = lex.lex()
