import unittest

import nltk
from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame

from Parser.rd_parser import RDParser
from nltk.tree import *
from Scanner.scanner import Scanner

import traceback


def draw_nltk_tree(tree):
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(), tree)
    cf.add_widget(tc, 10, 10)
    cf.print_to_file('tree.ps')
    cf.destroy()
    nltk.draw.tree.draw_trees(tree)


class ParserTest(unittest.TestCase):
    def test_one_statement(self):
        source_code = "program test; begin x := 1+3*2; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")



    def test_two_statements(self):
        source_code = "program test; begin a := b + c; x := y - z; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")


    def test_if_statement(self):
        source_code = "program test; begin if a = b then x := y + z; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

    def test_if_else_statement(self):
        source_code = "program test; begin if a = b then x := y + z; else x := y - z; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

    def test_repeat_statement(self):
        source_code = "program test; begin repeat x := y + z; until x = 0; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

    def test_variable_declaration(self):
        source_code = "program test; var x: integer; begin x := 10; end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

    def test_procedure_declaration(self):
        source_code = "program test; procedure PrintHello(); begin writeln('Hello, World!'); end; begin PrintHello(); end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            #print(f"Exception occurred during parsing: {e}")
            #get traceback info
            traceback.print_exc()

    def test_function_declaration(self):
        source_code = "program test; function CalculateSum(a: integer , b: integer): integer; begin result := a + b; end; begin writeln(CalculateSum(2, 3)); end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

    def test_empty_block(self):
        source_code = "program test; begin end."
        scanner = Scanner()
        tokens = scanner.scan(source_code)
        parser = RDParser(tokens)
        try:
            result = parser.parse()
            draw_nltk_tree(result)
            result.pretty_print()
        except Exception as e:
            print(f"Exception occurred during parsing: {e}")

if __name__ == '__main__':
    unittest.main()
