
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARGS CLASS DOT ID LBRACE LBRACKET LPAREN MAIN OUT PRINTLN PUBLIC QUOTE RBRACE RBRACKET RPAREN SEMICOLON STATIC STRING STRING_LITERAL SYSTEM VOIDprogram : PUBLIC CLASS ID LBRACE class_body RBRACEclass_body : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statement RBRACEstatement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING_LITERAL RPAREN SEMICOLON\n                 | SYSTEM DOT OUT DOT PRINTLN LPAREN ID RPAREN SEMICOLON'
    
_lr_action_items = {'PUBLIC':([0,5,],[2,6,]),'$end':([1,9,],[0,-1,]),'CLASS':([2,],[3,]),'ID':([3,26,],[4,28,]),'LBRACE':([4,17,],[5,18,]),'STATIC':([6,],[8,]),'RBRACE':([7,19,21,31,32,],[9,21,-2,-3,-4,]),'VOID':([8,],[10,]),'MAIN':([10,],[11,]),'LPAREN':([11,25,],[12,26,]),'STRING':([12,],[13,]),'LBRACKET':([13,],[14,]),'RBRACKET':([14,],[15,]),'ARGS':([15,],[16,]),'RPAREN':([16,27,28,],[17,29,30,]),'SYSTEM':([18,],[20,]),'DOT':([20,23,],[22,24,]),'OUT':([22,],[23,]),'PRINTLN':([24,],[25,]),'STRING_LITERAL':([26,],[27,]),'SEMICOLON':([29,30,],[31,32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_body':([5,],[7,]),'statement':([18,],[19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PUBLIC CLASS ID LBRACE class_body RBRACE','program',6,'p_program','analizador_sintactico.py',10),
  ('class_body -> PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statement RBRACE','class_body',13,'p_class_body','analizador_sintactico.py',13),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN STRING_LITERAL RPAREN SEMICOLON','statement',9,'p_statement','analizador_sintactico.py',16),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN ID RPAREN SEMICOLON','statement',9,'p_statement','analizador_sintactico.py',17),
]