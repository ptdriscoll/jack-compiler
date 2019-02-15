# -*- coding: utf-8 -*- 

"""
Out of five types of lexical elements, this includes two that can be looked up in lists.
Also included here is a lookup dictionary for XML entity codes.
"""


keywords = ['class', 'constructor', 'function', 'method', 
            'field', 'static', 'var', 
            'int', 'char', 'boolean', 'void', 
            'true', 'false', 'null', 'this', 
            'let', 'do', 'if', 'else', 'while', 'return'] 
           
symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', 
           '+', '-', '*', '/', '&', '|', '<', '>', '=', '~' ]
           
xml_entities = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}    