# -*- coding: utf-8 -*- 

"""
This class is the second half of a syntactic analyzer (the tokenizer is the first half), which parses 
Jack programs according to the Jack grammar. The output, using vm_writer functions, is virtual machine code. 
"""

import os, sys, ntpath, re

if os.getcwd().endswith('Compiler'):
    from compiler import tokenizer
    from compiler import symbol_table
    from compiler import vm_writer as vm
    
else:
    import tokenizer
    import symbol_table
    import vm_writer as vm
    

class CompilationEngine:
    """
    This module gets input from a tokenizer and uses a vm_writer to write virtual machine code 
    into an output file/stream. This is done by a series of compilexxx() methods, where xxx 
    is a corresponding syntactic element of the Jack grammar.
    
    The contract between these methods is that each compilexxx() method should read the 
    syntactic construct xxx from the input, advance() the tokenizer exactly beyond xxx, 
    and use vm_writer to output the parsed structure into virtual machine commands. Thus, 
    compilexxx() may only be called if xxx is the next syntactic element of the input.
    """
   
    def __init__(self, input_full_path, output_full_path, test=False, test_class=''):
        """
        creates a new compilation engine with the given input and output. 
        The next method called must be compileClass().
        """
        
        self._file_path = input_full_path  
        self._file_name = ntpath.basename(input_full_path)
        self._file_open = open(output_full_path, 'w')
        self._test_class = test_class        
        
        self._tokenize = tokenizer.Tokenizer(input_full_path)
        self._tokenize.get_next_token()
        self._var_table = symbol_table.SymbolTable()
        self._class = ''
        self._if_count = 0
        self._while_count = 0
        
        self._dispatch_statement = {
            'let': self.compile_let,
            'if': self.compile_if,
            'while': self.compile_while,
            'do': self.compile_do,
            'return': self.compile_return 
        }        
       
        if not test:
            self.compile_class()
    
    def __str__(self):    
        to_print = '   Input file: ' + self._file_name + '\n'
        to_print += 'Current token: ' + self._tokenize.get_current_token(xml=True) + '\n'
        return to_print
        
    def get_print_var_table(self):
        """
        Returns printable variable symbol table for both class and subroutines scopes.
        """
        to_print = '============================='
        to_print += '\nClass Table\n-----------------------------\n'
        if self._var_table.get_class_table():
            to_print += 'NAME\t   KIND\t   TYPE\t   INDEX\n-----------------------------\n' 
            for key, value in self._var_table.get_class_table().items():
                to_print += key + '\t   ' + value['kind'] + '\t   ' + value['type'] + '\t   ' + str(value['index']) + '\n'
        else:
            to_print += 'No variables\n'            
    
        to_print += '\nSubroutine Table\n-----------------------------\n'   
        if self._var_table.get_subroutine_table():    
            to_print += 'NAME\t   KIND\t   TYPE\t   INDEX\n-----------------------------\n' 
            for key, value in self._var_table.get_subroutine_table().items():
                to_print += key + '\t   ' + value['kind'] + '\t   ' + value['type'] + '\t   ' + str(value['index']) + '\n'
        else:
            to_print += 'No variables\n'                    
 
        return to_print
        
    def get_var_attributes(self, var_name):
        """
        Returns kind, type and index of a variable if it exists in variable symbol table. 
        Otherwise returns None.
        """
    
        if self._var_table.exists(var_name):
            kind = self._var_table.kind_of(var_name)
            type = self._var_table.type_of(var_name)
            index = self._var_table.index_of(var_name)
            return kind, type, index
            
        return None      
                
    def compile_class(self):
        """
        Compiles complete class.
        'class' className '{' classVarDec* subroutineDec* '}'        
        """
        
        self.eat('class')
        self._class = self._tokenize.get_current_token()
        self.eat('className')
        self.eat('{')
        
        while self._tokenize.get_current_token() in ['static', 'field']:            
            self.compile_class_var_dec()
            
        while self._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile_subroutine()            
      
        self.eat('}')    

        #close writer
        self.close()       
        
    def compile_class_var_dec(self):
        """
        Compiles static declaration or field declaration. 
        ('static' | 'field' ) type varName (',' varName)* ';'         
        """
        
        kind = self._tokenize.get_current_token()
        self.eat(['static', 'field'])
        
        var_type = self._tokenize.get_current_token()
        self.eat(['int', 'char', 'boolean', 'className'])
        
        var_name = self._tokenize.get_current_token()
        self._var_table.define(var_name, var_type, kind)
        self.eat('varName')
        
        while(self._tokenize.get_current_token() == ','):
            self.eat(',')
            var_name = self._tokenize.get_current_token()
            self._var_table.define(var_name, var_type, kind)            
            self.eat('varName')        
        self.eat(';')     
    
    def compile_subroutine(self):
        """
        Compiles complete method, function or constructor.  
        ('constructor' | 'function' | 'method') ('void' | type) 
        subroutineName '(' parameterList ')' subroutineBody         
        """
        
        self._var_table.start_subroutine()
        self._if_count = 0
        self._while_count = 0
        is_method = False
        is_constructor = False
        
        if (self._tokenize.get_current_token() == 'method'): 
            is_method = True  
            self._var_table.define('this', self._class, 'argument') 
            
        elif (self._tokenize.get_current_token() == 'constructor'): 
            is_constructor = True  
            
        self.eat(['constructor', 'function', 'method'])      
        self.eat(['void', 'int', 'char', 'boolean', 'className'])
        
        func_name = self._tokenize.get_current_token()        
        self.eat('subroutineName')
        self.eat('(')
        self.compile_parameter_list()
        self.eat(')')
       
        self.eat('{')
        while(self._tokenize.get_current_token() == 'var'):
            self.compile_var_dec()
            
        num_vars = str(self._var_table.var_count('var'))
        code = vm.write_function(self._class, func_name, num_vars)
        
        if is_method:      
            code += vm.write_push('argument', '0')
            code += vm.write_pop('pointer', '0')
            
        elif is_constructor:
            num_args = str(self._var_table.var_count('field'))
            code += vm.write_push('constant', num_args)            
            code += vm.write_call('Memory', 'alloc', '1')
            code += vm.write_pop('pointer', '0')
            
        self.write(code)             
            
        self.compile_statements()         
        self.eat('}')
       
        if self._class == self._test_class:
            print(self.get_print_var_table())
    
    def compile_parameter_list(self):
        """
        Compiles (possibly empty) parameter list, not including enclosing "()".
        ((type varName) (',' type varName)*)?         
        """
       
        if self._tokenize.get_current_token() != ')':        
            
            var_type = self._tokenize.get_current_token()
            self.eat(['int', 'char', 'boolean', 'className'])
            
            arg_name = self._tokenize.get_current_token()
            self.eat('varName')
            
            self._var_table.define(arg_name, var_type, 'argument')
            
            while(self._tokenize.get_current_token() == ','):
                self.eat(',')
                
                var_type = self._tokenize.get_current_token()
                self.eat(['int', 'char', 'boolean', 'className'])
                
                arg_name = self._tokenize.get_current_token()
                self.eat('varName') 
                
                self._var_table.define(arg_name, var_type, 'argument')                

    def compile_var_dec(self):
        """
        Compiles var declaration.
        'var' type varName (',' varName)* ';'         
        """
        
        self.eat('var')
        
        var_type = self._tokenize.get_current_token()
        self.eat(['int', 'char', 'boolean', 'className'])   
        
        var_name = self._tokenize.get_current_token()
        self._var_table.define(var_name, var_type, 'var')
        self.eat('varName') 
        
        while(self._tokenize.get_current_token() == ','):
            self.eat(',') 
            var_name = self._tokenize.get_current_token()
            self._var_table.define(var_name, var_type, 'var')            
            self.eat('varName') 
        self.eat(';')     

    def compile_statements(self):
        """
        Compiles  sequence of statements, not including enclosing "{}".     
        """
       
        while(self._tokenize.get_current_token() in ['let', 'if', 'while', 'do', 'return']):
            self._dispatch_statement[self._tokenize.get_current_token()]()  

    def compile_subroutine_call(self):
        """
        Compiles subroutine call statement.  
        subroutineName '(' expressionList ')' | ( className | varName) 
                        '.' subroutineName '('expressionList ')' 
        
        If name doesn't include a '.' symbol, it is a local method call:
            - push pointer 0, push args, call (num args + this)
            
        If there is a '.' and the left side is a variable, it's an object method:
            - push variable as first argument, push other args, call (num args + this)
            
        If there is a '.' and the left side isn't a variable, it's a function or constructor call
            - push args, call (num args)                        
        """

        class_name = self._class
        num_args = 0
        
        func_name = self._tokenize.get_current_token()
        self.eat(['className', 'subroutineName', 'varName'])
        
        if self._tokenize.get_current_token() == '.':
            class_name = func_name
            
            #is an object method
            if self._var_table.exists(class_name):
                num_args += 1            
                kind = self._var_table.kind_of(class_name, vm=True)
                index = self._var_table.index_of(class_name)
                class_name = self._var_table.type_of(class_name)
                code = vm.write_push(kind, str(index))
                self.write(code)                 
        
            self.eat('.')            
            func_name = self._tokenize.get_current_token()
            self.eat('subroutineName')
        
        #is a local method        
        else:
            num_args += 1
            code = vm.write_push('pointer', '0')
            self.write(code)     
            
        self.eat('(')
        num_args += self.compile_expression_list()
        self.eat(')') 
        
        code = vm.write_call(class_name, func_name, str(num_args))
        self.write(code)        
        
    def compile_do(self):
        """
        Compiles do statement.  
        DO: 'do' subroutineCall ';'  
        SUBROUTINECALL: subroutineName '(' expressionList ')' | ( className | varName) 
                        '.' subroutineName '('expressionList ')'         
        """
        
        self.eat('do')
        self.compile_subroutine_call()
        self.eat(';')
        
        code = vm.write_pop('temp', '0')
        self.write(code)
        
    def compile_let(self):
        """
        Compiles let statement. 
        'let' varName ('[' expression ']')? '=' expression ';'         
        """
        is_array = False
        
        self.eat('let')
        var_name = self._tokenize.get_current_token()
        kind = self._var_table.kind_of(var_name, vm=True)
        index = self._var_table.index_of(var_name)        
        self.eat('varName')
        
        while self._tokenize.get_current_token() == '[':
            is_array = True
            self.eat('[')
            self.compile_expression()
            self.eat(']') 
            
            code = vm.write_push(kind, str(index))
            code += vm.write_arithmetic('+')
            self.write(code)
            
        self.eat('=')  
        self.compile_expression()
        self.eat(';')   
        
        if is_array:    
            code = vm.write_pop('temp', '0')        
            code += vm.write_pop('pointer', '1')
            code += vm.write_push('temp', '0')     
            code += vm.write_pop('that', '0')       

        else:
            code = vm.write_pop(kind, str(index))
        
        self.write(code)        

    def compile_while(self):
        """
        Compiles while statement.   
        While condition is reset as not (~), as shown on page 233 in the book (2008 paperback).
        'while' '(' expression ')' '{' statements '}'   
        """
        
        while_count = str(self._while_count)
        self._while_count += 1     
        
        code = vm.write_label('WHILE_EXP' + while_count)
        self.write(code)
        
        self.eat('while')
        self.eat('(')
        self.compile_expression()
        self.eat(')')
        
        code = vm.write_arithmetic('~')
        code += vm.write_if('WHILE_END' + while_count)
        self.write(code)
        
        self.eat('{')
        self.compile_statements()
        self.eat('}')
        
        code = vm.write_goto('WHILE_EXP' + while_count)
        code += vm.write_label('WHILE_END' + while_count)
        self.write(code)

    def compile_return(self):
        """
        Compiles return statement.
        'return' expression? ';'        
        """
        
        self.eat('return')
        
        if self._tokenize.get_current_token() != ';':
            self.compile_expression()
            
        else:
            code = vm.write_push('constant', '0')
            self.write(code)    
            
        self.eat(';')
        
        code = vm.write_return()
        self.write(code)
        
    def compile_if(self):
        """
        Compiles if statement, possibly with trailing else clause.
        The if condition is NOT reset as not (~), as was shown on page 233 in the book (2008 paperback), 
        instead a typical condition is used to match, and make testing compatible, with the course's 
        supplied JackCompiler (v 2.5). 
        'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?        
        """
        
        if_count = str(self._if_count)
        self._if_count += 1
        
        self.eat('if')
        self.eat('(')        
        self.compile_expression()
        self.eat(')')        
        
        code = vm.write_if('IF_TRUE' + if_count)
        code += vm.write_goto('IF_FALSE' + if_count)
        code += vm.write_label('IF_TRUE' + if_count)
        self.write(code)
        
        self.eat('{')
        self.compile_statements()
        self.eat('}')
    
        if self._tokenize.get_current_token() == 'else':
            code = vm.write_goto('IF_END' + if_count)
            code += vm.write_label('IF_FALSE' + if_count)
            self.write(code)
            
            self.eat('else')
            self.eat('{')
            self.compile_statements()
            self.eat('}')        
        
            code = vm.write_label('IF_END' + if_count) 
            self.write(code)

        else:
            code = vm.write_label('IF_FALSE' + if_count)
            self.write(code)        

    def compile_expression(self):
        """
        Compiles expression. 
        term (op term)* 
        OP: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' 
        TERM: integerConstant | stringConstant | keywordConstant | varName | 
              varName '[' expression']' | subroutineCall | 
              '(' expression ')' | unaryOp term          
        """
            
        self.compile_term()
        
        if self._tokenize.get_current_token() in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            op = self._tokenize.get_current_token()
            self.eat(['+', '-', '*', '/', '&', '|', '<', '>', '='])
            self.compile_term() 
            
            code = vm.write_arithmetic(op)  
            self.write(code)                        
        
    def compile_term(self):
        """
        Compiles term. This method is faced with a slight difficulty when trying to 
        decide between some of the alternative rules. Specifically, if the 
        current token is an identifier, it must still distinguish between a variable, 
        an array entry, and a subroutine call. 
        
        The distinction can be made by looking ahead one extra token. A single 
        look-ahead token, which may be one of "[", "(", ".", suffices to distinguish 
        between the three possibilities. Any other token is not part of this term 
        and should not be advanced over.

        integerConstant | stringConstant | keywordConstant | varName | 
        varName '[' expression']' | subroutineCall | 
        '(' expression ')' | unaryOp term          
        """
        
        #this is a parentheses with an expression 
        if self._tokenize.get_current_token() == '(':
            self.eat('(')
            self.compile_expression()
            self.eat(')')
        
        #this is a unaryOp followed by a term
        elif self._tokenize.get_current_token() in ['-', '~']:
            unary_op = self._tokenize.get_current_token()
            self.eat(['-', '~'])
            self.compile_term()
            code = vm.write_arithmetic(unary_op, unary=True)
            self.write(code)       
            
        else:           
            cached_token, cached_index, cached_is_string, cached_state = self._tokenize.cache_current_token()             
            next_token = self._tokenize.get_next_token()            
            self._tokenize.reset_current_token(cached_token, cached_index, cached_is_string, cached_state)    
            
            #this is a subroutine call
            if next_token in ['(', '.']:
                self.compile_subroutine_call()
            
            #this is an array entry
            elif next_token == '[': 
                token = self._tokenize.get_current_token()
                kind = self._var_table.kind_of(token, vm=True)
                index = self._var_table.index_of(token)  
                
                self.eat('varName')  
                self.eat('[')                    
                self.compile_expression()
                self.eat(']')                

                code = vm.write_push(kind, str(index))
                code += vm.write_arithmetic('+')
                code += vm.write_pop('pointer', '1')
                code += vm.write_push('that', '0')            
                self.write(code)                
            
            #this is a variable or a constant              
            else:       
                token = self._tokenize.get_current_token()
                token_type = self._tokenize.get_token_type()
                
                if token_type == 'identifier':
                    kind = self._var_table.kind_of(token, vm=True)
                    index = self._var_table.index_of(token)
                    code = vm.write_push(kind, str(index))
                    
                elif token_type == 'integerConstant':
                    code = vm.write_push('constant', token)
                
                elif token_type == 'stringConstant':
                    code = vm.write_string(token) 

                elif token in ['true', 'false', 'null', 'this']:
                    code = vm.write_term(token)
               
                self.write(code) 
                self.eat(['varName', 'integerConstant', 'stringConstant', 'true', 'false', 'null', 'this'])

    def compile_expression_list(self):
        """
        Compiles (possibly empty) comma separated list of expressions.
        (expression (',' expression)* )?         
        """
        
        num_args = 0
        
        if (self._tokenize.get_token_type() in ['integerConstant', 'stringConstant', 'identifier']
            or self._tokenize.get_current_token() in ['true', 'false', 'null', 'this', '(', '-', '~']):
            
            self.compile_expression()
            num_args += 1            
            
            while(self._tokenize.get_current_token() == ','):
                self.eat(',')
                self.compile_expression()
                num_args += 1
                
        return num_args

    def eat(self, terminal):
        """
        Advances to next token and checks that it is what was expected.        
        """            

        token = self._tokenize.get_current_token()
        token_type = self._tokenize.get_token_type()
        
        #when a token is a keyword or symbol, it should match the terminal or a terminal option, input as a string or list 
        if token_type in ['keyword', 'symbol'] and token not in terminal:
            error = ('\nERROR 1: token ' + token + ' != terminal ' + str(terminal) 
                    + ' from file: ' + self._file_name)                
            self.print_error(error) 
        
        #when a token is an integer, then the terminal input should include 'integerConstant'        
        elif token_type == 'integerConstant' and 'integerConstant' not in terminal:
            error = ('\nERROR 2: terminal ' + str(terminal) + ' does not include token type ' + token_type
                     + ' from file: ' + self._file_name) 
            self.print_error(error)  
        
        #when a token is a string, then the terminal input should include 'stringConstant' 
        elif token_type == 'stringConstant' and 'stringConstant' not in terminal:     
            error = ('\nERROR 3: terminal ' + str(terminal) + ' does not include token type ' + token_type
                     + ' from file: ' + self._file_name) 
            self.print_error(error)           
        
        #when a token is an identifier, then the terminal or a terminal option, input as a string or list, 
        #should match an item in ['className', 'subroutineName', 'varName']
        elif token_type == 'identifier' and not any(x in terminal for x in ['className', 'subroutineName', 'varName']):     
            error = ('\nERROR 4: terminal ' + str(terminal) + ' has no match in [\'className\', \'subroutineName\', \'varName\'] '
                     + ' from file: ' + self._file_name) 
            self.print_error(error)
       
        #no errors, so advance to next token, if there is one       
        token = self._tokenize.get_next_token()
        
    def write(self, code):
        """
        Writes to file.
        """
        
        self._file_open.write(code)         

    def close(self):
        """
        Closes output file.
        """

        self._file_open.close()        

    def print_error(self, error):
        """
        Prints information for error and exits program.      
        """
        
        sys.exit(error)           