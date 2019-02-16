# -*- coding: utf-8 -*- 

"""
Tests CompilationEngine XML with added properties for identifiers. Runs from Compiler root directory.
To run tests in command line, i.e. for test_2_1 tests: prompt> python -m tests.test_2_1
To run a specific test, note addition of unittest: 
    prompt> python -m unittest tests.test_2_1.TestCompiler.test_class
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import compiler 
from compiler import compilation_engine_xml_vars
from compiler import symbol_table as var_table
import unittest, filecmp


class TestCompiler(unittest.TestCase):
    """
    Check compilation_engine_xml_vars on Square
    """
    
    print('\nCHECKING Square\n')
    
    def test_class(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_class.jack', 
                                                                './data_test_snippets_xml/Square_class_VARS.xml', 
                                                                test=True)
                                                                
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)
        
    def test_class_vars(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_class_vars.jack', 
                                                                './data_test_snippets_xml/Square_class_vars_VARS.xml', 
                                                                test=True)
                                                                
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                
                +  '  <classVarDec>\n'
                +  '    <keyword> field </keyword>\n'
                +  '    <keyword> int </keyword>\n'
                +  '    <identifier kind="field" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '    <symbol> , </symbol>\n'
                +  '    <identifier kind="field" type="int" index="1" assigned="false"> y </identifier>\n'
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n'
                +  '  <classVarDec>\n'
                +  '    <keyword> field </keyword>\n'
                +  '    <keyword> int </keyword>\n'
                +  '    <identifier kind="field" type="int" index="2" assigned="false"> size </identifier>\n'
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n'
                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')

        #print(self.compile)                
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)       

    def test_subroutine_args(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_args.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_args_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                
                +  '  <subroutineDec>\n'
                +  '    <keyword> constructor </keyword>\n'
                +  '    <identifier> Square </identifier>\n'
                +  '    <identifier kind="subroutine"> new </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="0" assigned="false"> Ax </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="1" assigned="false"> Ay </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="2" assigned="false"> Asize </identifier>\n'
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

    def test_subroutine_method_args(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_method_args.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_method_args_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'
                
                +  '  <subroutineDec>\n'
                +  '    <keyword> method </keyword>\n'
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="1" assigned="false"> Ax </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="2" assigned="false"> Ay </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="3" assigned="false"> Asize </identifier>\n'
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
        
        result = self.compile.get_print_var_table()
        compare = ('Class Table\n'
                +  '-----------\n'
                +  'No variables\n\n'
                
                +  'Subroutine Table\n'
                +  '----------------\n'
                +  'NAME\tKIND\tTYPE\tINDEX\n'
                +  '===\t====\t====\t=====\n'
                +  'this\targument\tSquare\t0\n'
                +  'Ax\targument\tint\t1\n'
                +  'Ay\targument\tint\t2\n'
                +  'Asize\targument\tint\t3\n') 

        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)                 

    def test_subroutine_locals(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_locals.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_locals_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'                
                +  '  <subroutineDec>\n'
                +  '    <keyword> method </keyword>\n'
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '    </parameterList>\n'
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'
                +  '      <symbol> { </symbol>\n'             
               
                +  '      <varDec>\n'                
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '        <symbol> , </symbol>\n'
                +  '        <identifier kind="var" type="int" index="1" assigned="false"> y </identifier>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </varDec>\n'                  
                +  '      <varDec>\n'
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="2" assigned="false"> size </identifier>\n'
                +  '        <symbol> ; </symbol>\n'
                +  '      </varDec>\n'
                +  '      <statements>\n'                  
                +  '        <returnStatement>\n'
                +  '          <keyword> return </keyword>\n'
                +  '          <symbol> ; </symbol>\n'
                +  '        </returnStatement>\n'                
                +  '      </statements>\n'                 
              
                +  '      <symbol> } </symbol>\n'                  
                +  '    </subroutineBody>\n'              
                +  '  </subroutineDec>\n'                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')               

        #print(self.compile) 
        #print(self.compile.get_print_var_table())         
        #print(compare)        
        #print(result) 
        #self.maxDiff = None
        self.assertEqual(compare, result)  

    def test_subroutine_let(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_let.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_let_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n' 
                +  '  <classVarDec>\n'
                +  '    <keyword> field </keyword>\n'
                +  '    <keyword> int </keyword>\n'
                +  '    <identifier kind="field" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n'                
                +  '  <subroutineDec>\n'
                +  '    <keyword> method </keyword>\n'
                +  '    <keyword> char </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="1" assigned="false"> Ax </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="2" assigned="false"> Ay </identifier>\n'
                +  '    </parameterList>\n'  
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'
                +  '      <symbol> { </symbol>\n'
                +  '      <varDec>\n'                
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="0" assigned="false"> y </identifier>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </varDec>\n' 
                +  '      <statements>\n'                
                
                +  '        <letStatement>\n'
                +  '          <keyword> let </keyword>\n'
                +  '          <identifier kind="field" type="int" index="0" assigned="true"> x </identifier>\n'
                +  '          <symbol> = </symbol>\n'
                +  '          <expression>\n'
                +  '            <term>\n'
                +  '              <identifier kind="argument" type="int" index="1" assigned="true"> Ax </identifier>\n'
                +  '            </term>\n'
                +  '          </expression>\n'
                +  '          <symbol> ; </symbol>\n'
                +  '        </letStatement>\n'
                +  '        <letStatement>\n'
                +  '          <keyword> let </keyword>\n'
                +  '          <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '          <symbol> = </symbol>\n'
                +  '          <expression>\n'
                +  '            <term>\n'
                +  '              <identifier kind="argument" type="int" index="2" assigned="true"> Ay </identifier>\n'
                +  '            </term>\n'
                +  '          </expression>\n'
                +  '          <symbol> ; </symbol>\n'
                +  '        </letStatement>\n'                
                
                +  '        <returnStatement>\n'
                +  '          <keyword> return </keyword>\n'
                +  '          <expression>\n'
                +  '            <term>\n'
                +  '              <keyword> this </keyword>\n'
                +  '            </term>\n'
                +  '          </expression>\n'                
                +  '          <symbol> ; </symbol>\n'
                +  '        </returnStatement>\n'                
                +  '      </statements>\n'                 
              
                +  '      <symbol> } </symbol>\n'                  
                +  '    </subroutineBody>\n'              
                +  '  </subroutineDec>\n'                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')               

        #print(self.compile) 
        #print(self.compile.get_print_var_table())         
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result) 

    def test_subroutine_do(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_do.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_do_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n' 
                +  '  <classVarDec>\n'
                +  '    <keyword> field </keyword>\n'
                +  '    <keyword> int </keyword>\n'
                +  '    <identifier kind="field" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '    <symbol> ; </symbol>\n'
                +  '  </classVarDec>\n'                
                +  '  <subroutineDec>\n'
                +  '    <keyword> method </keyword>\n'
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="1" assigned="false"> Ax </identifier>\n'
                +  '      <symbol> , </symbol>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="2" assigned="false"> Ay </identifier>\n'
                +  '    </parameterList>\n'  
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'
                +  '      <symbol> { </symbol>\n'
                +  '      <varDec>\n'                
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="0" assigned="false"> y </identifier>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </varDec>\n' 
                +  '      <statements>\n'                
                
                +  '        <doStatement>\n'
                +  '          <keyword> do </keyword>\n'
                +  '          <identifier kind="subroutine"> draw </identifier>\n'
                +  '          <symbol> ( </symbol>\n'
                +  '          <expressionList>\n'
                +  '          </expressionList>\n'
                +  '          <symbol> ) </symbol>\n'
                +  '          <symbol> ; </symbol>\n'
                +  '        </doStatement>\n' 

                +  '        <doStatement>\n'
                +  '          <keyword> do </keyword>\n'
                +  '          <identifier kind="subroutine"> Screen </identifier>\n'
                +  '          <symbol> . </symbol>\n'
                +  '          <identifier kind="subroutine"> drawRectangle </identifier>\n'
                +  '          <symbol> ( </symbol>\n'
                +  '          <expressionList>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier kind="field" type="int" index="0" assigned="true"> x </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> , </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> , </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier kind="field" type="int" index="0" assigned="true"> x </identifier>\n'
                +  '              </term>\n'
                +  '              <symbol> + </symbol>\n'
                +  '              <term>\n'
                +  '                <identifier kind="argument" type="int" index="1" assigned="true"> Ax </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '            <symbol> , </symbol>\n'
                +  '            <expression>\n'
                +  '              <term>\n'
                +  '                <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '              </term>\n'
                +  '              <symbol> + </symbol>\n'
                +  '              <term>\n'
                +  '                <identifier kind="argument" type="int" index="2" assigned="true"> Ay </identifier>\n'
                +  '              </term>\n'
                +  '            </expression>\n'
                +  '          </expressionList>\n'
                +  '          <symbol> ) </symbol>\n'
                +  '          <symbol> ; </symbol>\n'
                +  '        </doStatement>\n'                
              
                +  '      </statements>\n'              
                +  '      <symbol> } </symbol>\n'                  
                +  '    </subroutineBody>\n'              
                +  '  </subroutineDec>\n'                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')               

        #print(self.compile) 
        #print(self.compile.get_print_var_table())         
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)   

    def test_subroutine_if(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_if.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_if_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'               
                +  '  <subroutineDec>\n'
                +  '    <keyword> function </keyword>\n'
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '    </parameterList>\n'  
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'
                +  '      <symbol> { </symbol>\n'
                +  '      <varDec>\n'                
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="0" assigned="false"> y </identifier>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </varDec>\n' 
                +  '      <statements>\n'               
                
                +  '        <ifStatement>\n' 
                +  '          <keyword> if </keyword>\n' 
                +  '          <symbol> ( </symbol>\n' 
                +  '          <expression>\n' 
                +  '            <term>\n' 
                +  '              <identifier kind="argument" type="int" index="0" assigned="true"> x </identifier>\n' 
                +  '            </term>\n' 
                +  '            <symbol> &gt; </symbol>\n' 
                +  '            <term>\n' 
                +  '              <integerConstant> 1 </integerConstant>\n' 
                +  '            </term>\n' 
                +  '          </expression>\n' 
                +  '          <symbol> ) </symbol>\n' 
                +  '          <symbol> { </symbol>\n' 
                +  '          <statements>\n' 

                +  '            <letStatement>\n'
                +  '              <keyword> let </keyword>\n'
                +  '              <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '              <symbol> = </symbol>\n'
                +  '              <expression>\n'
                +  '                <term>\n'
                +  '                  <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '                </term>\n'
                +  '                <symbol> - </symbol>\n'
                +  '                <term>\n'
                +  '                  <integerConstant> 2 </integerConstant>\n'
                +  '                </term>\n'
                +  '              </expression>\n'
                +  '              <symbol> ; </symbol>\n'
                +  '            </letStatement>\n'
                
                +  '          </statements>\n' 
                +  '          <symbol> } </symbol>\n'
                +  '        </ifStatement>\n'     
                
                +  '      </statements>\n'                
                +  '      <symbol> } </symbol>\n'                  
                +  '    </subroutineBody>\n'              
                +  '  </subroutineDec>\n'                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')               

        #print(self.compile) 
        #print(self.compile.get_print_var_table())         
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result) 

    def test_subroutine_while(self):    
        self.compile = compilation_engine_xml_vars.CompilationEngine('./data_test_snippets_xml/Square_subroutine_while.jack', 
                                                                './data_test_snippets_xml/Square_subroutine_while_VARS.xml', 
                                                                test=True)
                                                                 
        self.compile.compile_class()
        result = self.compile._xml 
        compare = ('<class>\n'
                +  '  <keyword> class </keyword>\n'
                +  '  <identifier kind="class"> Square </identifier>\n'
                +  '  <symbol> { </symbol>\n'               
                +  '  <subroutineDec>\n'
                +  '    <keyword> function </keyword>\n'
                +  '    <keyword> void </keyword>\n'
                +  '    <identifier kind="subroutine"> draw </identifier>\n'
                +  '    <symbol> ( </symbol>\n'
                +  '    <parameterList>\n'
                +  '      <keyword> int </keyword>\n'
                +  '      <identifier kind="argument" type="int" index="0" assigned="false"> x </identifier>\n'
                +  '    </parameterList>\n'  
                +  '    <symbol> ) </symbol>\n'
                +  '    <subroutineBody>\n'
                +  '      <symbol> { </symbol>\n'
                +  '      <varDec>\n'                
                +  '        <keyword> var </keyword>\n'
                +  '        <keyword> int </keyword>\n'
                +  '        <identifier kind="var" type="int" index="0" assigned="false"> y </identifier>\n'
                +  '        <symbol> ; </symbol>\n' 
                +  '      </varDec>\n' 
                +  '      <statements>\n'               
                
                +  '        <whileStatement>\n' 
                +  '          <keyword> while </keyword>\n' 
                +  '          <symbol> ( </symbol>\n' 
                +  '          <expression>\n' 
                +  '            <term>\n' 
                +  '              <identifier kind="argument" type="int" index="0" assigned="true"> x </identifier>\n' 
                +  '            </term>\n' 
                +  '            <symbol> &gt; </symbol>\n' 
                +  '            <term>\n' 
                +  '              <integerConstant> 1 </integerConstant>\n' 
                +  '            </term>\n' 
                +  '          </expression>\n' 
                +  '          <symbol> ) </symbol>\n' 
                +  '          <symbol> { </symbol>\n' 
                +  '          <statements>\n' 

                +  '            <letStatement>\n'
                +  '              <keyword> let </keyword>\n'
                +  '              <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '              <symbol> = </symbol>\n'
                +  '              <expression>\n'
                +  '                <term>\n'
                +  '                  <identifier kind="var" type="int" index="0" assigned="true"> y </identifier>\n'
                +  '                </term>\n'
                +  '                <symbol> - </symbol>\n'
                +  '                <term>\n'
                +  '                  <integerConstant> 2 </integerConstant>\n'
                +  '                </term>\n'
                +  '              </expression>\n'
                +  '              <symbol> ; </symbol>\n'
                +  '            </letStatement>\n'
                
                +  '          </statements>\n' 
                +  '          <symbol> } </symbol>\n'
                +  '        </whileStatement>\n'     
                
                +  '      </statements>\n'                
                +  '      <symbol> } </symbol>\n'                  
                +  '    </subroutineBody>\n'              
                +  '  </subroutineDec>\n'                
                +  '  <symbol> } </symbol>\n'
                +  '</class>\n')               

        #print(self.compile) 
        #print(self.compile.get_print_var_table())         
        #print(compare)        
        #print(result) 
        self.assertEqual(compare, result)         
 
if __name__=='__main__':
    unittest.main()