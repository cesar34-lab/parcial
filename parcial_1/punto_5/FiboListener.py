# Generated from Fibo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FiboParser import FiboParser
else:
    from FiboParser import FiboParser

# This class defines a complete listener for a parse tree produced by FiboParser.
class FiboListener(ParseTreeListener):

    # Enter a parse tree produced by FiboParser#programa.
    def enterPrograma(self, ctx:FiboParser.ProgramaContext):
        pass

    # Exit a parse tree produced by FiboParser#programa.
    def exitPrograma(self, ctx:FiboParser.ProgramaContext):
        pass


    # Enter a parse tree produced by FiboParser#instruccion.
    def enterInstruccion(self, ctx:FiboParser.InstruccionContext):
        pass

    # Exit a parse tree produced by FiboParser#instruccion.
    def exitInstruccion(self, ctx:FiboParser.InstruccionContext):
        pass



del FiboParser