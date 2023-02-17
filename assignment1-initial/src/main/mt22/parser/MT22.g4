// Nguyen Minh My 2013811
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

// Comments
BLOCKCOM: '/*' .*? '*/' -> skip;
LINECOM: '//'  (~[\r\n])* -> skip;
WS :  [ \t\b\f\r\n]+ -> skip ; // skip whitespace charaters

// Keywords
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
ARRAY: 'array';

// Operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';

LT: '<';
LT_EQ: '<=';
GT: '>';
GT_EQ: '>=';
CONCAT: '::';

// Seperator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
ASSIGN: '=';


// Literals

LIT: INTLIT|FLOATLIT|BOOLLIT|STRINGLIT|ARRAYLIT;

INTLIT: [1-9][0-9]* ('_'[0-9]+)*| '0' {self.text = self.text.replace('_','')};

FLOATLIT: INTLIT DECPART | INTLIT DECPART? EXPPART;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLLIT: TRUE | FALSE;

STRINGLIT :'"' (ESC | ~[\b\t\f\r\n\\"] )* '"'
{
    self.text = self.text[1:-1]
};
fragment ESC: '\\' ["\\bfnrt];

ARRAYLIT: '{' INTLIT (',' INTLIT) *
		| FLOATLIT (',' FLOATLIT)*
		| BOOLLIT (',' BOOLLIT)*
		| STRINGLIT (',' STRINGLIT)* '}'; 



// Identifiers

ID: [a-zA-Z_][a-zA-Z_0-9]*;




ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;