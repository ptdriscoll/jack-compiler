# -*- coding: utf-8 -*- 

"""
This class is the second half of a syntactic analyzer (the tokenizer if the first half), 
which parses Jack programs according to the Jack grammar. The output is an XML formatted document. 
"""

import os, sys, ntpath, re

if os.getcwd().endswith('Compiler'):
    from compiler import tokenizer
    
else:
    import tokenizer
    

class CompilationEngine:
    """
    This module gets input from a tokenizer and writes a parsed XML structure 
    into an output file/stream. This is done by a series of compilexxx() methods, 
    where xxx is a corresponding syntactic element of the Jack grammar. 
    
    The contract between these methods is that each compilexxx() method should 
    read the syntactic construct xxx from the input, advance() the tokenizer exactly beyond xxx, 
    and output the XML parsing of xxx. Thus, compilexxx() may only be called if 
    xxx is the next syntactic element of the input.
    """
    
    def __init__(self, input_full_path, output_full_path, test=False):
        """
        creates a new compilation engine with the given input and output. 
        The next method called must be compileClass().
        """
        
        self._file_path = input_full_path  
        self._file_name = ntpath.basename(input_full_path)
        self._file_open = open(output_full_path, 'w') 
        self._tokenize = tokenizer.Tokenizer(input_full_path)
        self._tokenize.get_next_token()         
        self._IDENTIFIER_REGEX = re.compile('^[A-Za-z0-9_-][A-Za-z0-9_-]*$')
        
        self._dispatch_statement = {
            'let': self.compile_let,
            'if': self.compile_if,
            'while': self.compile_while,
            'do': self.compile_do,
            'return': self.compile_return 
        } 
                
        self._indent = 0
        self._tag_count = 0        
        self._xml = ''
        
        if not test:
            self.compile_class()
    
    def __str__(self):    
        to_print = '   Input file: ' + self._file_name + '\n'
        to_print += 'Current token: ' + self._tokenize.get_current_token(xml=True) + '\n'
        to_print += '    Tag count: ' + str(self._tag_count) + '\n' 
        return to_print
                
    def compile_class(self):
        """
        Compiles complete class.
        'class' className '{' classVarDec* subroutineDec* '}'        
        """
        
        self.tag('class')
        self._indent += 1
        
        self.eat('class')
        self.eat('className')
        self.eat('{')
        
        while self._tokenize.get_current_token() in ['static', 'field']:            
            self.compile_class_var_dec()
            
        while self._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile_subroutine()            
      
        self.eat('}')    
        
        self._indent -= 1
        self.tag('/class')

        #close writer
        self.close()       
        
    def compile_class_var_dec(self):
        """
        Compiles static declaration or field declaration. 
        ('static' | 'field' ) type varName (',' varName)* ';'         
        """
        
        self.tag('classVarDec')
        self._indent += 1 
        
        self.eat(['static', 'field'])
        self.eat(['int', 'char', 'boolean', 'className'])
        self.eat('varName')
        while(self._tokenize.get_current_token() == ','):
            self.eat(',')
            self.eat('varName')        
        self.eat(';')
       
        self._indent -= 1 
        self.tag('/classVarDec')        
    
    def compile_subroutine(self):
        """
        Compiles complete method, function or constructor.  
        ('constructor' | 'function' | 'method') ('void' | type) 
        subroutineName '(' parameterList ')' subroutineBody         
        """
        
        self.tag('subroutineDec') 
        self._indent += 1 
        
        self.eat(['constructor', 'function', 'method'])
        self.eat(['void', 'int', 'char', 'boolean', 'className'])
        self.eat('subroutineName')
        self.eat('(')
        self.compile_parameter_list()
        self.eat(')') 

        self.tag('subroutineBody') 
        self._indent += 1
        
        self.eat('{')
        while(self._tokenize.get_current_token() == 'var'):
            self.compile_var_dec()
        self.compile_statements()         
        self.eat('}')
        
        self._indent -= 1         
        self.tag('/subroutineBody')        
        
        self._indent -= 1 
        self.tag('/subroutineDec')        
    
    def compile_parameter_list(self):
        """
        Compiles (possibly empty) parameter list, not including enclosing "()".
        ((type varName) (',' type varName)*)?         
        """
        
        self.tag('parameterList')
        
        if self._tokenize.get_current_token() != ')':        
            self._indent += 1

            self.eat(['int', 'char', 'boolean', 'className'])
            self.eat('varName') 
            while(self._tokenize.get_current_token() == ','):
                self.eat(',')
                self.eat(['int', 'char', 'boolean', 'className'])
                self.eat('varName')        
            
            self._indent -= 1
        
        self.tag('/parameterList')

    def compile_var_dec(self):
        """
        Compiles var declaration.
        'var' type varName (',' varName)* ';'         
        """
        
        self.tag('varDec') 
        self._indent += 1
        
        self.eat('var')
        self.eat(['int', 'char', 'boolean', 'className'])        
        self.eat('varName') 
        while(self._tokenize.get_current_token() == ','):
            self.eat(',')      
            self.eat('varName') 
        self.eat(';')    
            
        self._indent -= 1
        self.tag('/varDec')        

    def compile_statements(self):
        """
        Compiles  sequence of statements, not including enclosing "{}".     
        """
        
        self.tag('statements') 
        
        while(self._tokenize.get_current_token() in ['let', 'if', 'while', 'do', 'return']):
            self._dispatch_statement[self._tokenize.get_current_token()]()  

        self.tag('/statements')

    def compile_subroutine_call(self):
        """
        Compiles subroutine call statement.  
        subroutineName '(' expressionList ')' | ( className | varName) 
                        '.' subroutineName '('expressionList ')'         
        """
        
        self.eat(['className', 'subroutineName', 'varName'])
        if self._tokenize.get_current_token() == '.':
            self.eat('.') 
            self.eat('subroutineName')            
        self.eat('(')
        self.compile_expression_list()
        self.eat(')')   
        
    def compile_do(self):
        """
        Compiles do statement.  
        DO: 'do' subroutineCall ';'  
        SUBROUTINECALL: subroutineName '(' expressionList ')' | ( className | varName) 
                        '.' subroutineName '('expressionList ')'         
        """
        
        self._indent += 1
        self.tag('doStatement') 
        self._indent += 1
        
        self.eat('do')
        self.compile_subroutine_call()
        self.eat(';') 
         
        self._indent -= 1
        self.tag('/doStatement')
        self._indent -= 1
        
    def compile_let(self):
        """
        Compiles let statement. 
        'let' varName ('[' expression ']')? '=' expression ';'         
        """

        self._indent += 1
        self.tag('letStatement') 
        self._indent += 1
        
        self.eat('let')
        self.eat('varName')
        while self._tokenize.get_current_token() == '[':
            self.eat('[')
            self.compile_expression()
            self.eat(']')            
        self.eat('=')  
        self.compile_expression()
        self.eat(';')        
        
        self._indent -= 1
        self.tag('/letStatement')
        self._indent -= 1        

    def compile_while(self):
        """
        Compiles while statement.   
        'while' '(' expression ')' '{' statements '}'         
        """
        
        self._indent += 1
        self.tag('whileStatement') 
        self._indent += 1
        
        self.eat('while')
        self.eat('(')
        self.compile_expression()
        self.eat(')')
        
        self.eat('{')
        self.compile_statements()
        self.eat('}')

        self._indent -= 1
        self.tag('/whileStatement') 
        self._indent -= 1        

    def compile_return(self):
        """
        Compiles return statement.
        'return' expression? ';'        
        """
        
        self._indent += 1
        self.tag('returnStatement') 
        self._indent += 1
        
        self.eat('return')
        if self._tokenize.get_current_token() != ';':
            self.compile_expression()
        self.eat(';')

        self._indent -= 1
        self.tag('/returnStatement')
        self._indent -= 1         

    def compile_if(self):
        """
        Compiles if statement, possibly with trailing else clause.
        'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?        
        """
        
        self._indent += 1
        self.tag('ifStatement') 
        self._indent += 1
        
        self.eat('if')
        self.eat('(')        
        self.compile_expression()
        self.eat(')')
        
        self.eat('{')
        self.compile_statements()
        self.eat('}')
        if self._tokenize.get_current_token() == 'else':
            self.eat('else')
            self.eat('{')
            self.compile_statements()
            self.eat('}')

        self._indent -= 1
        self.tag('/ifStatement')
        self._indent -= 1  

    def compile_expression(self):
        """
        Compiles expression. 
        term (op term)* 
        OP: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' 
        TERM: integerConstant | stringConstant | keywordConstant | varName | 
              varName '[' expression']' | subroutineCall | 
              '(' expression ')' | unaryOp term          
        """
        
        self.tag('expression')
        self._indent += 1  
            
        self.compile_term()
        
        if self._tokenize.get_current_token() in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            self.eat(['+', '-', '*', '/', '&', '|', '<', '>', '='])
            self.compile_term()
        
        self._indent -= 1        
        self.tag('/expression')        
        
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
        
        self.tag('term') 
        self._indent += 1
        
        if self._tokenize.get_current_token() == '(':
            self.eat('(')
            self.compile_expression()
            self.eat(')')
        
        elif self._tokenize.get_current_token() in ['-', '~']:
            self.eat(['-', '~'])
            self.compile_term()
            
        else:           
            cached_token, cached_index, cached_is_string, cached_state = self._tokenize.cache_current_token()             
            next_token = self._tokenize.get_next_token()            
            self._tokenize.reset_current_token(cached_token, cached_index, cached_is_string, cached_state)          
            
            if next_token in ['(', '.']:
                self.compile_subroutine_call()
                
            elif next_token == '[': 
                self.eat('varName')  
                self.eat('[')                    
                self.compile_expression()
                self.eat(']')
                
            else:                
                self.eat(['varName', 'integerConstant', 'stringConstant', 'true', 'false', 'null', 'this'])
            
        self._indent -= 1
        self.tag('/term')

    def compile_expression_list(self):
        """
        Compiles (possibly empty) comma separated list of expressions.
        (expression (',' expression)* )?         
        """
        
        self.tag('expressionList')
        self._indent += 1
        
        if (self._tokenize.get_token_type() in ['integerConstant', 'stringConstant', 'identifier']
            or self._tokenize.get_current_token() in ['true', 'false', 'null', 'this', '(', '-', '~']):
            
            self.compile_expression() 
            while(self._tokenize.get_current_token() == ','):
                self.eat(',')
                self.compile_expression()      
        
        self._indent -= 1
        self.tag('/expressionList')        
        
    def tag(self, type, token=None):
        """
        Writes xml tag.      
        """
        
        if token:
            xml = ('  ' * self._indent 
                    + '<' + type + '> ' 
                    + token 
                    + ' </' + type + '>\n') 
                    
        else:
            xml = '  ' * self._indent + '<' + type + '>\n'        

        self._tag_count += 1
        self._xml += xml
            
        self._file_open.write(xml)                    

    def eat(self, terminal):
        """
        Advances to next token and checks that it is what was expected.
        If all is good, calls xml tag writer.          
        """            

        token = self._tokenize.get_current_token()
        token_type = self._tokenize.get_token_type()
        
        #when a token is a keyword or symbol, it should match the terminal or a terminal option, input as a string or list 
        if token_type in ['keyword', 'symbol'] and token not in terminal:
            error = ('\nERROR 1: ' + token + ' != ' + str(terminal) + ' at tag ' + str(self._tag_count) 
                    + ' from file: ' + self._file_name)                
            self.print_error(error) 
        
        #when a token is an integer, then the terminal input should include 'integerConstant'        
        elif token_type == 'integerConstant' and 'integerConstant' not in terminal:
            error = ('\nERROR 2: ' + str(terminal) + ' does not include ' + token_type + ' at tag ' + str(self._tag_count)
                     + ' from file: ' + self._file_name) 
            self.print_error(error)  
        
        #when a token is a string, then the terminal input should include 'stringConstant' 
        elif token_type == 'stringConstant' and 'stringConstant' not in terminal:     
            error = ('\nERROR 3: ' + str(terminal) + ' does not include ' + token_type + ' at tag ' + str(self._tag_count)
                     + ' from file: ' + self._file_name) 
            self.print_error(error)           
        
        #when a token is an identifier, then the terminal or a terminal option, input as a string or list, 
        #should match an item in ['className', 'subroutineName', 'varName']
        elif token_type == 'identifier' and not any(x in terminal for x in ['className', 'subroutineName', 'varName']):     
            error = ('\nERROR 4: ' + str(terminal) + ' has no match in [\'className\', \'subroutineName\', \'varName\'] '
                     + 'at tag ' + str(self._tag_count) + ' from file: ' + self._file_name) 
            self.print_error(error) 
        
        #no errors, so get current token        
        else:
            token = self._tokenize.get_current_token(xml=True)                    
            self.tag(token_type, token)
        
        #advance to next token, if there is one       
        token = self._tokenize.get_next_token()

    def close(self):
        """
        Closes output file.
        """
        
        self._file_open.close()   

    def print_error(self, error):
        """
        Prints information for error and exits program.      
        """
        
        print('\n' + self._xml)
        sys.exit(error)        