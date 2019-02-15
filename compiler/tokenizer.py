# -*- coding: utf-8 -*- 

"""
This class, when applied to a text file containing Jack code, produces a list of tokens:
    - symbol
    - keyword
    - identifier
    - integer constant
    - string constant 
Each is printed in a separate line, with its classification recorded using XML tags.
"""

import os, re

if os.getcwd().endswith('Compiler'):
    from compiler import lexical_elements
    
else:
    import lexical_elements
    

class Tokenizer:
    """
    The tokenizer removes all comments and white space from the input stream 
    and breaks it into tokens, as specified in the Jack grammar.
    """
    
    def __init__(self, full_path):
        """
        Opens the input file/stream and gets ready to tokenize it.
        """
        
        self._file_path = full_path
        with open(full_path) as f:
            self._content = f.read()  
        self._cursor_index = 0    
        self._current_token = '' 
        self._current_token_is_string = False
        self._state = 'code' #can be 'code', 'block comment', 'inline comment' or 'string' 
        self._IDENTIFIER_REGEX = re.compile('^[A-Za-z0-9_-][A-Za-z0-9_-]*$')        
    
    def __str__(self):    
        to_print = '      File path: ' + self._file_path + '\n'
        to_print += '   Cursor index: ' + str(self._cursor_index) + '\n'
        to_print += '  Current token: ' + self._current_token + '\n'
        to_print += 'Token is string: ' + str(self._current_token_is_string) + '\n'
        to_print += '          State: ' + self._state + '\n'
        #to_print += '         File: \n' + self._content + '\n'
        return to_print
        
    def has_more_to_process(self):
        """
        Do we have more to process from input? Returns boolean. 
        """  

        return self._cursor_index < len(self._content)        

    def advance(self):
        """
        Gets next token, if there is one, from input and makes it current token. Should only be called if 
        has_more_to_process() is true. Initially there is no current token.
        """
        
        self._current_token = ''
        self._current_token_is_string = False
        char = ''
        next_char = ''               
        getting_token = True        
        
        while(getting_token and self.has_more_to_process()):   
            char = self._content[self._cursor_index]
            
            if self._state == 'block comment':
                if self._cursor_index + 1 < len(self._content):
                    next_char = self._content[self._cursor_index + 1]
                    
                if char == '*' and next_char == '/':
                    self._state = 'code'
                    self._cursor_index += 1 #advance to next_char
                
            elif self._state == 'inline comment':
                if char == '\n':
                    self._state = 'code'
                
            elif self._state == 'string':
                if char == '"':
                    self._current_token_is_string = True
                    self._state = 'code'
                    getting_token = False
                    
                else:
                    self._current_token += char                
            
            #handles 'code' state            
            else:   

                #a space or newline ends a token - but ignore if no token stored yet in self._current_token
                if char in [' ', '\n', '\t']:
                    if len(self._current_token) > 0:  
                        getting_token = False
                
                #a symbol ends a token - but is the token itself if no token stored yet in self._current_token
                elif char in lexical_elements.symbols: 

                    #get next character to see if '/' instead starts a comment                
                    if self._cursor_index + 1 < len(self._content):
                        next_char = self._content[self._cursor_index + 1]   
                    
                    if char == '/' and next_char in ['*', '/']: 
                        self._cursor_index += 1
                        
                        if next_char == '*':
                            self._state = 'block comment'   
                            
                        else:
                            self._state = 'inline comment'                        
                    
                    #now we know we're handling a symbol and not a comment
                    else:
                        getting_token = False  
                        
                        #if there is no token stored yet in self._current_token, then the symbol is a token 
                        if len(self._current_token) == 0:
                            self._current_token += char 
                            
                        #if there is a token stored in self._current_token, then symbol ends that token
                        #return now so cursor is not advanced, so symbol can be picked up as token in next call 
                        else:                        
                            return len(self._current_token) > 0                             
                        
                elif char == '"':
                    self._state = 'string'
                
                #this is another character in a token                
                else:
                    self._current_token += char                
            
            self._cursor_index += 1
        
        return len(self._current_token) > 0              
    
    def get_token_type(self):
        """
        Returns type of the current token:
            - keyword
            - symbol
            - identifier
            - integerConstant
            - stringConstant
        """
        
        #self._current_token_is_string is first so that strings aren't marked as keywords
        if self._current_token_is_string: 
            return 'stringConstant'         
        
        elif self._current_token in lexical_elements.keywords:
            return 'keyword'
            
        elif self._current_token in lexical_elements.symbols:
            return 'symbol'       
            
        elif self._current_token.isdigit():
            return 'integerConstant'
            
        elif self._IDENTIFIER_REGEX.match(self._current_token):
            return 'identifier'        

        print('\nCURRENT TOKEN IS NOT A VALID TYPE:', self._current_token, '\n')            
        
    def get_current_token(self, xml=False):
        """
        Returns current token. 
        """
        
        if xml and self._current_token in lexical_elements.xml_entities:
            return lexical_elements.xml_entities[self._current_token]
            
        return self._current_token      
        
    def get_next_token(self, xml=False):
        """
        Checks to see if there is another token, and if there is, returns token. 
        """
        
        if self.has_more_to_process():
            token = self.advance()            
            if token:
                return self.get_current_token(xml=xml)

        return None            

    def cache_current_token(self):
        """
        Returns current token, cursor index and states for caching. 
        """  

        return self._current_token, self._cursor_index, self._current_token_is_string, self._state     

    def reset_current_token(self, token, index, is_string, state):
        """
        Sets or resets current token, cursor index and states to cached values. 
        """  
        
        self._current_token = token
        self._cursor_index = index 
        self._current_token_is_string = is_string
        self._state = state
        
    def write_xml(self):
        """
        Writes output to XML file. 
        """
        
        token = ''
        tag = ''
        
        translation_file = self._file_path.replace('.jack','T.xml')
        with open(translation_file, 'w') as f:
        
            f.write('<tokens>\n')
            while self.has_more_to_process():
            
                token = self.advance()                
                if token:            
                    tag = ('<' + self.get_token_type() + '> ' 
                           + self.get_current_token(xml=True) 
                           + ' </' + self.get_token_type() + '>\n')                         
                    f.write(tag)
                    
            f.write('</tokens>\n')    