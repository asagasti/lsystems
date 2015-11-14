#lexer
tokens = ('G', 'D' 'id', 'e', 'a', 'c')

#giros
t_G = r'x | \+ | \-' 

#desplazamientos
t_D = r'F | f | Z | z'

t_id = #Que va aqui
t_e = r'\='
t_a = r'\['
t_c = r'\]'

#tokens default
t_ignore = " \t"

def t_error (t):
    print ("Error léxico")
    t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")

import ply.lex as lex
lex.lex()

#parser
def p_raiz(p):
	''' A : id e W'''

def p_W(p):
	''' W : a W c 
	| id W 
	| id 
	| G W 
	| D W'''	
	
	
def p_error(p):
    print (">.>")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        lsystem = input("lsystem>")
    except EOFError:
        break
    if not lsystem:
        continue
    yacc.parse(lsystem)

    
    