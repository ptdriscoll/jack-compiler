# -*- coding: utf-8 -*- 

"""
Tests CompilationEngineXML methods. Runs from Compiler root directory.
To run tests in command line, i.e. for test_1_2 tests: prompt> python -m tests.test_1_2
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_1_2.Compiler.test_methods
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine_xml
import unittest, filecmp


class TestCompilerExpressions(unittest.TestCase):
    """
    Check compilation_engine_xml on Square
    """
    
    print('\nCHECKING Square\n')
    
    def test_expressions_1(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/Square_expressions_1.jack', 
                                                                './data_test_snippets_xml/Square_expressions_1.xml', 
                                                                test=True)
                                                                
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close() 
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> test </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'                
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <statements>\n'
                
                +  '      <letStatement>\n'
                +  '        <keyword> let </keyword>\n'
                +  '        <identifier> s </identifier>\n'
                +  '        <symbol> = </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <stringConstant> string constant </stringConstant>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </letStatement>\n'                
                
                +  '      <letStatement>\n' 
                +  '        <keyword> let </keyword>\n' 
                +  '        <identifier> s </identifier>\n' 
                +  '        <symbol> = </symbol>\n' 
                +  '        <expression>\n' 
                +  '          <term>\n' 
                +  '            <keyword> null </keyword>\n' 
                +  '          </term>\n' 
                +  '        </expression>\n' 
                +  '        <symbol> ; </symbol>\n' 
                +  '      </letStatement>\n'                 
                
                +  '      <letStatement>\n'
                +  '        <keyword> let </keyword>\n'
                +  '        <identifier> a </identifier>\n'
                +  '        <symbol> [ </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <integerConstant> 1 </integerConstant>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ] </symbol>\n'
                +  '        <symbol> = </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> a </identifier>\n'
                +  '            <symbol> [ </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <integerConstant> 2 </integerConstant>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ] </symbol>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </letStatement>\n'                
                
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n') 

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)

    def test_expressions_2(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/Square_expressions_2.jack', 
                                                                './data_test_snippets_xml/Square_expressions_2.xml', 
                                                                test=True)
                                                                
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close() 
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> test </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'                
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <statements>\n'
                
                +  '      <letStatement>\n'
                +  '        <keyword> let </keyword>\n'
                +  '        <identifier> i </identifier>\n'
                +  '        <symbol> = </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> i </identifier>\n'
                +  '          </term>\n'
                +  '          <symbol> * </symbol>\n'
                +  '          <term>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <symbol> - </symbol>\n'
                +  '                <term>\n'
                +  '                  <identifier> j </identifier>\n'
                +  '                </term>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </letStatement>\n'                
                
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n') 

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result) 

    def test_expressions_3(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/Square_expressions_3.jack', 
                                                                './data_test_snippets_xml/Square_expressions_3.xml', 
                                                                test=True)
                                                                
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close() 
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> test </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'                
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <statements>\n'
                
                +  '      <letStatement>\n'
                +  '        <keyword> let </keyword>\n'
                +  '        <identifier> j </identifier>\n'
                +  '        <symbol> = </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> j </identifier>\n'
                +  '          </term>\n'
                +  '          <symbol> / </symbol>\n'
                +  '          <term>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <symbol> - </symbol>\n'
                +  '                <term>\n'
                +  '                  <integerConstant> 2 </integerConstant>\n'
                +  '                </term>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </letStatement>\n'              
                
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n') 

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result) 

    def test_expressions_4(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/Square_expressions_4.jack', 
                                                                './data_test_snippets_xml/Square_expressions_4.xml', 
                                                                test=True)
                                                                
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close() 
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> test </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'                
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <statements>\n'
                
                +  '      <ifStatement>\n'
                +  '        <keyword> if </keyword>\n'
                +  '        <symbol> ( </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <symbol> ( </symbol>\n'
                +  '                <expression>\n'
                +  '                  <term>\n'
                +  '                    <identifier> y </identifier>\n'
                +  '                  </term>\n'
                +  '                  <symbol> + </symbol>\n'
                +  '                  <term>\n'
                +  '                    <identifier> size </identifier>\n'
                +  '                  </term>\n'
                +  '                </expression>\n'
                +  '                <symbol> ) </symbol>\n'
                +  '              </term>\n'
                +  '              <symbol> &lt; </symbol>\n'
                +  '              <term>\n'
                +  '                <integerConstant> 254 </integerConstant>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '          </term>\n'
                +  '          <symbol> &amp; </symbol>\n'
                +  '          <term>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <symbol> ( </symbol>\n'
                +  '                <expression>\n'
                +  '                  <term>\n'
                +  '                    <identifier> x </identifier>\n'
                +  '                  </term>\n'
                +  '                  <symbol> + </symbol>\n'
                +  '                  <term>\n'
                +  '                    <identifier> size </identifier>\n'
                +  '                  </term>\n'
                +  '                </expression>\n'
                +  '                <symbol> ) </symbol>\n'
                +  '              </term>\n'
                +  '              <symbol> &lt; </symbol>\n'
                +  '              <term>\n'
                +  '                <integerConstant> 510 </integerConstant>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ) </symbol>\n'
                +  '        <symbol> { </symbol>\n'
                +  '        <statements>\n'
                +  '          <doStatement>\n'
                +  '            <keyword> do </keyword>\n'
                +  '            <identifier> erase </identifier>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expressionList>\n'
                +  '            </expressionList>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </doStatement>\n'
                +  '          <letStatement>\n'
                +  '            <keyword> let </keyword>\n'
                +  '            <identifier> size </identifier>\n'
                +  '            <symbol> = </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> size </identifier>\n'
                +  '              </term>\n'
                +  '              <symbol> + </symbol>\n'
                +  '              <term>\n'
                +  '                <integerConstant> 2 </integerConstant>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </letStatement>\n'
                +  '          <doStatement>\n'
                +  '            <keyword> do </keyword>\n'
                +  '            <identifier> draw </identifier>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expressionList>\n'
                +  '            </expressionList>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </doStatement>\n'
                +  '        </statements>\n'
                +  '        <symbol> } </symbol>\n'
                +  '      </ifStatement>\n'
                +  '      <returnStatement>\n'
                +  '        <keyword> return </keyword>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </returnStatement>\n'         
                
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n') 

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)         
  

class CompareSquare(unittest.TestCase):
    """
    Compare outputs with correct versions
    """
    
    print('\nCOMPARING OUTPUTS')

    def test_run(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data/Square/Main.jack', 
                                                                './data/Square/Main.xml')
        self.assertTrue(filecmp.cmp('./data_compare/Square/Main.xml', 
                                    './data/Square/Main.xml'))          
     
        self.compile = compilation_engine_xml.CompilationEngine('./data/Square/Square.jack', 
                                                                './data/Square/Square.xml')
        self.assertTrue(filecmp.cmp('./data_compare/Square/Square.xml', 
                                    './data/Square/Square.xml'))  

        self.compile = compilation_engine_xml.CompilationEngine('./data/Square/SquareGame.jack', 
                                                                './data/Square/SquareGame.xml')
        self.assertTrue(filecmp.cmp('./data_compare/Square/SquareGame.xml', 
                                    './data/Square/SquareGame.xml'))   

class CompareArray(unittest.TestCase):
    """
    Compare outputs with correct versions
    """
    
    print('\nCOMPARING OUTPUTS')

    def test_run(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data/ArrayTest/Main.jack', 
                                                                './data/ArrayTest/Main.xml')
        self.assertTrue(filecmp.cmp('./data_compare/ArrayTest/Main.xml', 
                                    './data/ArrayTest/Main.xml'))                                      
 
if __name__=='__main__':
    unittest.main()