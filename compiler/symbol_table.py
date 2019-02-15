# -*- coding: utf-8 -*- 

"""
A symbol table that associates names with information needed for Jack compilation: type, kind, and
running index. The symbol table has 2 nested scopes (class/subroutine).
"""


class SymbolTable:
    """
    This module provides services for creating, populating, and using a symbol table. Each symbol has a scope 
    from which it is visible in the source code. In the symbol table, each symbol is given a running number (index) 
    within the scope, where the index starts at 0 and is reset when starting a new scope. 
    
    These identifiers may appear in the symbol table:
        - static: Scope: class
        - field: Scope: class
        - argument: Scope: subroutine (method/function/constructor)
        - var: Scope: subroutine (method/function/constructor)
    
    When compiling code, any identifier not found in the symbol table may be assumed to be a subroutine name 
    or a class name. Since the Jack language syntax rules suffice for distinguishing between these two possibilities, 
    and since no "linking" needs to be done by the compiler, these identifiers do not have to be kept in the symbol table. 
    """
    
    def __init__(self):
        """
        Creates new empty symbol table.
        Example for method's position 1 argument for an integer (position 0 is for method's this object): 
            {'sum': {'type': 'int', 'kind': 'argument', 'index': 1}}        
        """
        
        self._class = {}
        self._subroutine = {}
        self._var_count = {'static': 0, 
                         'field': 0,
                         'argument': 0, 
                         'var': 0}

    def __str__(self):
        to_print = 'Class Table\n-----------\n'
        if self._class:
            for key, value in self._class.items():
                to_print += key + '\t' + value['type'] + '\t' + value['kind'] + '\t' + str(value['index']) + '\n'
        else:
            to_print += 'No variables\n'                
                
        to_print += '\nSubroutine Table\n----------------\n'   
        if self._subroutine:    
            to_print += 'NAME\tKIND\tTYPE\tINDEX\n===\t====\t====\t=====\n' 
            for key, value in self._subroutine.items():
                to_print += key + '\t' + value['type'] + '\t' + value['kind'] + '\t' + str(value['index']) + '\n'
        else:
            to_print += 'No variables\n'             
 
        return to_print
                         
    def start_subroutine(self):
        """
        Starts new subroutine scope (i.e. erases all names in the previous subroutine's scope). 
        """
        
        self._subroutine = {}
        self._var_count['argument'] = 0
        self._var_count['var'] = 0          
        
    def define(self, name, type, kind):
        """
        Accepts name, type (static, field, argument, var) and kind. 
        Defines new identifier of a given name, type and kind, and assigns it a running index.        
        static and field identifiers have a class scope, while argument and var identifiers have a subroutine scope. 
        """        
        
        if kind in ['static', 'field']: 
            self._class[name] = {'type': type, 'kind': kind, 'index': self._var_count[kind]}  
            
        else:
            self._subroutine[name] = {'type': type, 'kind': kind, 'index': self._var_count[kind]}
            
        self._var_count[kind] += 1    
        
    def var_count(self, kind):
        """
        Accepts kind (static, field, argument, var). 
        Returns number of variables, as integer, of the given kind already defined in the current scope. 
        """
        
        return self._var_count[kind]
        
    def exists(self, name):
        """
        Checks whether keyword is in symbol table and returns bool. 
        """
        
        if name in self._subroutine or name in self._class:
            return True  

        return False         

    def type_of(self, name):
        """
        Returns the type of named identifier in current scope. 
        """
        
        if name in self._subroutine:
            return self._subroutine[name]['type']

        elif name in self._class:
            return self._class[name]['type']  

        return None         
        
    def kind_of(self, name, vm=False):
        """
        Returns the kind of named identifier in current scope (static, field, argument, var).
        If vm=True, then field is returned as this, and var is returned as local.        
        Returns None if identifier is unknown in the current scope.
        """
        
        kind = None
        
        vm_map = {'static': 'static',
                  'field': 'this',
                  'argument': 'argument',
                  'var': 'local',
                  None: None}
        
        if name in self._subroutine:
            kind = self._subroutine[name]['kind']

        elif name in self._class:
            kind = self._class[name]['kind']  
            
        if vm:
            kind = vm_map[kind]    

        return kind            
        
    def index_of(self, name):
        """
        Returns the index, as integer, assigned to named dentifier.
        """
        
        if name in self._subroutine:
            return self._subroutine[name]['index']

        elif name in self._class:
            return self._class[name]['index']  

        return None
        
    def get_class_table(self):
        """
        Returns symbol class table.
        """
        return self._class 
        
    def get_subroutine_table(self):
        """
        Returns symbol subroutine table.
        """
        return self._subroutine          