grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

program: decls;// write for program rule here using vardecl and funcdecl
decls: decl decls | decl;
decl: vardecl | funcdecl;
vardecl: typ idlist SEMI ;

funcdecl: typ ID para_decl body ;
para_decl: LB (typ idlist (SEMI typ idlist)*)? RB;

body : '{' stats '}';
stats: statement stats |;
statement: vardecl | assignment | call | re ;
assignment: ID '=' expr SEMI;
call: ID LB (expr (COMMA expr)*)? RB SEMI;
re: 'return' expr SEMI ;
expr: expr0 PLUS expr | expr0 ;
expr0: expr1 MINUS expr1 | expr1;
expr1: expr1 DIVIDE expr2 | expr1 MUL expr2 | expr2;
expr2: LB expr RB | ID | call | intlit | floatlit;
intlit: '-'? number+;
floatlit: intlit '.' number+;
number: ('0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9') ;
PLUS: '+';
MINUS: '-';
DIVIDE: '/';
MUL: '*';
SEMI: ';';
typ: 'int' | 'float';
idlist: ID COMMA idlist | ID;
COMMA: ',';
LB: '(';
RB: ')';
ID: [a-z]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;