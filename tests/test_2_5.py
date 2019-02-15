# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine's ability to produce virtual machine code. Runs from Compiler root directory.
To run tests in command line, i.e. for test_2_5 tests: prompt> python -m tests.test_2_5
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_2_5.TestCompiler.test_array
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine
from compiler import symbol_table as var_table
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine on Average, ComplexArrays and Pong
    """
    
    print('\nCHECKING Average, ComplexArrays and Pong\n')
    
    def test_array(self):    
        self.compile = compilation_engine.CompilationEngine('./data_test_snippets_vm/Average_array/Main.jack', 
                                                            './data_test_snippets_vm/Average_array/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data_test_snippets_vm/Average_array/Main.vm', 
                                    './data_test_snippets_vm/Average_array/compare/Main.vm'))                                  

    def test_Average(self):
        self.compile = compilation_engine.CompilationEngine('./data/Average/Main.jack', 
                                                            './data/Average/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Average/Main.vm', 
                                    './data_compare/Average/Main.vm'))
    def test_ComplexArrays(self):
        self.compile = compilation_engine.CompilationEngine('./data/ComplexArrays/Main.jack', 
                                                            './data/ComplexArrays/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/ComplexArrays/Main.vm', 
                                    './data_compare/ComplexArrays/Main.vm')) 

    def test_Pong_Main(self):
        self.compile = compilation_engine.CompilationEngine('./data/Pong/Main.jack', 
                                                            './data/Pong/Main.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Pong/Main.vm', 
                                    './data_compare/Pong/Main.vm')) 

    def test_Pong_Ball(self):
        self.compile = compilation_engine.CompilationEngine('./data/Pong/Ball.jack', 
                                                            './data/Pong/Ball.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Pong/Ball.vm', 
                                    './data_compare/Pong/Ball.vm')) 

    def test_Pong_Bat(self):
        self.compile = compilation_engine.CompilationEngine('./data/Pong/Bat.jack', 
                                                            './data/Pong/Bat.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Pong/Bat.vm', 
                                    './data_compare/Pong/Bat.vm')) 

    def test_PongGame(self):
        self.compile = compilation_engine.CompilationEngine('./data/Pong/PongGame.jack', 
                                                            './data/Pong/PongGame.vm', 
                                                            test=True)
                                                                
        self.compile.compile_class()    
        #print(self.compile.get_print_var_table())
        self.assertTrue(filecmp.cmp('./data/Pong/PongGame.vm', 
                                    './data_compare/Pong/PongGame.vm'))                                     
                               
if __name__=='__main__':
    unittest.main()