%{
#include <stdio.h>
#include <math.h>

void yyerror(const char *msg);
int yylex();

// traduccion exacta del codigo Python que dieron
double raiz_cuadrada(double a) {
    double tolerancia = 1e-10;
    int max_iter = 1000;
    double x = a / 2;  // estimacion inicial

    for (int i = 0; i < max_iter; i++) {
        double x_nuevo = 0.5 * (x + a / x);

        if (x_nuevo - x < tolerancia && x - x_nuevo < tolerancia)
            return x_nuevo;

        x = x_nuevo;
    }
    return x;
}
%}

%union {
    double real;
}

%token <real> NUMERO
%token SQRT LPAREN RPAREN FIN
%type  <real> expresion

%%

programa:
    programa linea
    | linea
;

linea:
    expresion FIN  { printf("Raiz aproximada: %f\n", $1); }
    | FIN
;

expresion:
    NUMERO                          { $$ = $1; }
    | SQRT LPAREN expresion RPAREN  { $$ = raiz_cuadrada($3); }
;

%%

void yyerror(const char *msg) {
    printf("error: %s\n", msg);
}

int main() {
    yyparse();
    return 0;
}

