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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u022c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\7\n\u00ed\n\n\f\n\16\n\u00f0\13")
        buf.write("\n\3\n\3\n\6\n\u00f4\n\n\r\n\16\n\u00f5\7\n\u00f8\n\n")
        buf.write("\f\n\16\n\u00fb\13\n\3\n\5\n\u00fe\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u0110\n\13\3\f\3\f\7\f\u0114\n\f\f\f\16")
        buf.write("\f\u0117\13\f\3\r\3\r\5\r\u011b\n\r\3\r\6\r\u011e\n\r")
        buf.write("\r\r\16\r\u011f\3\16\3\16\5\16\u0124\n\16\3\17\3\17\3")
        buf.write("\17\7\17\u0129\n\17\f\17\16\17\u012c\13\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u0138\n\21")
        buf.write("\f\21\16\21\u013b\13\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u0146\n\22\f\22\16\22\u0149\13\22")
        buf.write("\3\22\3\22\3\23\6\23\u014e\n\23\r\23\16\23\u014f\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\7C\u020c")
        buf.write("\nC\fC\16C\u020f\13C\3D\3D\3D\7D\u0214\nD\fD\16D\u0217")
        buf.write("\13D\3D\5D\u021a\nD\3D\3D\3E\3E\3E\7E\u0221\nE\fE\16E")
        buf.write("\u0224\13E\3E\3E\3E\3E\3F\3F\3F\3\u0139\2G\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16")
        buf.write("\37\2!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65")
        buf.write("\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*")
        buf.write("Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}")
        buf.write("=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\3\2\r")
        buf.write("\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\n\2$$))^")
        buf.write("^ddhhppttvv\4\2\f\f\17\17\5\2\n\f\16\17\"\"\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\3\f\f\2\u023d\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0099\3\2\2\2\7\u00a6")
        buf.write("\3\2\2\2\t\u00b0\3\2\2\2\13\u00bd\3\2\2\2\r\u00c8\3\2")
        buf.write("\2\2\17\u00d4\3\2\2\2\21\u00da\3\2\2\2\23\u00fd\3\2\2")
        buf.write("\2\25\u010f\3\2\2\2\27\u0111\3\2\2\2\31\u0118\3\2\2\2")
        buf.write("\33\u0123\3\2\2\2\35\u0125\3\2\2\2\37\u0130\3\2\2\2!\u0133")
        buf.write("\3\2\2\2#\u0141\3\2\2\2%\u014d\3\2\2\2\'\u0153\3\2\2\2")
        buf.write(")\u0158\3\2\2\2+\u015e\3\2\2\2-\u0166\3\2\2\2/\u0169\3")
        buf.write("\2\2\2\61\u016e\3\2\2\2\63\u0174\3\2\2\2\65\u017a\3\2")
        buf.write("\2\2\67\u017e\3\2\2\29\u0187\3\2\2\2;\u018a\3\2\2\2=\u0192")
        buf.write("\3\2\2\2?\u0199\3\2\2\2A\u01a0\3\2\2\2C\u01a5\3\2\2\2")
        buf.write("E\u01ab\3\2\2\2G\u01b0\3\2\2\2I\u01b4\3\2\2\2K\u01bd\3")
        buf.write("\2\2\2M\u01c0\3\2\2\2O\u01c8\3\2\2\2Q\u01ce\3\2\2\2S\u01d0")
        buf.write("\3\2\2\2U\u01d2\3\2\2\2W\u01d4\3\2\2\2Y\u01d6\3\2\2\2")
        buf.write("[\u01d8\3\2\2\2]\u01da\3\2\2\2_\u01dd\3\2\2\2a\u01e0\3")
        buf.write("\2\2\2c\u01e3\3\2\2\2e\u01e6\3\2\2\2g\u01e8\3\2\2\2i\u01eb")
        buf.write("\3\2\2\2k\u01ed\3\2\2\2m\u01f0\3\2\2\2o\u01f3\3\2\2\2")
        buf.write("q\u01f5\3\2\2\2s\u01f7\3\2\2\2u\u01f9\3\2\2\2w\u01fb\3")
        buf.write("\2\2\2y\u01fd\3\2\2\2{\u01ff\3\2\2\2}\u0201\3\2\2\2\177")
        buf.write("\u0203\3\2\2\2\u0081\u0205\3\2\2\2\u0083\u0207\3\2\2\2")
        buf.write("\u0085\u0209\3\2\2\2\u0087\u0210\3\2\2\2\u0089\u021d\3")
        buf.write("\2\2\2\u008b\u0229\3\2\2\2\u008d\u008e\7t\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091\7f\2\2\u0091\u0092")
        buf.write("\7K\2\2\u0092\u0093\7p\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7i\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\4\3\2\2\2\u0099\u009a\7r\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7K\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7t\2\2\u00a5\6\3\2\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7f\2\2\u00aa\u00ab\7H\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad")
        buf.write("\7q\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7v\2\2\u00af\b")
        buf.write("\3\2\2\2\u00b0\u00b1\7r\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6")
        buf.write("\7D\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9")
        buf.write("\7n\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\n\3\2\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2")
        buf.write("\7U\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\f")
        buf.write("\3\2\2\2\u00c8\u00c9\7r\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7U\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7i\2\2\u00d3\16")
        buf.write("\3\2\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7r\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7t\2\2\u00d9\20")
        buf.write("\3\2\2\2\u00da\u00db\7r\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7x\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7F\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7w\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7v\2\2\u00e8\22")
        buf.write("\3\2\2\2\u00e9\u00fe\7\62\2\2\u00ea\u00ee\t\2\2\2\u00eb")
        buf.write("\u00ed\t\3\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f9\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f3\7a\2\2\u00f2\u00f4")
        buf.write("\t\3\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2")
        buf.write("\u00f7\u00f1\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fe\b\n\2\2\u00fd\u00e9\3\2\2\2\u00fd")
        buf.write("\u00ea\3\2\2\2\u00fe\24\3\2\2\2\u00ff\u0100\5\23\n\2\u0100")
        buf.write("\u0101\5\27\f\2\u0101\u0102\5\31\r\2\u0102\u0103\b\13")
        buf.write("\3\2\u0103\u0110\3\2\2\2\u0104\u0105\5\23\n\2\u0105\u0106")
        buf.write("\5\27\f\2\u0106\u0107\b\13\4\2\u0107\u0110\3\2\2\2\u0108")
        buf.write("\u0109\5\23\n\2\u0109\u010a\5\31\r\2\u010a\u010b\b\13")
        buf.write("\5\2\u010b\u0110\3\2\2\2\u010c\u010d\5\27\f\2\u010d\u010e")
        buf.write("\5\31\r\2\u010e\u0110\3\2\2\2\u010f\u00ff\3\2\2\2\u010f")
        buf.write("\u0104\3\2\2\2\u010f\u0108\3\2\2\2\u010f\u010c\3\2\2\2")
        buf.write("\u0110\26\3\2\2\2\u0111\u0115\7\60\2\2\u0112\u0114\t\3")
        buf.write("\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\30\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0118\u011a\t\4\2\2\u0119\u011b\t\5\2\2\u011a")
        buf.write("\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2")
        buf.write("\u011c\u011e\t\3\2\2\u011d\u011c\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\32")
        buf.write("\3\2\2\2\u0121\u0124\5A!\2\u0122\u0124\5\61\31\2\u0123")
        buf.write("\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\34\3\2\2\2\u0125")
        buf.write("\u012a\7$\2\2\u0126\u0129\5\37\20\2\u0127\u0129\n\6\2")
        buf.write("\2\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129\u012c")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012d\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e\7$\2\2")
        buf.write("\u012e\u012f\b\17\6\2\u012f\36\3\2\2\2\u0130\u0131\7^")
        buf.write("\2\2\u0131\u0132\t\7\2\2\u0132 \3\2\2\2\u0133\u0134\7")
        buf.write("\61\2\2\u0134\u0135\7,\2\2\u0135\u0139\3\2\2\2\u0136\u0138")
        buf.write("\13\2\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013c\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013d\7,\2\2\u013d\u013e\7")
        buf.write("\61\2\2\u013e\u013f\3\2\2\2\u013f\u0140\b\21\7\2\u0140")
        buf.write("\"\3\2\2\2\u0141\u0142\7\61\2\2\u0142\u0143\7\61\2\2\u0143")
        buf.write("\u0147\3\2\2\2\u0144\u0146\n\b\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3")
        buf.write("\2\2\2\u0148\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b")
        buf.write("\b\22\7\2\u014b$\3\2\2\2\u014c\u014e\t\t\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\b\23\7")
        buf.write("\2\u0152&\3\2\2\2\u0153\u0154\7c\2\2\u0154\u0155\7w\2")
        buf.write("\2\u0155\u0156\7v\2\2\u0156\u0157\7q\2\2\u0157(\3\2\2")
        buf.write("\2\u0158\u0159\7d\2\2\u0159\u015a\7t\2\2\u015a\u015b\7")
        buf.write("g\2\2\u015b\u015c\7c\2\2\u015c\u015d\7m\2\2\u015d*\3\2")
        buf.write("\2\2\u015e\u015f\7d\2\2\u015f\u0160\7q\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7n\2\2\u0162\u0163\7g\2\2\u0163\u0164")
        buf.write("\7c\2\2\u0164\u0165\7p\2\2\u0165,\3\2\2\2\u0166\u0167")
        buf.write("\7f\2\2\u0167\u0168\7q\2\2\u0168.\3\2\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016a\u016b\7n\2\2\u016b\u016c\7u\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d\60\3\2\2\2\u016e\u016f\7h\2\2\u016f\u0170")
        buf.write("\7c\2\2\u0170\u0171\7n\2\2\u0171\u0172\7u\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173\62\3\2\2\2\u0174\u0175\7h\2\2\u0175\u0176")
        buf.write("\7n\2\2\u0176\u0177\7q\2\2\u0177\u0178\7c\2\2\u0178\u0179")
        buf.write("\7v\2\2\u0179\64\3\2\2\2\u017a\u017b\7h\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7t\2\2\u017d\66\3\2\2\2\u017e\u017f")
        buf.write("\7h\2\2\u017f\u0180\7w\2\2\u0180\u0181\7p\2\2\u0181\u0182")
        buf.write("\7e\2\2\u0182\u0183\7v\2\2\u0183\u0184\7k\2\2\u0184\u0185")
        buf.write("\7q\2\2\u0185\u0186\7p\2\2\u01868\3\2\2\2\u0187\u0188")
        buf.write("\7k\2\2\u0188\u0189\7h\2\2\u0189:\3\2\2\2\u018a\u018b")
        buf.write("\7k\2\2\u018b\u018c\7p\2\2\u018c\u018d\7v\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7i\2\2\u018f\u0190\7g\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191<\3\2\2\2\u0192\u0193\7t\2\2\u0193\u0194")
        buf.write("\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196\7w\2\2\u0196\u0197")
        buf.write("\7t\2\2\u0197\u0198\7p\2\2\u0198>\3\2\2\2\u0199\u019a")
        buf.write("\7u\2\2\u019a\u019b\7v\2\2\u019b\u019c\7t\2\2\u019c\u019d")
        buf.write("\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f\7i\2\2\u019f@\3")
        buf.write("\2\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3")
        buf.write("\7w\2\2\u01a3\u01a4\7g\2\2\u01a4B\3\2\2\2\u01a5\u01a6")
        buf.write("\7y\2\2\u01a6\u01a7\7j\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9")
        buf.write("\7n\2\2\u01a9\u01aa\7g\2\2\u01aaD\3\2\2\2\u01ab\u01ac")
        buf.write("\7x\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae\7k\2\2\u01ae\u01af")
        buf.write("\7f\2\2\u01afF\3\2\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2")
        buf.write("\7w\2\2\u01b2\u01b3\7v\2\2\u01b3H\3\2\2\2\u01b4\u01b5")
        buf.write("\7e\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7\7p\2\2\u01b7\u01b8")
        buf.write("\7v\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb")
        buf.write("\7w\2\2\u01bb\u01bc\7g\2\2\u01bcJ\3\2\2\2\u01bd\u01be")
        buf.write("\7q\2\2\u01be\u01bf\7h\2\2\u01bfL\3\2\2\2\u01c0\u01c1")
        buf.write("\7k\2\2\u01c1\u01c2\7p\2\2\u01c2\u01c3\7j\2\2\u01c3\u01c4")
        buf.write("\7g\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7N\3\2\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca")
        buf.write("\7t\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd")
        buf.write("\7{\2\2\u01cdP\3\2\2\2\u01ce\u01cf\7-\2\2\u01cfR\3\2\2")
        buf.write("\2\u01d0\u01d1\7/\2\2\u01d1T\3\2\2\2\u01d2\u01d3\7,\2")
        buf.write("\2\u01d3V\3\2\2\2\u01d4\u01d5\7\61\2\2\u01d5X\3\2\2\2")
        buf.write("\u01d6\u01d7\7\'\2\2\u01d7Z\3\2\2\2\u01d8\u01d9\7#\2\2")
        buf.write("\u01d9\\\3\2\2\2\u01da\u01db\7(\2\2\u01db\u01dc\7(\2\2")
        buf.write("\u01dc^\3\2\2\2\u01dd\u01de\7~\2\2\u01de\u01df\7~\2\2")
        buf.write("\u01df`\3\2\2\2\u01e0\u01e1\7?\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2b\3\2\2\2\u01e3\u01e4\7#\2\2\u01e4\u01e5\7?\2\2")
        buf.write("\u01e5d\3\2\2\2\u01e6\u01e7\7>\2\2\u01e7f\3\2\2\2\u01e8")
        buf.write("\u01e9\7>\2\2\u01e9\u01ea\7?\2\2\u01eah\3\2\2\2\u01eb")
        buf.write("\u01ec\7@\2\2\u01ecj\3\2\2\2\u01ed\u01ee\7@\2\2\u01ee")
        buf.write("\u01ef\7?\2\2\u01efl\3\2\2\2\u01f0\u01f1\7<\2\2\u01f1")
        buf.write("\u01f2\7<\2\2\u01f2n\3\2\2\2\u01f3\u01f4\7*\2\2\u01f4")
        buf.write("p\3\2\2\2\u01f5\u01f6\7+\2\2\u01f6r\3\2\2\2\u01f7\u01f8")
        buf.write("\7}\2\2\u01f8t\3\2\2\2\u01f9\u01fa\7\177\2\2\u01fav\3")
        buf.write("\2\2\2\u01fb\u01fc\7]\2\2\u01fcx\3\2\2\2\u01fd\u01fe\7")
        buf.write("_\2\2\u01fez\3\2\2\2\u01ff\u0200\7\60\2\2\u0200|\3\2\2")
        buf.write("\2\u0201\u0202\7.\2\2\u0202~\3\2\2\2\u0203\u0204\7=\2")
        buf.write("\2\u0204\u0080\3\2\2\2\u0205\u0206\7<\2\2\u0206\u0082")
        buf.write("\3\2\2\2\u0207\u0208\7?\2\2\u0208\u0084\3\2\2\2\u0209")
        buf.write("\u020d\t\n\2\2\u020a\u020c\t\13\2\2\u020b\u020a\3\2\2")
        buf.write("\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e")
        buf.write("\3\2\2\2\u020e\u0086\3\2\2\2\u020f\u020d\3\2\2\2\u0210")
        buf.write("\u0215\7$\2\2\u0211\u0214\5\37\20\2\u0212\u0214\n\6\2")
        buf.write("\2\u0213\u0211\3\2\2\2\u0213\u0212\3\2\2\2\u0214\u0217")
        buf.write("\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216")
        buf.write("\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a\t\f\2\2")
        buf.write("\u0219\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\b")
        buf.write("D\b\2\u021c\u0088\3\2\2\2\u021d\u0222\7$\2\2\u021e\u0221")
        buf.write("\5\37\20\2\u021f\u0221\n\6\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0222\3")
        buf.write("\2\2\2\u0225\u0226\7^\2\2\u0226\u0227\n\7\2\2\u0227\u0228")
        buf.write("\bE\t\2\u0228\u008a\3\2\2\2\u0229\u022a\13\2\2\2\u022a")
        buf.write("\u022b\bF\n\2\u022b\u008c\3\2\2\2\27\2\u00ee\u00f5\u00f9")
        buf.write("\u00fd\u010f\u0115\u011a\u011f\u0123\u0128\u012a\u0139")
        buf.write("\u0147\u014f\u020d\u0213\u0215\u0219\u0220\u0222\13\3")
        buf.write("\n\2\3\13\3\3\13\4\3\13\5\3\17\6\b\2\2\3D\7\3E\b\3F\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INTLIT = 9
    FLOATLIT = 10
    BOOLLIT = 11
    STRINGLIT = 12
    BLOCKCOM = 13
    LINECOM = 14
    WS = 15
    AUTO = 16
    BREAK = 17
    BOOLEAN = 18
    DO = 19
    ELSE = 20
    FALSE = 21
    FLOAT = 22
    FOR = 23
    FUNCTION = 24
    IF = 25
    INTEGER = 26
    RETURN = 27
    STRING = 28
    TRUE = 29
    WHILE = 30
    VOID = 31
    OUT = 32
    CONTINUE = 33
    OF = 34
    INHERIT = 35
    ARRAY = 36
    PLUS = 37
    MINUS = 38
    MUL = 39
    DIV = 40
    MOD = 41
    NOT = 42
    AND = 43
    OR = 44
    EQ = 45
    NOT_EQ = 46
    LT = 47
    LT_EQ = 48
    GT = 49
    GT_EQ = 50
    CONCAT = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    LSB = 56
    RSB = 57
    DOT = 58
    COMMA = 59
    SEMI = 60
    COLON = 61
    ASSIGN = 62
    ID = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'printBoolean'", 
            "'readString'", "'printString'", "'super'", "'preventDefault'", 
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "BLOCKCOM", "LINECOM", 
            "WS", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
            "NOT_EQ", "LT", "LT_EQ", "GT", "GT_EQ", "CONCAT", "LB", "RB", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "ASSIGN", 
            "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INTLIT", "FLOATLIT", "DECPART", "EXPPART", "BOOLLIT", 
                  "STRINGLIT", "ESC", "BLOCKCOM", "LINECOM", "WS", "AUTO", 
                  "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQ", "NOT_EQ", "LT", "LT_EQ", "GT", "GT_EQ", "CONCAT", 
                  "LB", "RB", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
                  "SEMI", "COLON", "ASSIGN", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[8] = self.INTLIT_action 
            actions[9] = self.FLOATLIT_action 
            actions[13] = self.STRINGLIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            self.text = self.text.replace("_", "");

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            self.text = self.text.replace("_", "");

     

        if actionIndex == 2:

            self.text = self.text.replace("_", "");

     

        if actionIndex == 3:

            self.text = self.text.replace("_", "");

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	text = self.text[1:-1] if self.text[-1] == '\n' else self.text[1:]
            	raise UncloseString(text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


