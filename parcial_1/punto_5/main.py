import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from fibo_visitor import MiFiboVisitor

def main():
    # entrada por consola
    entrada = input("Ingrese la instruccion: ")

    # convertir el texto en tokens
    stream = InputStream(entrada)
    lexer = FiboLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = FiboParser(tokens)

    # construir el arbol
    tree = parser.programa()

    # recorrer el arbol con el visitor
    visitor = MiFiboVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
