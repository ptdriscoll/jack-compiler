# -*- coding: utf-8 -*- 

"""
Tests Tokenizer methods. Runs from Compiler root directory.
To run tests in command line, i.e. for test_1_1 tests: prompt> python -m tests.test_1_1
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_1_1.TestTokenizer.test_advance
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import tokenizer
import unittest, filecmp


class TestTokenizer(unittest.TestCase):
    """
    Check tokenizer on ExpressionLessSquare
    """
    
    print('\nCHECKING ExpressionLessSquare')
    
    def setUp(self):
        self.tokenize = tokenizer.Tokenizer('./data/Square/Main.jack')
            
    def test_advance(self):        
        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('class', token) 
        self.assertEqual('code', state) 
        self.assertEqual('keyword', type)
        print(self.tokenize)  

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('Main', token) 
        self.assertEqual('code', state) 
        self.assertEqual('identifier', type)
        print(self.tokenize)   

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('{', token) 
        self.assertEqual('code', state) 
        self.assertEqual('symbol', type)
        print(self.tokenize)
        
        for x in range(2):
            self.tokenize.advance()
            
        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('test', token) 
        self.assertEqual('code', state) 
        self.assertEqual('identifier', type)
        print(self.tokenize)   

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual(';', token) 
        self.assertEqual('code', state) 
        self.assertEqual('symbol', type)
        print(self.tokenize) 

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('function', token) 
        self.assertEqual('code', state) 
        self.assertEqual('keyword', type)
        print(self.tokenize) 

        for x in range(61):
            self.tokenize.advance()
            
        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('s', token) 
        self.assertEqual('code', state) 
        self.assertEqual('identifier', type)
        print(self.tokenize)          

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        is_string = self.tokenize._current_token_is_string
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('=', token) 
        self.assertEqual(False, is_string)
        self.assertEqual('code', state) 
        self.assertEqual('symbol', type)
        print(self.tokenize) 
        
        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        is_string = self.tokenize._current_token_is_string
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual('string constant', token) 
        self.assertEqual(True, is_string)
        self.assertEqual('code', state) 
        self.assertEqual('stringConstant', type)
        print(self.tokenize)        

        result = self.tokenize.advance()
        token = self.tokenize.get_current_token()
        is_string = self.tokenize._current_token_is_string
        state = self.tokenize._state
        type = self.tokenize.get_token_type()
        self.assertEqual(True, result) 
        self.assertEqual(';', token) 
        self.assertEqual(False, is_string)
        self.assertEqual('code', state) 
        self.assertEqual('symbol', type)
        print(self.tokenize)         
        
    def test_get_next_token(self):        
        result = self.tokenize.get_next_token()
        type = self.tokenize.get_token_type()      
        self.assertEqual('class', result)
        self.assertEqual('keyword', type)        
        
        result = self.tokenize.get_next_token()
        type = self.tokenize.get_token_type() 
        self.assertEqual('Main', result) 
        self.assertEqual('identifier', type)

        result = self.tokenize.get_next_token()
        type = self.tokenize.get_token_type() 
        self.assertEqual('{', result)  
        self.assertEqual('symbol', type)        
       
        for x in range(2):
            self.tokenize.advance()
            
        result = self.tokenize.get_next_token()
        type = self.tokenize.get_token_type() 
        self.assertEqual('test', result)  
        self.assertEqual('identifier', type)        
        
class Compare(unittest.TestCase):
    """
    Compare outputs with correct versions
    """
    
    print('\nCOMPARING OUTPUTS')

    def test_run(self):
        self.tokenize = tokenizer.Tokenizer('./data/Square/Main.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/Square/MainT.xml', './data/Square/MainT.xml'))          
     
        self.tokenize = tokenizer.Tokenizer('./data/Square/Square.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/Square/SquareT.xml', './data/Square/SquareT.xml'))  

        self.tokenize = tokenizer.Tokenizer('./data/Square/Main.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/Square/SquareGameT.xml', './data/Square/SquareGameT.xml'))          
        
        self.tokenize = tokenizer.Tokenizer('./data/ExpressionLessSquare/Main.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/MainT.xml', './data/ExpressionLessSquare/MainT.xml'))          
     
        self.tokenize = tokenizer.Tokenizer('./data/ExpressionLessSquare/Square.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/SquareT.xml', './data/ExpressionLessSquare/SquareT.xml'))  

        self.tokenize = tokenizer.Tokenizer('./data/ExpressionLessSquare/Main.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/SquareGameT.xml', './data/ExpressionLessSquare/SquareGameT.xml'))          

        self.tokenize = tokenizer.Tokenizer('./data/ArrayTest/Main.jack')
        self.tokenize.write_xml()
        self.assertTrue(filecmp.cmp('./data_compare/ArrayTest/MainT.xml', './data/ArrayTest/MainT.xml'))
        
if __name__=='__main__':
    unittest.main()