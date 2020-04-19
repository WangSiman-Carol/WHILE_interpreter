#!/usr/bin/env python3

import sys
from lark import Lark
from interpreter import *

def main():
    try:
        for text in sys.stdin:
                while_parser = Lark.open('WHILE.lark', parser='lalr')
                tree = while_parser.parse(text)
                print(tree)
                #print(tree.children[0].type)
                #print("output,  ", tree.children[0].children[0])
                interpreter = Interpreter(while_parser)
                result = interpreter.interpret(text)
                print(result, flush=True)              
    except OSError as err:
        print("OS error: {0}".format(err))
    except EOFError:
        print("EOF error.")
        raise

if __name__ == '__main__':
    main()
