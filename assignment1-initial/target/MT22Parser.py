# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'false'", "'float'", "'for'", "'function'", "'integer'", 
                     "'return'", "'string'", "'true'", "'void'", "'out'", 
                     "'continue'", "'of'", "'array'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "BLOCKCOM", "LINECOM", "WS", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                      "FOR", "FUNCTION", "INTEGER", "RETURN", "STRING", 
                      "TRUE", "VOID", "OUT", "CONTINUE", "OF", "ARRAY", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", 
                      "OR", "EQ", "NOT_EQ", "LT", "LT_EQ", "GT", "GT_EQ", 
                      "CONCAT", "LB", "RB", "LP", "RP", "LSB", "RSB", "DOT", 
                      "COMMA", "SEMI", "COLON", "ASSIGN", "LIT", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", "ID", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BLOCKCOM=1
    LINECOM=2
    WS=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FALSE=9
    FLOAT=10
    FOR=11
    FUNCTION=12
    INTEGER=13
    RETURN=14
    STRING=15
    TRUE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    ARRAY=21
    PLUS=22
    MINUS=23
    MUL=24
    DIV=25
    MOD=26
    NOT=27
    AND=28
    OR=29
    EQ=30
    NOT_EQ=31
    LT=32
    LT_EQ=33
    GT=34
    GT_EQ=35
    CONCAT=36
    LB=37
    RB=38
    LP=39
    RP=40
    LSB=41
    RSB=42
    DOT=43
    COMMA=44
    SEMI=45
    COLON=46
    ASSIGN=47
    LIT=48
    INTLIT=49
    FLOATLIT=50
    BOOLLIT=51
    STRINGLIT=52
    ARRAYLIT=53
    ID=54
    ERROR_CHAR=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





