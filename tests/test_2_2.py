# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine's ability to produce virtual machine code. Runs from Compiler root directory.
To run tests in command line, i.e. for test_2_2 tests: prompt> python -m tests.test_2_2
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_2_2.TestCompiler.test_class
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine
from compiler import symbol_table as var_table
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine on Seven
    """
    
    print('\nCHECKING Seven\n')
    
    def test_class(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Seven_class/Main.jack', 
                                                            './data_test_snippets_vm/Seven_class/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        result = self.compile._class 
        compare = 'Main'        
        #print(compare)        
        #print(result) 
        #print()
        #print(self.compile.get_print_var_table())
        self.assertEqual(compare, result)
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Seven_class/Main.vm', 
                                    './data_test_snippets_vm/Seven_class/compare/Main.vm')) 
    def test_subroutine(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Seven_subroutine/Main.jack', 
                                                            './data_test_snippets_vm/Seven_subroutine/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Seven_subroutine/Main.vm', 
                                    './data_test_snippets_vm/Seven_subroutine/compare/Main.vm'))

    def test_do(self):
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Seven_do/Main.jack', 
                                                            './data_test_snippets_vm/Seven_do/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Seven_do/Main.vm', 
                                    './data_test_snippets_vm/Seven_do/compare/Main.vm'))
        
    def test_return(self):
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Seven_return/Main.jack', 
                                                            './data_test_snippets_vm/Seven_return/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Seven_return/Main.vm', 
                                    './data_test_snippets_vm/Seven_return/compare/Main.vm'))  
                                    
    def test_string(self):
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Seven_string/Main.jack', 
                                                            './data_test_snippets_vm/Seven_string/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Seven_string/Main.vm', 
                                    './data_test_snippets_vm/Seven_string/compare/Main.vm'))                                      

    def test_seven(self):
        self.compile = compilation_engine.CompilationEngine('./data/Seven/Main.jack', 
                                                            './data/Seven/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Seven/Main.vm', 
                                    './data_compare/Seven/Main.vm'))                                     
 
if __name__=='__main__':
    unittest.main()