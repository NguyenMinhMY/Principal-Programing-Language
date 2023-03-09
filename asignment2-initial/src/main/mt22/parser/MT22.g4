// Nguyen Minh My 2013811
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF ;
decls: decl decls | decl;
decl: (var_decl|func_decl);

// Variable Declaration

var_decl: listID COLON var_type SEMI | var_init;
var_init: ID (COMMA recursive_decl|COLON var_type ASSIGN) expr SEMI;
recursive_decl: ID (COMMA recursive_decl|COLON var_type ASSIGN) expr COMMA;

// Function Declaration
func_decl: ID COLON FUNCTION return_type LB list_para? RB (INHERIT ID)? block_stmt;

// Parameter Declaration
list_para: para_decl COMMA list_para | para_decl;
para_decl: INHERIT? OUT? ID COLON var_type;

// Statements
stmt: assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| cont_stmt
	| return_stmt
	| call_stmt
	| block_stmt
	| var_decl;
assign_stmt: lhs ASSIGN expr SEMI;
lhs : ID LSB list_expr RSB | ID;
if_stmt : IF LB expr RB stmt (ELSE stmt)?;
for_stmt: FOR LB (ID ASSIGN expr ) COMMA expr COMMA expr RB (stmt);
while_stmt: WHILE LB expr RB (stmt);
do_while_stmt: DO block_stmt WHILE LB expr RB SEMI;
break_stmt: BREAK SEMI;
cont_stmt: CONTINUE SEMI;
return_stmt: RETURN expr? SEMI;
call_stmt: func_call SEMI;
block_stmt: LP (stmt)* RP;

// Expression
expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQ | NOT_EQ | LT | GT | LT_EQ | GT_EQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: ID LSB list_expr RSB | expr8;
expr8: LB expr RB | ID | func_call | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | array_lit;

// Function Call
func_call: ID LB list_expr? RB | special_func;

// Special functions
special_func: 'readInteger' LB RB
			| 'printInteger' LB expr RB
			| 'readFloat' LB RB
			| 'printBoolean' LB expr RB
			| 'readString' LB RB
			| 'printString' LB expr RB
			| 'super' LB list_expr RB
			| 'preventDefault' LB RB;
list_expr: expr COMMA list_expr | expr;

// Literals

INTLIT: '0' | [1-9][0-9]* ('_'[0-9]+)* {
self.text = self.text.replace("_", "");
};

FLOATLIT: INTLIT DECPART EXPPART {
self.text = self.text.replace("_", "");
} | INTLIT DECPART {
self.text = self.text.replace("_", "");
}| INTLIT EXPPART  {
self.text = self.text.replace("_", "");
}| DECPART EXPPART;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLLIT: TRUE | FALSE;

STRINGLIT :'"' (ESC | ~[\n\\"] )* '"' {self.text = self.text[1:-1]};
fragment ESC: '\\' ['"\\bfnrt];

array_lit: LP (list_expr|) RP;

// Types
// Array type declaration
arr_typ_decl: ARRAY LSB listInt RSB OF elementType;
return_type: var_type | VOID;
var_type: elementType |arr_typ_decl| AUTO ;
elementType: BOOLEAN | INTEGER | FLOAT | STRING;

// List
listInt: INTLIT COMMA listInt | INTLIT;
listID: ID COMMA listID | ID;

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
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
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
// Identifiers
ID: [a-zA-Z_][a-zA-Z_0-9]*;
UNCLOSE_STRING: '"' (ESC | ~[\n\\"] )* (EOF|'\n')
{
	text = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
	raise UncloseString(text)
};
ILLEGAL_ESCAPE: '"' (ESC | ~[\n\\"] )* '\\' ~[bfnrt'"\\]
{
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};