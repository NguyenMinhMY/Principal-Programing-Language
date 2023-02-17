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
        expect = ""  
        self.assertTrue(TestLexer.test(input,expect,101)) 

    def test_literals_string_0(self):
        input = "He asked me: \\\"Where is John?\\\""
        expect = "He asked me: \\\"Where is John?\\\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,400))
    def test_literals_string_9(self):
            """STRING LITERALS #9 CASE#21"""
            input = "\"duchungho@$%^*7@()%^#$@mail.com\"\n"
            expect = "\"duchungho@$%^*7@()%^#$@mail.com\",<EOF>"
            self.assertTrue(TestLexer.test(input, expect, 409))

    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
