grammar Fibo;

// regla principal
programa : instruccion EOF ;

instruccion : 'FIBO' '(' NUMERO ')' ;

// token numero
NUMERO : [0-9]+ ;

// ignorar espacios
WS : [ \t\n\r]+ -> skip ;
