import getopt
import sys
import re
#lexer
tokens = ('G', 'D',  'ID', 'E', 'S', 'C', 'COLOR', 'NUMBER')

#giros
t_G = r'x | \+ | \-' 

#desplazamientos
t_D = r'F | f | Z | z'

t_ID = r'[A-Z]'
t_E = r'\='
t_S = r'\['
t_C = r'\]'
t_COLOR = r'c'
t_NUMBER = r'\d+'
file = open('lsystem.txt', 'w')
step = 1
#tokens default
t_ignore = " \t"

def t_error (t):
    print ("Error lexico")
    t.lexer.skip(1)

def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")

import ply.lex as lex
lex.lex()

#parser
def p_raiz(p):
    'A : ID E COLOR W'
    file.write(str(p[1] + ' ' + p[2] + ' ' + p[3]) + p[4] + '\n')
    global step
    step = step + 1
    
def p_raiz1(p):
    'A : ID E W'
    file.write(str(p[1] + ' ' + p[2] + ' ' + p[3]) + '\n')
    global step
    step = step + 1
    
def p_raiz2(p):
    'A : N'
    global step
    if step <= 2:
        file.write(str(p[1]) + '\n')
        step = step + 1
    else:
        p_error(p)
    
def p_raiz3(p):
    'A : ID'
    file.write(str(p[1]) + '\n')
    global step
    step = step + 1
    
def p_raiz4(p):
    'A : ID W'
    file.write(str(p[1] + p[2]) + '\n')
    global step
    step = step + 1
    
def p_W(p):
    'W : S W C'
    p[0] = p[1] + p[2] + p[3]

def p_WSC(p):
    'W : S W C W'
    p[0] = p[1] + p[2] + p[3] + p[4]
    
def p_SW(p):
    ''' W : ID W
    | G W
    | D W '''
    p[0] = p[1] + p[2]
    
def p_ID(p):
    '''W : ID
    | D
    | G'''
    p[0] = p[1]
    
def p_number(p):
    'N : NUMBER'
    p[0] = p[1]
    
    
def p_error(p):
    print ("-.-")
    Joystick.sendToScreen("Error sintactico")

import ply.yacc as yacc
from PS4_Map import PS4Input
import lindenmayer

yacc.yacc()
Joystick = PS4Input()
done = False
file.write('Dimensions : 1920, 1080 \n')
file.write('Position : -300, -300 \n\n')

while done == False:
    
    
    try:
        if step == 1:
            file.write('Iterations : ')
            lsystem = Joystick.getline(step)
            temp = (int(lsystem)%30 + 5)
            lsystem = str(temp)
           
        elif step == 2:
            file.write("Angle : '")
            lsystem = Joystick.getline(step)
            temp = (int(lsystem)%360)
            lsystem = str(temp)
        elif step == 3:
            file.write('Linelength : 3 \n')
            file.write('Linewidth : 1 \n')
            file.write('Linecolor : #00ff00 \n')
            file.write('Background : #ffffff \n')
            file.write("Axiom : ")
            lsystem = Joystick.getline(step)
        elif step >= 4:
            lsystem = Joystick.getline(step)
            if lsystem == "":
                done = True
                print 'Linea' + lsystem
                Joystick.end()
        
    except EOFError:
        break
    if not lsystem:
        continue
    yacc.parse(lsystem)

file.close()

lindenmayer.main(sys.argv[1:])
    
    
