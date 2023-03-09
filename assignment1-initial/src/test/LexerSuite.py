import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # Test comments
    def test_comment_0(self):
        input = "/* // */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))
    def test_comment_1(self):
        input = "/* /* */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
    def test_comment_2(self):
        input = "/* */ */"
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
    def test_comment_3(self):
        input = "/* nguyenminhmy \n \b \r */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
    def test_comment_4(self):
        input = "/* */ afasf /* */"
        expect = "afasf,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_comment_5(self):
        input = "/* afasf ;llasf\n \\b \t */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
    def test_comment_6(self):
        input = "// fasokmadlkbanjpj aglkhibndjpojbwjb; "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
    def test_comment_7(self):
        input = "// fasokmadlkbanjpj aglkhibndjpojbwjb\n\nabc "
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
    def test_comment_8(self):
        input = "// Day la line comment "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
    def test_comment_9(self):
        input = "// Day la line comment va \n /* Day la block comments \n\t\b*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))

    # Test Literals
    # Integer
    def test_literals_integer_0(self):
        input = "315115"
        expect = "315115,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))
    def test_literals_integer_1(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
    def test_literals_integer_2(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
    def test_literals_integer_3(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    def test_literals_integer_4(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
    def test_literals_integer_5(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_literals_integer_6(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))
    def test_literals_integer_7(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_literals_integer_8(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_literals_integer_9(self):
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,119))
    # Float
    def test_literals_float_0(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,120))
    def test_literals_float_1(self):
        self.assertTrue(TestLexer.test(".3e-2+423", ".3e-2,+,423,<EOF>", 121))
    def test_literals_float_2(self):
        self.assertTrue(TestLexer.test("1.26e2E3","1.26e2,E3,<EOF>",122))
    def test_literals_float_3(self):
        self.assertTrue(TestLexer.test("10e3","10e3,<EOF>",123))
    def test_literals_float_4(self):
        self.assertTrue(TestLexer.test("10e-356","10e-356,<EOF>",124))
    def test_literals_float_5(self):
        self.assertTrue(TestLexer.test("10.E+-3","10.,E,+,-,3,<EOF>",125))
    def test_literals_float_6(self):
        self.assertTrue(TestLexer.test("12.-25","12.,-,25,<EOF>",126))
    def test_literals_float_7(self):
        self.assertTrue(TestLexer.test("10.25E+24","10.25E+24,<EOF>",127))
    def test_literals_float_8(self):
        self.assertTrue(TestLexer.test("123.3e+23abc","123.3e+23,abc,<EOF>",128))
    def test_literals_float_9(self):
        self.assertTrue(TestLexer.test("125600.adc","125600.,adc,<EOF>",129))
    # String  
    def test_literals_string_0(self):
        input = """ "He asked me: \\"Where is John?\\"" """
        expect = """He asked me: \\"Where is John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(	input,expect, 130))
    def test_literals_string_1(self):
        input = """ "He asked \\n me: \\"Where is John?\\"" """
        expect = """He asked \\n me: \\"Where is John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,131))
    def test_literals_string_2(self):
        input = "\"mynguyen@$%^*7@()%$@mail.com.vn\"\n"
        expect = "mynguyen@$%^*7@()%$@mail.com.vn,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))
    def test_literals_string_3(self):
        input = """ "The quick brown fox jumps over the lazy dog." """
        expect = "The quick brown fox jumps over the lazy dog.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))
    def test_literals_string_4(self):
        input = """ "!@#$%^&*()-_=+[]{};:'",.<>/|?" """
        expect = """!@#$%^&*()-_=+[]{};:',,,.,<,>,/,Error Token |"""
        self.assertTrue(TestLexer.test(input, expect, 134))
    def test_literals_string_5(self):
        input = """ "\\"Hello, \\u041C\\u0438\\u0440!\\"" """
        expect = """Illegal Escape In String: \\"Hello, \\u"""
        self.assertTrue(TestLexer.test(input, expect, 135))
    def test_literals_string_6(self):
        input = """"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))
    def test_literals_string_7(self):
        input = """ "\\t Hello \\b my \\r family" """
        expect = """\\t Hello \\b my \\r family,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 137))
    def test_literals_string_8(self):
        input = """ "\\t Hello \\b my \\r family" """
        expect = """\\t Hello \\b my \\r family,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))
    def test_literals_string_9(self):
        input = """ "\\t Hello \\b my \\r family" """
        expect = """\\t Hello \\b my \\r family,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 139))

    # Test Keywords
    def test_keywords_0(self):
        self.assertTrue(TestLexer.test("auto break boolean do else false","auto,break,boolean,do,else,false,<EOF>", 140))
    def test_keywords_1(self):
        self.assertTrue(TestLexer.test("float for function if integer return string","float,for,function,if,integer,return,string,<EOF>", 141))
    def test_keywords_2(self):
        self.assertTrue(TestLexer.test("true while void out continue of inherit array","true,while,void,out,continue,of,inherit,array,<EOF>", 142))

    # Test whitespaces
    def test_whitespace_0(self):
        self.assertTrue(TestLexer.test("\t", "<EOF>", 143))
    def test_whitespace_1(self):
        self.assertTrue(TestLexer.test("\n", "<EOF>", 144))
    def test_whitespace_2(self):
        self.assertTrue(TestLexer.test(" \t \n \r", "<EOF>", 145))
    def test_whitespace_3(self):
        self.assertTrue(TestLexer.test("my\nnguyen \t\r", "my,nguyen,<EOF>", 146))
    # Test operators
    def test_operators(self):
        self.assertTrue(TestLexer.test("+ +. - -. * *. \ \. % ! && || == != < > <= >= =/= <. >. <=. >=."
                        , "+,+,.,-,-,.,*,*,.,Error Token \\", 147))
    # Test seperators
    def test_seperators_0(self):
        self.assertTrue(TestLexer.test("( ) [ ] : . , ; { }", "(,),[,],:,.,,,;,{,},<EOF>", 148))
    def test_seperators_1(self):
        self.assertTrue(TestLexer.test("(my nguyen)", "(,my,nguyen,),<EOF>", 149))
    # Test ID
    def test_identifier_0(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",150))    
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("abcDf","abcDf,<EOF>",151))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("aCBbdcMinhMy","aCBbdcMinhMy,<EOF>",152))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("abc_12Agv@dhft","abc_12Agv,Error Token @",153))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("1692nguyenminhmy","1692,nguyenminhmy,<EOF>",154))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("NguyenMinhMy","NguyenMinhMy,<EOF>",155))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.test("aA12_gk20#readf","aA12_gk20,Error Token #",156))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.test("2013811my_nguyen2013811","2013811,my_nguyen2013811,<EOF>",157))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.test("Varr 367","Varr,367,<EOF>",158))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("20t","20,t,<EOF>",159))    

    # Test Complex
    def test_complex_0(self):
        self.assertTrue(TestLexer.test("foo : function integer(){return 1;}","foo,:,function,integer,(,),{,return,1,;,},<EOF>",160))
    def test_complex_1(self):
        input = "for i in range(len(a)):\n        for j in range(len(a[0]))"
        expect = "for,i,in,range,(,len,(,a,),),:,for,j,in,range,(,len,(,a,[,0,],),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_complex_2(self):
        input = "int n,m;\n    cin >> n >> m;\n    integer arr[n,1];\n "
        expect = "int,n,,,m,;,cin,>,>,n,>,>,m,;,integer,arr,[,n,,,1,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))

    def test_complex_3(self):
        input = "pair<int, float> b)\n{\n    if (a.first < b.first)\n"
        expect = "pair,<,int,,,float,>,b,),{,if,(,a,.,first,<,b,.,first,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_complex_4(self):
        input = "variable: fl = 0.12e123; Var: a[[fl][0x123F,0O256]];"
        expect = "variable,:,fl,=,0.12e123,;,Var,:,a,[,[,fl,],[,0,x123F,,,0,O256,],],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_complex_5(self):
        input = " for (long long i = 0; i < n; i ++)\n        cin >> a1[i];\n"
        expect = "for,(,long,long,i,=,0,;,i,<,n,;,i,+,+,),cin,>,>,a1,[,i,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test_complex_6(self):
        input = "Var: nguyen = new My();\n"
        expect = "Var,:,nguyen,=,new,My,(,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))    
    def test_complex_7(self):
        input = """fibonacci: function integer (n: integer){
                if( n== -1 || n == 0) return 1;
                return fibonacci(n-1)+ fibonacci(n+1);
            }"""
        expect = "fibonacci,:,function,integer,(,n,:,integer,),{,if,(,n,==,-,1,||,n,==,0,),return,1,;,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,+,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))    
    def test_complex_8(self):
        input = "integer: boolean = true;"
        expect = "integer,:,boolean,=,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))    
    def test_complex_9(self):
        input = "a: array[3] of integer = {1,2,3};"
        expect = "a,:,array,[,3,],of,integer,=,{,1,,,2,,,3,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))    
    
    # Unclosed String, Illigal Escape, Error char
    def test_literals_unclosed_string_0(self):
        input = "\"%^#$@mail.com"
        expect = "Unclosed String: %^#$@mail.com"
        self.assertTrue(TestLexer.test(input, expect, 170))
    def test_literals_unclosed_string_1(self):
        input = """ "sdghjhjgjhg"""
        expect = "Unclosed String: sdghjhjgjhg"
        self.assertTrue(TestLexer.test(input, expect, 171))
    def test_literals_unclosed_string_2(self):
        input = """ "Lan song xanh"""
        expect = "Unclosed String: Lan song xanh"
        self.assertTrue(TestLexer.test(input, expect, 172))
    def test_literals_unclosed_string_3(self):
        input = """ "my family"""
        expect = "Unclosed String: my family"
        self.assertTrue(TestLexer.test(input, expect, 173))
    def test_literals_unclosed_string_4(self):
        input = """ "nguyen minh my"""
        expect = "Unclosed String: nguyen minh my"
        self.assertTrue(TestLexer.test(input, expect, 174))
    def test_literals_unclosed_string_5(self):
        input = """ "abc"anh em\""""
        expect = "abc,anh,em,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 175))
    def test_literals_unclosed_string_6(self):
        input = """ "sdghjhjgjhg"""
        expect = "Unclosed String: sdghjhjgjhg"
        self.assertTrue(TestLexer.test(input, expect, 176))
    def test_literals_unclosed_string_7(self):
        input = """ "Hello every body"""
        expect = "Unclosed String: Hello every body"
        self.assertTrue(TestLexer.test(input, expect, 177))
    def test_literals_unclosed_string_8(self):
        input = """ "CSE \n\\t"""
        expect = "Unclosed String: CSE \n"
        self.assertTrue(TestLexer.test(input, expect, 178))
    def test_literals_unclosed_string_9(self):
        input = """ "aaaaaaaaa\n\n\n"""
        expect = "Unclosed String: aaaaaaaaa\n"
        self.assertTrue(TestLexer.test(input, expect, 179))
    
    def test_literals_illegal_esc_0(self):
        input = """ " \\"he \\e abc \\" " """
        expect = """Illegal Escape In String:  \\"he \\e"""
        self.assertTrue(TestLexer.test(input, expect, 180))
    def test_literals_illegal_esc_1(self):
        input = """ " \\"he \\vrt abc \\" " """
        expect = """Illegal Escape In String:  \\"he \\v"""
        self.assertTrue(TestLexer.test(input, expect, 181))
    def test_literals_illegal_esc_2(self):
        input = """ "con buom xinh \d\r\t\h\k" """
        expect = """Illegal Escape In String: con buom xinh \d"""
        self.assertTrue(TestLexer.test(input, expect, 182))
    def test_literals_illegal_esc_3(self):
        input = """ "con buom xinh \l " """
        expect = """Illegal Escape In String: con buom xinh \l"""
        self.assertTrue(TestLexer.test(input, expect, 183))
    def test_literals_illegal_esc_4(self):
        input = """ "abbb \g " """
        expect = """Illegal Escape In String: abbb \g"""
        self.assertTrue(TestLexer.test(input, expect, 184))
    def test_literals_illegal_esc_5(self):
        input = """ " \\"she \m \\" " """
        expect = """Illegal Escape In String:  \\"she \m"""
        self.assertTrue(TestLexer.test(input, expect, 185))
    def test_literals_illegal_esc_6(self):
        input = """ " \\"he \\e abc \\" " """
        expect = """Illegal Escape In String:  \\"he \\e"""
        self.assertTrue(TestLexer.test(input, expect, 186))
    def test_literals_illegal_esc_7(self):
        input = """ " A Hi Hi HA HA \q" """
        expect = """Illegal Escape In String:  A Hi Hi HA HA \q"""
        self.assertTrue(TestLexer.test(input, expect, 187))
    def test_literals_illegal_esc_8(self):
        input = """ "\\kvan\\k duyen " """
        expect = """Illegal Escape In String: \k"""
        self.assertTrue(TestLexer.test(input, expect, 188))
    def test_literals_illegal_esc_9(self):
        input = """ 123 "123a\\m123" """
        expect = """123,Illegal Escape In String: 123a\m"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    # Test error char
    def test_error_char_0(self):
        input = "@"
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input,expect,190))
    def test_error_char_1(self):
        input = "^^"
        expect = "Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,191))
    def test_error_char_2(self):
        input = "<..> ** <^^>"
        expect = "<,.,.,>,*,*,<,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,192))
    def test_error_char_3(self):
        input = """/\/\/\/\ """
        expect = "/,Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,193))
    def test_error_char_4(self):
        input = "\\B\\T"
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,194))
    def test_error_char_5(self):
        input = "!-!&#@"
        expect = "!,-,!,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,195))
    def test_error_char_6(self):
        input = "0x123 nguyen $"
        expect = "0,x123,nguyen,Error Token $"
        self.assertTrue(TestLexer.test(input,expect,196))
    def test_error_char_7(self):
        input = "Var: xyz; ^"
        expect = "Var,:,xyz,;,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,197))        
    def test_error_char_8(self):
        input = "Where are you from %%%%&"
        expect = "Where,are,you,from,%,%,%,%,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,198))
    def test_error_char_9(self):
        input = "agojoiqwn@akjhs8"
        expect = "agojoiqwn,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,199))
