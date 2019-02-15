# -*- coding: utf-8 -*- 

"""
The JackAnalyzer accepts a single command line parameter, Xxx or Xxx.jack, where either 
Xxx is a directory containing one more .jack files, or Xxx.jack is a file containing Jack code.

FROM compiler DIRECTORY:
-prompt> python JackAnalyzer.py Xxx
-prompt> python JackAnalyzer.py Xxx.jack
-prompt> python JackAnalyzer.py run_all

FROM Compiler root DIRECTORY, one level up from compiler:
-prompt> python -m compiler Xxx
-prompt> python -m compiler Xxx.jack
-prompt> python -m compiler run_all

The analyzer then parses the Xxx.jack file, or in case of a directory all .jacks files. A corresponding
Xxx.xml file for each .jack file is created and placed in the same directory as the .jack file/s.  
"""

import os, sys, ntpath 

if os.getcwd().endswith('Compiler'):
    from compiler import compilation_engine_xml
    
else:
    import compilation_engine_xml
    
    
def parse_file(file, file_full_path, writer):
    """
    Accepts name of .jack code file and returns xml 
    """
    
    pass  
    

def parse(arg):
    """
    Checks command argument to see if its a directory of .jack files or just one .jack file.
    Writes corresponding .xml file for each .jack file, and saves to the same directory as the .jack file/s.
    """

    #get directory or file from arg and, if on Windows, convert to back slashes
    print('\nUser input: \n\t' + arg)
    to_translate = arg.strip()  
    to_translate = os.path.abspath(to_translate)
    
    if os.path.isdir(to_translate):
        print('\nParsing .jack files in directory: \n\t' + to_translate)
        
        for root, dirs, files in os.walk(to_translate):
            for file in files:
                if file.endswith('.jack'):
                    file_full_path = os.path.join(root, file)
                    file_to_write = file_full_path.replace('.jack', '.xml')
                    compilation_engine_xml.CompilationEngine(file_full_path, file_to_write)
        
    else:
        print('\nParsing file: \n\t' + to_translate)
        to_write = to_translate.replace('.jack', '.xml')
        compilation_engine_xml.CompilationEngine(to_translate, to_write)
    
    print('\nParsing completed')  
    print('\n----------------------------------------------------------------------')   
    
def main():
    """
    Checks whether arg is run_all, or a file or directory.
    If run_all, then walks through data directory to parse all .jack files and directories.    
    """
    
    if sys.argv[1] == 'run_all':
        if os.getcwd().endswith('Compiler'):
            start_directory = 'data/'
        else:
            start_directory = '../data/'   
            
        for root, dirs, files in os.walk(start_directory):
            for file in files:
                if file.endswith('.jack'):
                    fname = os.path.join(root, file)
                    parse(fname)                    
            for dir in dirs:
                dname = os.path.join(root, dir)
                parse(dname)                     
        
    else:
        parse(sys.argv[1])
    
if __name__ == '__main__':
    main()   