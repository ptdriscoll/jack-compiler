# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine's ability to produce virtual machine code. Runs from Compiler root directory.
To run tests in command line, i.e. for test_2_4 tests: prompt> python -m tests.test_2_4
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_2_4.TestCompiler.test_main
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine
from compiler import symbol_table as var_table
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine on Square
    """
    
    print('\nCHECKING Square\n')
    
    def test_main(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Square_main/Main.jack', 
                                                            './data_test_snippets_vm/Square_main/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Square_main/Main.vm', 
                                    './data_test_snippets_vm/Square_main/compare/Main.vm'))  

    def test_array(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Square_array/Main.jack', 
                                                            './data_test_snippets_vm/Square_array/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Square_array/Main.vm', 
                                    './data_test_snippets_vm/Square_array/compare/Main.vm'))
                              
    def test_Square_Main(self):
        self.compile = compilation_engine.CompilationEngine('./data/Square/Main.jack', 
                                                            './data/Square/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Square/Main.vm', 
                                    './data_compare/Square/Main.vm'))                                      
                      
    def test_Square_Square(self):
        self.compile = compilation_engine.CompilationEngine('./data/Square/Square.jack', 
                                                            './data/Square/Square.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Square/Square.vm', 
                                    './data_compare/Square/Square.vm')) 
                                    
    def test_Square_SquareGame(self):
        self.compile = compilation_engine.CompilationEngine('./data/Square/SquareGame.jack', 
                                                            './data/Square/SquareGame.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Square/SquareGame.vm', 
                                    './data_compare/Square/SquareGame.vm'))                                     

                                    
if __name__=='__main__':
    unittest.main()