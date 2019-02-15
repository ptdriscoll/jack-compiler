# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine's ability to produce virtual machine code. Runs from Compiler root directory.
To run tests in command line, i.e. for test_2_3 tests: prompt> python -m tests.test_2_3
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_2_3.TestCompiler.test_class_var
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine
from compiler import symbol_table as var_table
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine on ConvertToBin
    """
    
    print('\nCHECKING ConvertToBin\n')
    
    def test_class_var(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/ConvertToBin_class_var/Main.jack', 
                                                            './data_test_snippets_vm/ConvertToBin_class_var/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        
        kind, type, index = self.compile.get_var_attributes('value_1')
        self.assertTrue(kind, 'field')
        self.assertTrue(type, 'char')
        self.assertEqual(index, 0)
        
        kind, type, index = self.compile.get_var_attributes('value_2')        
        self.assertTrue(kind, 'field')
        self.assertTrue(type, 'char')
        self.assertEqual(index, 1)
        
        kind, type, index = self.compile.get_var_attributes('value_3')
        self.assertTrue(kind, 'field')
        self.assertTrue(type, 'char')
        self.assertEqual(index, 2)
        
        kind, type, index = self.compile.get_var_attributes('value')
        self.assertTrue(kind, 'static')
        self.assertTrue(type, 'int')
        self.assertEqual(index, 0)        
        
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/ConvertToBin_class_var/Main.vm', 
                                    './data_test_snippets_vm/ConvertToBin_class_var/compare/Main.vm'))
                                    
    def test_var(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/ConvertToBin_var/Main.jack', 
                                                            './data_test_snippets_vm/ConvertToBin_var/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        
        kind, type, index = self.compile.get_var_attributes('value')
        self.assertTrue(kind, 'var')
        self.assertTrue(type, 'int')
        self.assertEqual(index, 0)
        
        kind, type, index = self.compile.get_var_attributes('value_1')
        self.assertTrue(kind, 'var')
        self.assertTrue(type, 'bool')
        self.assertEqual(index, 1)

        kind, type, index = self.compile.get_var_attributes('value_2')
        self.assertTrue(kind, 'var')
        self.assertTrue(type, 'bool')
        self.assertEqual(index, 2)        
        
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/ConvertToBin_var/Main.vm', 
                                    './data_test_snippets_vm/ConvertToBin_var/compare/Main.vm'))                                    
   
    def test_let(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/ConvertToBin_let/Main.jack', 
                                                            './data_test_snippets_vm/ConvertToBin_let/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/ConvertToBin_let/Main.vm', 
                                    './data_test_snippets_vm/ConvertToBin_let/compare/Main.vm'))        
        
    def test_if(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/ConvertToBin_if/Main.jack', 
                                                            './data_test_snippets_vm/ConvertToBin_if/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/ConvertToBin_if/Main.vm', 
                                    './data_test_snippets_vm/ConvertToBin_if/compare/Main.vm'))          
                                
    def test_while(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/ConvertToBin_while/Main.jack', 
                                                            './data_test_snippets_vm/ConvertToBin_while/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/ConvertToBin_while/Main.vm', 
                                    './data_test_snippets_vm/ConvertToBin_while/compare/Main.vm')) 

    def test_ConvertToBin(self):
        self.compile = compilation_engine.CompilationEngine('./data/ConvertToBin/Main.jack', 
                                                            './data/ConvertToBin/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/ConvertToBin/Main.vm', 
                                    './data_compare/ConvertToBin/Main.vm'))
                                    
if __name__=='__main__':
    unittest.main()