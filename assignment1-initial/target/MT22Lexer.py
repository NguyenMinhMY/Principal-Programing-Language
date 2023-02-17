# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\7\2\u0080\n\2\f\2\16")
        buf.write("\2\u0083\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3")
        buf.write("\u008e\n\3\f\3\16\3\u0091\13\3\3\3\3\3\3\4\6\4\u0096\n")
        buf.write("\4\r\4\16\4\u0097\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u0146\n\61\3\62\3\62\7\62\u014a\n\62\f\62\16")
        buf.write("\62\u014d\13\62\3\62\3\62\6\62\u0151\n\62\r\62\16\62\u0152")
        buf.write("\7\62\u0155\n\62\f\62\16\62\u0158\13\62\3\62\3\62\5\62")
        buf.write("\u015c\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u0163\n\63\3")
        buf.write("\63\3\63\5\63\u0167\n\63\3\64\3\64\7\64\u016b\n\64\f\64")
        buf.write("\16\64\u016e\13\64\3\65\3\65\5\65\u0172\n\65\3\65\6\65")
        buf.write("\u0175\n\65\r\65\16\65\u0176\3\66\3\66\5\66\u017b\n\66")
        buf.write("\3\67\3\67\3\67\7\67\u0180\n\67\f\67\16\67\u0183\13\67")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\39\39\79\u018f\n9\f9\16")
        buf.write("9\u0192\139\39\39\39\79\u0197\n9\f9\169\u019a\139\39\3")
        buf.write("9\39\79\u019f\n9\f9\169\u01a2\139\39\39\39\79\u01a7\n")
        buf.write("9\f9\169\u01aa\139\39\39\59\u01ae\n9\3:\3:\7:\u01b2\n")
        buf.write(":\f:\16:\u01b5\13:\3;\3;\3;\3<\3<\3=\3=\3\u0081\2>\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\2i\2k\65m\66o\2q\67s8")
        buf.write("u9w:y;\3\2\f\4\2\f\f\17\17\5\2\n\f\16\17\"\"\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\t\2$$^^ddhhp")
        buf.write("pttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u01d4\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\3{\3\2\2\2\5\u0089\3\2\2\2\7\u0095\3\2\2\2\t\u009b")
        buf.write("\3\2\2\2\13\u00a0\3\2\2\2\r\u00a6\3\2\2\2\17\u00ae\3\2")
        buf.write("\2\2\21\u00b1\3\2\2\2\23\u00b6\3\2\2\2\25\u00bc\3\2\2")
        buf.write("\2\27\u00c2\3\2\2\2\31\u00c6\3\2\2\2\33\u00cf\3\2\2\2")
        buf.write("\35\u00d7\3\2\2\2\37\u00de\3\2\2\2!\u00e5\3\2\2\2#\u00ea")
        buf.write("\3\2\2\2%\u00ef\3\2\2\2\'\u00f3\3\2\2\2)\u00fc\3\2\2\2")
        buf.write("+\u00ff\3\2\2\2-\u0105\3\2\2\2/\u0107\3\2\2\2\61\u0109")
        buf.write("\3\2\2\2\63\u010b\3\2\2\2\65\u010d\3\2\2\2\67\u010f\3")
        buf.write("\2\2\29\u0111\3\2\2\2;\u0114\3\2\2\2=\u0117\3\2\2\2?\u011a")
        buf.write("\3\2\2\2A\u011d\3\2\2\2C\u011f\3\2\2\2E\u0122\3\2\2\2")
        buf.write("G\u0124\3\2\2\2I\u0127\3\2\2\2K\u012a\3\2\2\2M\u012c\3")
        buf.write("\2\2\2O\u012e\3\2\2\2Q\u0130\3\2\2\2S\u0132\3\2\2\2U\u0134")
        buf.write("\3\2\2\2W\u0136\3\2\2\2Y\u0138\3\2\2\2[\u013a\3\2\2\2")
        buf.write("]\u013c\3\2\2\2_\u013e\3\2\2\2a\u0145\3\2\2\2c\u015b\3")
        buf.write("\2\2\2e\u0166\3\2\2\2g\u0168\3\2\2\2i\u016f\3\2\2\2k\u017a")
        buf.write("\3\2\2\2m\u017c\3\2\2\2o\u0187\3\2\2\2q\u01ad\3\2\2\2")
        buf.write("s\u01af\3\2\2\2u\u01b6\3\2\2\2w\u01b9\3\2\2\2y\u01bb\3")
        buf.write("\2\2\2{|\7\61\2\2|}\7,\2\2}\u0081\3\2\2\2~\u0080\13\2")
        buf.write("\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0081\177\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\7,\2\2\u0085\u0086\7\61\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\b\2\2\2\u0088\4\3\2\2\2\u0089")
        buf.write("\u008a\7\61\2\2\u008a\u008b\7\61\2\2\u008b\u008f\3\2\2")
        buf.write("\2\u008c\u008e\n\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\b\3\2\2")
        buf.write("\u0093\6\3\2\2\2\u0094\u0096\t\3\2\2\u0095\u0094\3\2\2")
        buf.write("\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\4\2\2\u009a")
        buf.write("\b\3\2\2\2\u009b\u009c\7c\2\2\u009c\u009d\7w\2\2\u009d")
        buf.write("\u009e\7v\2\2\u009e\u009f\7q\2\2\u009f\n\3\2\2\2\u00a0")
        buf.write("\u00a1\7d\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7c\2\2\u00a4\u00a5\7m\2\2\u00a5\f\3\2\2\2\u00a6")
        buf.write("\u00a7\7d\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7q\2\2\u00a9")
        buf.write("\u00aa\7n\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\16\3\2\2\2\u00ae\u00af\7f\2\2\u00af")
        buf.write("\u00b0\7q\2\2\u00b0\20\3\2\2\2\u00b1\u00b2\7g\2\2\u00b2")
        buf.write("\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\22\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8\7c\2\2\u00b8")
        buf.write("\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\24\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be\7n\2\2\u00be")
        buf.write("\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7v\2\2\u00c1")
        buf.write("\26\3\2\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4\7q\2\2\u00c4")
        buf.write("\u00c5\7t\2\2\u00c5\30\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7")
        buf.write("\u00c8\7w\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7e\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\u00d4\7i\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\34\3\2\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\u00da\7v\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\36\3\2\2\2\u00de\u00df\7u\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4 \3\2\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7w\2\2\u00e8")
        buf.write("\u00e9\7g\2\2\u00e9\"\3\2\2\2\u00ea\u00eb\7x\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7f\2\2\u00ee")
        buf.write("$\3\2\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7w\2\2\u00f1")
        buf.write("\u00f2\7v\2\2\u00f2&\3\2\2\2\u00f3\u00f4\7e\2\2\u00f4")
        buf.write("\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7v\2\2\u00f7")
        buf.write("\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7w\2\2\u00fa")
        buf.write("\u00fb\7g\2\2\u00fb(\3\2\2\2\u00fc\u00fd\7q\2\2\u00fd")
        buf.write("\u00fe\7h\2\2\u00fe*\3\2\2\2\u00ff\u0100\7c\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7t\2\2\u0102\u0103\7c\2\2\u0103")
        buf.write("\u0104\7{\2\2\u0104,\3\2\2\2\u0105\u0106\7-\2\2\u0106")
        buf.write(".\3\2\2\2\u0107\u0108\7/\2\2\u0108\60\3\2\2\2\u0109\u010a")
        buf.write("\7,\2\2\u010a\62\3\2\2\2\u010b\u010c\7\61\2\2\u010c\64")
        buf.write("\3\2\2\2\u010d\u010e\7\'\2\2\u010e\66\3\2\2\2\u010f\u0110")
        buf.write("\7#\2\2\u01108\3\2\2\2\u0111\u0112\7(\2\2\u0112\u0113")
        buf.write("\7(\2\2\u0113:\3\2\2\2\u0114\u0115\7~\2\2\u0115\u0116")
        buf.write("\7~\2\2\u0116<\3\2\2\2\u0117\u0118\7?\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119>\3\2\2\2\u011a\u011b\7#\2\2\u011b\u011c")
        buf.write("\7?\2\2\u011c@\3\2\2\2\u011d\u011e\7>\2\2\u011eB\3\2\2")
        buf.write("\2\u011f\u0120\7>\2\2\u0120\u0121\7?\2\2\u0121D\3\2\2")
        buf.write("\2\u0122\u0123\7@\2\2\u0123F\3\2\2\2\u0124\u0125\7@\2")
        buf.write("\2\u0125\u0126\7?\2\2\u0126H\3\2\2\2\u0127\u0128\7<\2")
        buf.write("\2\u0128\u0129\7<\2\2\u0129J\3\2\2\2\u012a\u012b\7*\2")
        buf.write("\2\u012bL\3\2\2\2\u012c\u012d\7+\2\2\u012dN\3\2\2\2\u012e")
        buf.write("\u012f\7}\2\2\u012fP\3\2\2\2\u0130\u0131\7\177\2\2\u0131")
        buf.write("R\3\2\2\2\u0132\u0133\7]\2\2\u0133T\3\2\2\2\u0134\u0135")
        buf.write("\7_\2\2\u0135V\3\2\2\2\u0136\u0137\7\60\2\2\u0137X\3\2")
        buf.write("\2\2\u0138\u0139\7.\2\2\u0139Z\3\2\2\2\u013a\u013b\7=")
        buf.write("\2\2\u013b\\\3\2\2\2\u013c\u013d\7<\2\2\u013d^\3\2\2\2")
        buf.write("\u013e\u013f\7?\2\2\u013f`\3\2\2\2\u0140\u0146\5c\62\2")
        buf.write("\u0141\u0146\5e\63\2\u0142\u0146\5k\66\2\u0143\u0146\5")
        buf.write("m\67\2\u0144\u0146\5q9\2\u0145\u0140\3\2\2\2\u0145\u0141")
        buf.write("\3\2\2\2\u0145\u0142\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146b\3\2\2\2\u0147\u014b\t\4\2\2\u0148")
        buf.write("\u014a\t\5\2\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u0156\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014e\u0150\7a\2\2\u014f\u0151")
        buf.write("\t\5\2\2\u0150\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u014e\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u015c\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0159\u015a\7\62\2\2\u015a\u015c\b\62\3\2\u015b")
        buf.write("\u0147\3\2\2\2\u015b\u0159\3\2\2\2\u015cd\3\2\2\2\u015d")
        buf.write("\u015e\5c\62\2\u015e\u015f\5g\64\2\u015f\u0167\3\2\2\2")
        buf.write("\u0160\u0162\5c\62\2\u0161\u0163\5g\64\2\u0162\u0161\3")
        buf.write("\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\5i\65\2\u0165\u0167\3\2\2\2\u0166\u015d\3\2\2\2\u0166")
        buf.write("\u0160\3\2\2\2\u0167f\3\2\2\2\u0168\u016c\7\60\2\2\u0169")
        buf.write("\u016b\t\5\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dh\3\2\2")
        buf.write("\2\u016e\u016c\3\2\2\2\u016f\u0171\t\6\2\2\u0170\u0172")
        buf.write("\t\7\2\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0174\3\2\2\2\u0173\u0175\t\5\2\2\u0174\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177j\3\2\2\2\u0178\u017b\5!\21\2\u0179\u017b")
        buf.write("\5\23\n\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("l\3\2\2\2\u017c\u0181\7$\2\2\u017d\u0180\5o8\2\u017e\u0180")
        buf.write("\n\b\2\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\7")
        buf.write("$\2\2\u0185\u0186\b\67\4\2\u0186n\3\2\2\2\u0187\u0188")
        buf.write("\7^\2\2\u0188\u0189\t\t\2\2\u0189p\3\2\2\2\u018a\u018b")
        buf.write("\7}\2\2\u018b\u0190\5c\62\2\u018c\u018d\7.\2\2\u018d\u018f")
        buf.write("\5c\62\2\u018e\u018c\3\2\2\2\u018f\u0192\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u01ae\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0193\u0198\5e\63\2\u0194\u0195\7")
        buf.write(".\2\2\u0195\u0197\5e\63\2\u0196\u0194\3\2\2\2\u0197\u019a")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u01ae\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u01a0\5k\66\2")
        buf.write("\u019c\u019d\7.\2\2\u019d\u019f\5k\66\2\u019e\u019c\3")
        buf.write("\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u01ae\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a8\5m\67\2\u01a4\u01a5\7.\2\2\u01a5\u01a7\5m\67\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\7\177\2\2\u01ac\u01ae\3\2\2\2\u01ad")
        buf.write("\u018a\3\2\2\2\u01ad\u0193\3\2\2\2\u01ad\u019b\3\2\2\2")
        buf.write("\u01ad\u01a3\3\2\2\2\u01aer\3\2\2\2\u01af\u01b3\t\n\2")
        buf.write("\2\u01b0\u01b2\t\13\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("t\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\13\2\2\2\u01b7")
        buf.write("\u01b8\b;\5\2\u01b8v\3\2\2\2\u01b9\u01ba\13\2\2\2\u01ba")
        buf.write("x\3\2\2\2\u01bb\u01bc\13\2\2\2\u01bcz\3\2\2\2\31\2\u0081")
        buf.write("\u008f\u0097\u0145\u014b\u0152\u0156\u015b\u0162\u0166")
        buf.write("\u016c\u0171\u0176\u017a\u017f\u0181\u0190\u0198\u01a0")
        buf.write("\u01a8\u01ad\u01b3\6\b\2\2\3\62\2\3\67\3\3;\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCKCOM = 1
    LINECOM = 2
    WS = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FALSE = 9
    FLOAT = 10
    FOR = 11
    FUNCTION = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    ARRAY = 21
    PLUS = 22
    MINUS = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQ = 30
    NOT_EQ = 31
    LT = 32
    LT_EQ = 33
    GT = 34
    GT_EQ = 35
    CONCAT = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMI = 45
    COLON = 46
    ASSIGN = 47
    LIT = 48
    INTLIT = 49
    FLOATLIT = 50
    BOOLLIT = 51
    STRINGLIT = 52
    ARRAYLIT = 53
    ID = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'integer'", "'return'", "'string'", 
            "'true'", "'void'", "'out'", "'continue'", "'of'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'{'", "'}'", "'['", "']'", "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOM", "LINECOM", "WS", "AUTO", "BREAK", "BOOLEAN", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "INTEGER", "RETURN", 
            "STRING", "TRUE", "VOID", "OUT", "CONTINUE", "OF", "ARRAY", 
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
            "NOT_EQ", "LT", "LT_EQ", "GT", "GT_EQ", "CONCAT", "LB", "RB", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", 
            "LIT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ARRAYLIT", 
            "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCKCOM", "LINECOM", "WS", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "VOID", "OUT", "CONTINUE", 
                  "OF", "ARRAY", "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQ", "NOT_EQ", "LT", "LT_EQ", "GT", "GT_EQ", 
                  "CONCAT", "LB", "RB", "LP", "RP", "LSB", "RSB", "DOT", 
                  "COMMA", "SEMI", "COLON", "ASSIGN", "LIT", "INTLIT", "FLOATLIT", 
                  "DECPART", "EXPPART", "BOOLLIT", "STRINGLIT", "ESC", "ARRAYLIT", 
                  "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.INTLIT_action 
            actions[53] = self.STRINGLIT_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


