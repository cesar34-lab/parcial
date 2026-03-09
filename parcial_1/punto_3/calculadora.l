%{
#include "calculadora.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+(\.[0-9]+)?   { yylval.real = atof(yytext); return NUMERO; }
"sqrt"              { return SQRT; }
"("                 { return LPAREN; }
")"                 { return RPAREN; }
"\n"                { return FIN; }
[ \t]               { }
.                   { printf("caracter no reconocido: %s\n", yytext); }

%%

int yywrap() { return 1; }
