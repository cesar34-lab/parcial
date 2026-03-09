from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from FiboVisitor import FiboVisitor

# visitor que procesa la instruccion FIBO(n)
class MiFiboVisitor(FiboVisitor):

    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)

    def visitInstruccion(self, ctx):
        n = int(ctx.NUMERO().getText())
        resultado = self.calcular_fibo(n)
        print(f"FIBO({n}) =", ", ".join(map(str, resultado)))

    # funcion recursiva de fibonacci
    def calcular_fibo(self, n):
        secuencia = []
        for i in range(n):
            secuencia.append(self.fibo(i))
        return secuencia

    def fibo(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibo(n - 1) + self.fibo(n - 2)
