# app.py
from flask import Flask, request, render_template
import analizador_lexico
import analizador_sintactico

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', results=None, syntax_valid=None, counts=None, code='')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    tokens = analizador_lexico.tokenize(code)
    syntax_valid = True
    error_message = "correcto"
    results = []

    token_categories = {
        "reserved": set(analizador_lexico.reserved.values()),
        "identifier": {"ID"},
        "number": {"NUMBER"},
        "symbol": {"SEMICOLON", "DOT"},
        "paren_left": {"LPAREN"},
        "paren_right": {"RPAREN"},
        "brace_left": {"LBRACE"},
        "brace_right": {"RBRACE"}
    }

    counts = {key: 0 for key in token_categories.keys()}
    counts["total"] = 0

    analizador_sintactico.parser.parse(code)


    if analizador_sintactico.parse_error_message:
        error_message = analizador_sintactico.parse_error_message  
    else:
        print("Syntax is valid")
        error_message = None
    
    for token in tokens:
        token_type = token.type
        token_value = token.value

        is_reserved = token_type in token_categories["reserved"]
        is_identifier = token_type in token_categories["identifier"]
        is_number = token_type in token_categories["number"]
        is_symbol = token_type in token_categories["symbol"]
        is_paren_left = token_type in token_categories["paren_left"]
        is_paren_right = token_type in token_categories["paren_right"]
        is_brace_left = token_type in token_categories["brace_left"]
        is_brace_right = token_type in token_categories["brace_right"]

        results.append({
            "token": token_value,
            "reserved": 'X' if is_reserved else '',
            "identifier": 'X' if is_identifier else '',
            "number": 'X' if is_number else '',
            "symbol": 'X' if is_symbol else '',
            "paren_left": 'X' if is_paren_left else '',
            "paren_right": 'X' if is_paren_right else '',
            "brace_left": 'X' if is_brace_left else '',
            "brace_right": 'X' if is_brace_right else ''
        })

        if is_reserved:
            counts["reserved"] += 1
        if is_identifier:
            counts["identifier"] += 1
        if is_number:
            counts["number"] += 1
        if is_symbol:
            counts["symbol"] += 1
        if is_paren_left:
            counts["paren_left"] += 1
        if is_paren_right:
            counts["paren_right"] += 1
        if is_brace_left:
            counts["brace_left"] += 1
        if is_brace_right:
            counts["brace_right"] += 1
        
        counts["total"] += 1

    return render_template('index.html', results=results, syntax_valid=syntax_valid, counts=counts, code=code, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)