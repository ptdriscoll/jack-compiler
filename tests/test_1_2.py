# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine XML. Runs from Compiler root directory.
To run tests in command line, i.e. for test_1_2 tests: prompt> python -m tests.test_1_2
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_1_2.TestCompiler.test_class
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine_xml
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine_xml on ExpressionLessSquare
    """
    
    print('\nCHECKING ExpressionLessSquare\n')
    
    def test_class(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_class.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_class.xml', 
                                                                test=True)
                                                                
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier> Main </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)

    def test_class_var_dec(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_class_var_dec.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_class_var_dec.xml', 
                                                                test=True)  
                                                                
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier> Main </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                
                +  '  <classVarDec>\n'
                +  '    <keyword> static </keyword>\n'                
                +  '    <keyword> boolean </keyword>\n'
                +  '    <identifier> test </identifier>\n'                
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n' 
                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')

        #print(self.compile)               
        #print(compare) 
        #print(result) 
        self.assertEqual(compare, result) 

    def test_subroutine(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_subroutine.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_subroutine.xml', 
                                                                test=True)  
                                                                
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier> Main </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                +  '  <classVarDec>\n'
                +  '    <keyword> static </keyword>\n'                
                +  '    <keyword> boolean </keyword>\n'
                +  '    <identifier> test </identifier>\n'                
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n'                
                
                +  '  <subroutineDec>\n'
                +  '    <keyword> function </keyword>\n'                
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier> main </identifier>\n'                 
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '    </parameterList>\n'
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'                
                +  '      <symbol> { </symbol>\n'
                +  '      <statements>\n'
                +  '      </statements>\n'                
                +  '      <symbol> } </symbol>\n'
                +  '    </subroutineBody>\n'                
                +  '  </subroutineDec>\n'     
                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')
                
        #print(self.compile)                
        #print(compare) 
        #print(result)   
        self.assertEqual(compare, result)        
                
    def test_parameter_list(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_parameter_list.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_parameter_list.xml', 
                                                                test=True)  
        
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close()            
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> main </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'
                
                +  '    <keyword> int </keyword>\n'
                +  '    <identifier> arg1 </identifier>\n'
                
                +  '    <symbol> , </symbol>\n' 
                +  '    <keyword> char </keyword>\n'
                +  '    <identifier> arg2 </identifier>\n'
                
                +  '    <symbol> , </symbol>\n' 
                +  '    <keyword> boolean </keyword>\n'
                +  '    <identifier> arg3 </identifier>\n'
                
                +  '    <symbol> , </symbol>\n'               
                +  '    <identifier> ClassType </identifier>\n'
                +  '    <identifier> ClassInstance </identifier>\n'  
                
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <statements>\n'
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n')                
                
        #print(self.compile)                
        #print(compare) 
        #print(result) 
        self.assertEqual(compare, result)
        
    def test_var_dec(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_var_dec.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_var_dec.xml', 
                                                                test=True)  
        
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close()            
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> main </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'              
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                
                +  '    <varDec>\n'              
                +  '      <keyword> var </keyword>\n'                
                +  '      <identifier> SquareGame </identifier>\n'                
                +  '      <identifier> game </identifier>\n'                
                +  '      <symbol> ; </symbol>\n' 
                +  '    </varDec>\n' 
                
                +  '    <varDec>\n'            
                +  '      <keyword> var </keyword>\n'                  
                +  '      <keyword> int </keyword>\n'                
                +  '      <identifier> var1 </identifier>\n'                
                +  '      <symbol> , </symbol>\n'             
                +  '      <identifier> var2 </identifier>\n'                
                +  '      <symbol> ; </symbol>\n' 
                +  '    </varDec>\n'  
                
                +  '    <varDec>\n'    
                +  '      <keyword> var </keyword>\n'                  
                +  '      <keyword> char </keyword>\n'                
                +  '      <identifier> varString </identifier>\n'                
                +  '      <symbol> ; </symbol>\n'  
                +  '    </varDec>\n'  
                
                +  '    <varDec>\n'        
                +  '      <keyword> var </keyword>\n'                  
                +  '      <keyword> boolean </keyword>\n'                
                +  '      <identifier> truthy </identifier>\n'                
                +  '      <symbol> ; </symbol>\n'                
                +  '    </varDec>\n'  
                
                +  '    <statements>\n'
                +  '    </statements>\n'                 
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n')                
                
        #print(self.compile)                
        #print(compare) 
        #print(result)
        self.assertEqual(compare, result)   

    def test_statements_do(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_statements_do.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_statements_do.xml', 
                                                                test=True)  
        
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close()            
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> main </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'              
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <varDec>\n'              
                +  '      <keyword> var </keyword>\n'                
                +  '      <identifier> SquareGame </identifier>\n'                
                +  '      <identifier> game </identifier>\n'                
                +  '      <symbol> ; </symbol>\n' 
                +  '    </varDec>\n' 
                +  '    <statements>\n' 
                
                +  '      <doStatement>\n'
                +  '        <keyword> do </keyword>\n'
                +  '        <identifier> game </identifier>\n'
                +  '        <symbol> . </symbol>\n'
                +  '        <identifier> run </identifier>\n'
                +  '        <symbol> ( </symbol>\n'
                +  '        <expressionList>\n'
                +  '        </expressionList>\n'
                +  '        <symbol> ) </symbol>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </doStatement>\n' 
                
                +  '      <doStatement>\n'
                +  '        <keyword> do </keyword>\n'
                +  '        <identifier> game </identifier>\n'
                +  '        <symbol> . </symbol>\n'
                +  '        <identifier> dispose </identifier>\n'
                +  '        <symbol> ( </symbol>\n'
                +  '        <expressionList>\n'
                +  '        </expressionList>\n'
                +  '        <symbol> ) </symbol>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </doStatement>\n'       
                
                +  '    </statements>\n'               
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n')                
                
        #print(self.compile)                
        #print(compare) 
        #print(result)
        self.assertEqual(compare, result) 

    def test_statements_let(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_statements_let.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_statements_let.xml', 
                                                                test=True)  
        
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close()            
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> main </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'              
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <varDec>\n'              
                +  '      <keyword> var </keyword>\n'                
                +  '      <identifier> SquareGame </identifier>\n'                
                +  '      <identifier> game </identifier>\n'                
                +  '      <symbol> ; </symbol>\n' 
                +  '    </varDec>\n' 
                +  '    <statements>\n' 
                
                +  '      <letStatement>\n'
                +  '        <keyword> let </keyword>\n'
                +  '        <identifier> game </identifier>\n'
                +  '        <symbol> = </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> game </identifier>\n'
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

    def test_statements_return(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_statements_return.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_statements_return.xml', 
                                                                test=True)  
        
        while self.compile._tokenize.get_current_token() in ['constructor', 'function', 'method']:            
            self.compile.compile_subroutine()  

        self.compile.close()            
        result = self.compile._xml 
        compare = ('<subroutineDec>\n'
                +  '  <keyword> function </keyword>\n'                
                +  '  <keyword> void </keyword>\n'
                +  '  <identifier> main </identifier>\n'                 
                +  '  <symbol> ( </symbol>\n'
                +  '  <parameterList>\n'              
                +  '  </parameterList>\n'
                +  '  <symbol> ) </symbol>\n'
                +  '  <subroutineBody>\n'                
                +  '    <symbol> { </symbol>\n'
                +  '    <varDec>\n'              
                +  '      <keyword> var </keyword>\n'                
                +  '      <identifier> SquareGame </identifier>\n'                
                +  '      <identifier> game </identifier>\n'                
                +  '      <symbol> ; </symbol>\n' 
                +  '    </varDec>\n' 
                +  '    <statements>\n' 
                
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

    def test_statements_if(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_statements_if.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_statements_if.xml', 
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
                
                +  '    <varDec>\n'
                +  '      <keyword> var </keyword>\n'
                +  '      <identifier> Array </identifier>\n'
                +  '      <identifier> a </identifier>\n'
                +  '      <symbol> ; </symbol>\n'
                +  '    </varDec>\n'                
                +  '    <statements>\n'
                
                +  '      <ifStatement>\n'
                +  '        <keyword> if </keyword>\n'
                +  '        <symbol> ( </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> i </identifier>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ) </symbol>\n'
                +  '        <symbol> { </symbol>\n'
                +  '        <statements>\n'

                +  '          <letStatement>\n'
                +  '            <keyword> let </keyword>\n'
                +  '            <identifier> s </identifier>\n'
                +  '            <symbol> = </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> j </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </letStatement>\n'
                +  '          <letStatement>\n'
                +  '            <keyword> let </keyword>\n'
                +  '            <identifier> a </identifier>\n'
                +  '            <symbol> [ </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> i </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ] </symbol>\n'
                +  '            <symbol> = </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> j </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </letStatement>\n'
                +  '        </statements>\n'
                +  '        <symbol> } </symbol>\n'
                +  '        <keyword> else </keyword>\n'
                +  '        <symbol> { </symbol>\n'
                +  '        <statements>\n'

                +  '          <letStatement>\n'
                +  '            <keyword> let </keyword>\n'
                +  '            <identifier> i </identifier>\n'
                +  '            <symbol> = </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> i </identifier>\n'
                +  '              </term>\n'
                +  '              <symbol> | </symbol>\n'
                +  '              <term>\n'
                +  '                <identifier> j </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </letStatement>\n'
                +  '        </statements>\n'
                +  '        <symbol> } </symbol>\n'
                +  '      </ifStatement>\n'           
                   
                +  '    </statements>\n'               
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n')                
                
        #print(self.compile)                
        #print(compare) 
        #print(result)
        self.assertEqual(compare, result)  

    def test_statements_while(self): 
        self.compile = compilation_engine_xml.CompilationEngine('./data_test_snippets_xml/ExpressionLessSquare_statements_while.jack', 
                                                                './data_test_snippets_xml/ExpressionLessSquare_statements_while.xml', 
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
                
                +  '      <whileStatement>\n'
                +  '        <keyword> while </keyword>\n'
                +  '        <symbol> ( </symbol>\n'
                +  '        <expression>\n'
                +  '          <term>\n'
                +  '            <identifier> key </identifier>\n'
                +  '          </term>\n'
                +  '        </expression>\n'
                +  '        <symbol> ) </symbol>\n'
                +  '        <symbol> { </symbol>\n'
                +  '        <statements>\n'
                +  '          <letStatement>\n'
                +  '            <keyword> let </keyword>\n'
                +  '            <identifier> key </identifier>\n'
                +  '            <symbol> = </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier> key </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </letStatement>\n'
                +  '          <doStatement>\n'
                +  '            <keyword> do </keyword>\n'
                +  '            <identifier> moveSquare </identifier>\n'
                +  '            <symbol> ( </symbol>\n'
                +  '            <expressionList>\n'
                +  '            </expressionList>\n'
                +  '            <symbol> ) </symbol>\n'
                +  '            <symbol> ; </symbol>\n'
                +  '          </doStatement>\n'
                +  '        </statements>\n'
                +  '        <symbol> } </symbol>\n'
                +  '      </whileStatement>\n'           
                   
                +  '    </statements>\n'               
                +  '    <symbol> } </symbol>\n'
                +  '  </subroutineBody>\n'                
                +  '</subroutineDec>\n')                
                
        #print(self.compile)                
        #print(compare) 
        #print(result)
        self.assertEqual(compare, result)   

class Compare(unittest.TestCase):
    """
    Compare outputs with correct versions
    """
    
    print('\nCOMPARING OUTPUTS')

    def test_run(self):    
        self.compile = compilation_engine_xml.CompilationEngine('./data/ExpressionLessSquare/Main.jack', 
                                                                './data/ExpressionLessSquare/Main.xml')
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/Main.xml', 
                                    './data/ExpressionLessSquare/Main.xml'))          
     
        self.compile = compilation_engine_xml.CompilationEngine('./data/ExpressionLessSquare/Square.jack', 
                                                                './data/ExpressionLessSquare/Square.xml')
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/Square.xml', 
                                    './data/ExpressionLessSquare/Square.xml'))  

        self.compile = compilation_engine_xml.CompilationEngine('./data/ExpressionLessSquare/SquareGame.jack', 
                                                                './data/ExpressionLessSquare/SquareGame.xml')
        self.assertTrue(filecmp.cmp('./data_compare/ExpressionLessSquare/SquareGame.xml', 
                                    './data/ExpressionLessSquare/SquareGame.xml'))          
 
if __name__=='__main__':
    unittest.main()