# -*- coding: utf-8 -*- 

"""
Functions and data maps that produce virtual machine commands.  
"""

#Maps a VM op command. 
ops = {'+': 'add\n', 
       '-': 'sub\n', 
       '*': 'call Math.multiply 2\n', 
       '/': 'call Math.divide 2\n', 
       '&': 'and\n', 
       '|': 'or\n', 
       '<': 'lt\n', 
       '>': 'gt\n', 
       '=': 'eq\n',
       '~': 'not\n',    
       'neg': 'neg\n'}

#Maps a VM unary op command. 
unary_ops = {'~': 'not\n', '-': 'neg\n'}

#maps spefic terms to simple VM commands
#true is NOT mapped to push constant 1 followed by a neg (-1) as described 
#on page 233 in the book (2008 paperback). It is instead mapped to 
#push contant 0 followed by a not (~0). This matches, and make testing compatible, 
#with the course's supplied JackCompiler (v 2.5). 
terms = {'true': 'push constant 0\nnot\n', 
         'false': 'push constant 0\n', 
         'null': 'push constant 0\n', 
         'this': 'push pointer 0\n'}
   
def write_push(segment, index):
    """
    Writes a VM push command.
    Accepts a segment:
        - constant
        - argument
        - local
        - static
        - this
        - that 
        - pointer
        - temp
    Also accepts an index as an integer.         
    """
    
    code = 'push ' + segment + ' ' + index + '\n'
    return code
    
def write_pop(segment, index):
    """
    Writes a VM pop command. 
    Accepts a segment:
        - constant
        - argument
        - local
        - static
        - this
        - that 
        - pointer
        - temp
    Also accepts and index as an integer.          
    """
    
    code = 'pop ' + segment + ' ' + index + '\n'
    return code
    
def write_arithmetic(command, unary=False):
    """
    Writes a VM arithmetic command. 
    Accepts an op command: +, -, *, /, &, |, <, >, = 
    Or an unary op command: -, ~  
    """
    
    if unary:
        code = unary_ops[command]
        
    else:
        code = ops[command]
        
    return code    
    
def write_term(command):
    """
    Writes simple terms: true, false, null, this 
    """    
      
    code = terms[command]
    return code    

def write_string(string):
    """
    Writes String constant using the OS constructor String.new(length) 
    and the OS method String.appendChar(nextChar).  
    """    

    code = 'push constant ' + str(len(string)) + '\n'
    code += 'call String.new 1\n'
    
    for char in string:
        code += 'push constant ' + str(ord(char)) + '\n'
        code += 'call String.appendChar 2\n'
      
    return code      

def write_label(label):
    """
    Writes a VM label command. Accepts label.
    """
    
    code = 'label ' + label + '\n'
    return code

def write_goto(label):
    """
    Writes a VM goto command. Accepts label.  
    """
    
    code = 'goto ' + label + '\n'
    return code

def write_if(label):
    """
    Writes a VM If-goto command. Accepts label.
    """
    
    code = 'if-goto ' + label + '\n'
    return code

def write_call(class_name, func_name, num_args):
    """
    Writes a VM call command. Accepts class name, function name and number of arguments.
    """
    
    code = 'call ' +  class_name + '.' + func_name + ' ' + num_args + '\n'
    return code

def write_function(class_name, func_name, num_args):
    """
    Writes a VM function command. Accepts name and number of local variables.
    """
    
    code = 'function ' +  class_name + '.' + func_name + ' ' + num_args + '\n'
    return code

def write_return():
    """
    Writes a VM return command. 
    """
    
    code = 'return\n'
    return code