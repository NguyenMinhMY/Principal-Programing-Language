import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    #  Test expressions and statements
    def test_assign_expression_0(self):
        input = "x = 5;"
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_assign_expression_1(self):
        input = "a[2] = b + c;"
        expect = "Error on line 1 col 1: ["
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_assign_expression_2(self):
        input = "y = \"hello world\""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_assign_expression_3(self):
        input = "z:integer = 2 * (3 + 4);"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_assign_expression_4(self):
        input = "a, b = 1, 2"
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_assign_expression_5(self):
        input = "x == 5"
        expect = "Error on line 1 col 2: =="
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_assign_expression_6(self):
        input = "y = ;"
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_assign_expression_7(self):
        input = "z,y:integer = 2, 3;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_assign_expression_8(self):
        input = "1 = x;"
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_assign_expression_9(self):
        input = "print(\"hello world\")"
        expect = "Error on line 1 col 5: ("
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_if_statement_0(self):
        input = "if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n"
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_if_statement_1(self):
        input = "x: function integer() {if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n}"
        expect = "Error on line 1 col 26: x"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_if_statement_2(self):
        input = "abc: function array[2] float (f: string) {if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n}"
        expect = "Error on line 1 col 23: float"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_if_statement_3(self):
        input = "a : boolean = if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n"
        expect = "Error on line 1 col 14: if"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_if_statement_4(self):
        input = "b : function auto (x: integer) {if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n;}"
        expect = "Error on line 1 col 35: x"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_if_statement_5(self):
        input = "bg : function integer() {if (x == 5)\n\ty = 2 * x;\nelse\n\ty = x - 1\n;}"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_if_statement_6(self):
        input = "happy: float = if x == 5:\n\ty = 2 * x\nelse:\n\ty = x - 1\n"
        expect = "Error on line 1 col 15: if"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_if_statement_7(self):
        input = "x : function float () {if (x == 5)\n\ty = 2 * x;\nelse\n\ty = x - 1\n;}"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_if_statement_8(self):
        input = "abc: function void () {if (x == 5)\n\ty = 2 * x\n;}"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_if_statement_9(self):
        input = " syntax: function auto () {if (x == 5)\n\ty = 2 * x\nelse\n\ty = x - 1\n;}"
        expect = "Error on line 3 col 0: else"
        self.assertTrue(TestParser.test(input, expect, 219))
    # while loop
    def test_while_loop_0(self):
        input = "x: integer = while x < 10:\n\tx = x + 1\n;"
        expect = "Error on line 1 col 13: while"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_while_loop_1(self):
        input = "x: integer = while x < 10:\n\tx = x + 1\n"
        expect = "Error on line 1 col 13: while"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_while_loop_2(self):
        input = """
            hai : string = "hello world";
            main: function auto(){
                do{
                    return abc;
                }while(n == 0);
                var = "Chung ta la lu quy" :: abc;
                for(x = 2,x == 2,  x+1) continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_while_loop_3(self):
        input = """
            varr : string = "hello world";
            main: function boolean(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(,,) {}
                test(123, 5+2+5+5);
            }
        """
        expect = "Error on line 8 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_while_loop_4(self):
        input = "while x < 10:\n\tx = x + 1\n"
        expect = "Error on line 1 col 0: while"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_while_loop_5(self):
        input = """
            main: function void(){
                var = "" :: "";
                for(i = 0 , i < n + 1, i = i + 1){
                }
            }
        """
        expect = "Error on line 4 col 41: ="
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_while_loop_6(self):
        input = "g: function auto () {while (x < 10){\n\tx = x + 1\n;}}"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_while_loop_7(self):
        input = "x: function void () {while (x < 10)\n\tx = x + 1\n;}"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_while_loop_8(self):
        input = "while x < 10:\n\tx = x + 1\n"
        expect = "Error on line 1 col 0: while"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_while_loop_9(self):
        input = "while x < 10:\n\tx = x + 1\n"
        expect = "Error on line 1 col 0: while"
        self.assertTrue(TestParser.test(input, expect, 229))
    # Test variable
    def test_variable_declaration_0(self):
        input = "f,x,t : integer = {3,8}, 5 ;jkj"
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_variable_declaration_1(self):
        input = "h : auto = 9 + 2 -3 * 5 /10 + foo(ihf,z,t) ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_variable_declaration_2(self):
        input = "f : float = 14445_45.41124e-1436 ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_variable_declaration_3(self):
        input = "f : array [4,5,6,7,8,8] of integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_variable_declaration_4(self):
        input = "f,y : string = footg(5+2-6*1), a(98 == 16) ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_variable_declaration_5(self):
        input = "a:string;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_variable_declaration_6(self):
        input = "a : float;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_variable_declaration_7(self):
        input = "a,b: auto = 3.4,6.7; "
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_variable_declaration_8(self):
        input = "mynguyen: boolean;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_variable_declaration_9(self):
        input = "foo: integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_variable_declaration_10(self):
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_variable_declaration_11(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_variable_declaration_12(self):
        input = """float: integer = 105;"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_variable_declaration_13(self):
        input = """a: string = "Hello, World\n";"""
        expect = "Hello, World\n"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_variable_declaration_14(self):
        input = """a: array[3] of integer = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_variable_declaration_15(self):
        input = """integer: boolean = true;"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_variable_declaration_16(self):
        input = """integer: boolean = true;"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_variable_declaration_17(self):
        input = """integer: boolean = true;"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_variable_declaration_18(self):
        input = """integer: boolean = true;"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_variable_declaration_19(self):
        input = """integer: boolean = true;"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 249))
    # test function
    def test_funcdecl_0(self):
        input = """fibonacci: function integer (n: integer){
                if( n== -1) || (n == 0) return 1;
                return fibonacci(n-1)+ fibonacci(n+1);
            }"""
        expect = "Error on line 2 col 28: ||"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_funcdecl_1(self):
        input = """fibonacci: function integer (n: integer){
                if( n== -1 || n == 0) return 1;
                return fibonacci(n-1)+ fibonacci(n+1);
            }"""
        expect = "Error on line 2 col 32: =="
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_funcdecl_2(self):
        input = """sum:function float(arr: array [] of float,res: integer){
            i, sum: integer;
            sum = 0;
            for (i = 0, i < n, i + 1) {
                sum = sum + n[i];
            }
            return sum;
        }"""
        expect = "Error on line 1 col 31: ]"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_funcdecl_3(self):
        input = """foo: function integer () {
            _false(x:int);
        }"""
        expect = "Error on line 2 col 20: :"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_funcdecl_4(self):
        input = """ v: function integer hehe () {
        
        }"""
        expect = "Error on line 1 col 21: hehe"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_funcdecl_5(self):
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_funcdecl_6(self):
        input = """count: function integer () {
            while (a-3>=12)
                abc : integer = a+4342;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_funcdecl_7(self):
        input = """foooooo: function auto () {
            }
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_funcdecl_8(self):
        input = """foo23: function array[13] of boolean () {
            if (i>10) i=i+1;
            x = y+3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_funcdecl_9(self):
        input = """foo: function void () {
            a[12,34,45,12,35,53]= "";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_program_0(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_program_1(self):
        input = """xa: integer = 6523;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(323);
            inc(xyx, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_program_2(self):
        input ="""a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_program_3(self):
        input = """fibonacci: function integer (n: integer){
                if n== -1 || (n == 0) return 1;
                return fibonacci(n-1)+ fibonacci(n+1);
            }"""
        expect = "Error on line 2 col 19: n"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_program_4(self):
        input ="""a,b : array [5] of in = {1,2,3,4,5},{2,3,4,5,6}"""
        expect = "Error on line 1 col 19: in"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_program_5(self):
        input = """ mynguyen : array[] of integer; """
        expect = """Error on line 1 col 18: ]"""
        self.assertTrue(TestParser.test(input,expect,265))
    def test_program_6(self):
        input = "f,y,y : integer = foo(), abc(),f() ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_program_7(self):
        input = """ /**/"""
        expect = """Error on line 1 col 5: <EOF>"""
        self.assertTrue(TestParser.test(input,expect,267))
    def test_program_8(self):
        input = """foo: function float () {
            foo(2);
            return expr;
        }

        c == expr;"""
        expect = "Error on line 6 col 10: =="
        self.assertTrue(TestParser.test(input,expect,268))
    def test_program_9(self):
        input = """
        // Declare and initialize variables.
        float: array [10] of integer;
        fib_nums: array [10] of integer;
        for (i = 0, i < 10, i + 1) {
            fib_nums[i] = fibonacci(i);
        }

        matrix: array [3, 3] of integer;

        // Find the largest Fibonacci number.
        largest_fib: integer = find_largest(fib_nums);

        // Find the row with the largest sum in the matrix.
        largest_sum: integer = 0;
        largest_sum_row: integer = -1;

        // Output the results.
        printf("The largest Fibonacci number is %d.\n", largest_fib);
        printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\n", largest_sum_row, largest_sum);"""
        expect = "Error on line 3 col 8: float"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_program_10(self):
        input = """ a: array [2] of string = {"s","sas"};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,270))
    def test_program_11(self):
        input = """ // this is comment
                // declaration
                x: float = 6.7;
                sum: function void() {}
                """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,271))
    def test_program_12(self):
        input = """
            // // // main function */
            ac : float = 0.12;
            str : auto = "ac";
            main: function float () {
                a = "it's dark inside" :: "it's where my demon hide";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_program_13(self):
        input = """
            func_: function integer () {
                if ("a") 
                    while("b")
                        return 345;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_program_14(self):
        input = """
            /* comment function */
            ac : float string integer = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
            }
        """
        expect = "Error on line 3 col 23: string"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_program_15(self):
        input = """main: function float () {
                a = 1_23.40E+156;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_program_16(self):
        input = """
            /* main function */
            factor_ : integer = 16.0;
            main_: function float () {
                a_ = "He asked me: \\\"Where is John?\\\"";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_program_17(self):
        input = """
            abc : auto = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "ATHFT" :: var;
                for(x=3,x==4,x+8) break;
                if ( i < 1) return 1 + foo(2);
                test();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_program_18(self):
        input = """
        matrix: array [4, 4] of integer = {[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]};
        diag_sum: integer = 0;
        for (i = 0, i < 4, i + 1) {
            diag_sum = diag_sum + matrix[i, i];
        }
        printf("The sum of the elements is %d.\\n", diag_sum);"""
        expect = "Error on line 2 col 43: ["
        self.assertTrue(TestParser.test(input,expect,278))
    def test_program_19(self):
        input = """foo: function float (x:float) {
            {x = 2+3;}
            {}        
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_program_20(self):
        input = """
         topKFrequent : function array [10] of integer (nums : array[10] of integer, k : integer) {
             map : array [10,10] of integer = {};
             for (i = 0, i < length(nums), i + 1) {
                 if (map[nums[i]] == null) {
                     map[nums[i]] = 0;
                 }
                 map[nums[i]] = map[nums[i]] + 1;
             }
             result : array [10,10] of integer = {};
             for (i = 0, i < length(map), i + 1) {
                 if (map[i] != null) {
                     result = result + i;
                 }
             }
             sort(result, map);
             return result;
         }
         main: function void () {
             nums : array [10] of integer = {1, 1, 1, 2, 2, 3};
             k = 2;
             printString(topKFrequent(nums, k));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_program_21(self):
        input = """
         canConstruct : function boolean (ransomNote : string, magazine : string) {
             n : integer = length(ransomNote);
             m : integer = length(magazine);
             if (n > m) {
                 return false;
             }
             count : array[26] of integer = {0};
             for (i = 0, i < m, i + 1) {
                 count[magazine[i] - "a"] = count[magazine[i] - "a"] + 1;
             }
             for (i = 0, i < n, i + 1) {
                 count[ransomNote[i] - "a"] = count[ransomNote[i] - "a"] - 1;
                 if (count[ransomNote[i] - "a"] < 0) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             ransomNote = "aa";
             magazine = "aab";
             printBool(canConstruct(ransomNote, magazine));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_program_22(self):
        input = """
         isValid : function boolean (s : string) {
             n : integer = length(s);
             if (n != 10) {
                 return false;
             }
             for (i = 0, i < n, i + 1) {
                 if ((s[i] < "0") || (s[i] > "9")) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s = "1234567890";
             printBool(isValid(s));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_program_23(self):
        input = """
         isPowerOfTwo : function boolean (n : integer) {
             if (n <= 0) {
                 return false;
             }
             return (n * (n - 1)) == 0;
         }
         main: function void () {
             n = 16;
             printBool(isPowerOfTwo(n));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_program_24(self):
        input = """
         isPowerOfThree : function boolean (n : integer) {
             if (n <= 0) {
                 return false;
             }
             while (n % 3 == 0) {
                 n = n / 3;
             }
             return n == 1;
         }
         main: function void () {
             n = 27;
             printBool(isPowerOfThree(n));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_program_25(self):
        input = """
         addDigits : function integer (num : integer) {
             while (num >= 10) {
                 num = num / 10 + num % 10;
             }
             return num;
         }
         main: function void () {
             num = 38;
             printInt(addDigits(num));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_program_26(self):
        input = """
         isUgly : function boolean (num : integer) {
             if (num <= 0) {
                 return false;
             }
             while (num % 2 == 0) {
                 num = num / 2;
             }
             while (num % 3 == 0) {
                 num = num / 3;
             }
             while (num % 5 == 0) {
                 num = num / 5;
             }
             return num == 1;
         }
         main: function void () {
             num = 14;
             printBool(isUgly(num));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_program_27(self):
        input = """
         hammingWeight : function integer (n : integer) {
             result : integer = 0;
             while (n != 0) {
                 result = result + 1;
                 n = n - (n - 1);
             }
             return result;
         }
         main: function void () {
             n = 11;
             printInt(hammingWeight(n));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_program_28(self):
        input = """
         reverseBits : function integer (n : integer) {
             result : integer = 0;
             for (i = 0, i < 32, i + 1) {
                 result = result * 2 + n % 2;
                 n = n / 2;
             }
             return result;
         }
         main: function void () {
             n = 43261596;
             printInt(reverseBits(n));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_program_29(self):
        input = """
         wordPattern : function boolean (pattern : string, str : string) {
             n : integer = length(pattern);
             m : integer = length(str);
             if (n != m) {
                 return false;
             }
             for (i = 0, i < n, i + 1) {
                 if (pattern[i] != str[i]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             pattern = "abba";
             str = "dog cat cat dog";
             printBool(wordPattern(pattern, str));
         }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_program_30(self):
        """longest common prefix function"""
        input = """
         longestCommonPrefix : function string (strs : array[256] of string) {
             n : integer = length(strs);
             if (n == 0) {
                 return "";
             }
             result : string = strs[0];
             for (i = 1, i < n, i + 1) {
                 while (strs[i] != result) {
                     result = result[length(result) - 1];
                 }
             }
             return result;
         }
         main: function void () {
             strs = {"flower", "flow", "flight"};
             printString(longestCommonPrefix(strs));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 290))

    def test_program_31(self):
        """Reverse string function"""
        input = """
         reverseString : function string (s : string) {
             n : integer = length(s);
             result : string = "";
             for (i = n - 1, i >= 0, i - 1) {
                 result = result + s[i];
             }
             return result;
         }
         main: function void () {
             s = "hello";
             printString(reverseString(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 291))

    def test_program_32(self):
        """Teemo attacking function"""
        input = """
         findPoisonedDuration : function integer (timeSeries : array[25] of integer, duration : integer) {
             n : integer = length(timeSeries);
             if (n == 0) {
                 return 0;
             }
             result : integer = duration;
             for (i = 1, i < n, i + 1) {
                 result = result + min(duration, timeSeries[i] - timeSeries[i - 1]);
             }
             return result;
         }
         main: function void () {
             timeSeries = {1, 4};
             duration = 2;
             printInt(findPoisonedDuration(timeSeries, duration));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 292))

    def test_program_33(self):
        """Perfect number function"""
        input = """
         checkPerfectNumber : function boolean (num : integer) {
             if (num <= 0) {
                 return false;
             }
             result : integer = 0;
             for (i = 1, i < num, i + 1) {
                 if (num % i == 0) {
                     result = result + i;
                 }
             }
             return result == num;
         }
         main: function void () {
             num = 28;
             printBool(checkPerfectNumber(num));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 293))

    def test_program_34(self):
        """Binary watch function"""
        input = """
         readBinaryWatch : function array[25] of string (num : integer) {
             result : array[230] of string = {};
             for (h = 0, h < 12, h + 1) {
                 for (m = 0, m < 60, m + 1) {
                     if ((countBits(h) + countBits(m)) == num) {
                         result = result + h + ":" + m;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             num = 1;
             printString(readBinaryWatch(num));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 294))

    def test_program_35(self):
        """to lower case function"""
        input = """
         toLowerCase : function string (str : string) {
             result : string = "";
             for (i = 0, i < length(str), i + 1) {
                 if ((str[i] >= "A") && (str[i] <= "Z")) {
                     result = result + chr(ord(str[i]) + 32);
                 } else {
                     result = result + str[i];
                 }
             }
             return result;
         }
         main: function void () {
             str = "Hello";
             printString(toLowerCase(str));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 295))

    def test_program_36(self):
        """Find pivot index function"""
        input = """
         pivotIndex : function integer (nums : array[10] of integer) {
             n : integer = length(nums);
             if (n == 0) {
                 return -1;
             }
             leftSum : array[25] of integer = {0};
             for (i = 0, i < n, i + 1) {
                 leftSum = leftSum + leftSum[i] + nums[i];
             }
             for (i = 0, i < n, i + 1) {
                 if (leftSum[i] == (leftSum[n] - leftSum[i + 1])) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             nums = {1, 7, 3, 6, 5, 6};
             printInt(pivotIndex(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 296))

    def test_program_37(self):
        """Rotate string"""
        input = """
         rotateString : function boolean (A : string, B : string) {
             return (length(A) == length(B)) && contains(B,(A + A));
         }
         main: function void () {
             A = "abcde";
             B = "cdeab";
             printBool(rotateString(A, B));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 297))

    def test_program_38(self):
        """Fixed point function"""
        input = """
         fixedPoint : function integer (a: array[5] of integer) {
             n : integer = length(a);
             for (i = 0, i < n, i + 1) {
                 if (a[i] == i) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             a : array[5] of integer = {-10, -5, 0, 3, 7};
             printInt(fixedPoint(a));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 298))

    def test_program_39(self):
        """High five function"""
        input = """
         highFive : function array [10] of integer (items : array[10,10] of integer) {
             result : array[10] of integer = {};
             map : array [10,10] of integer = {};
             for (i = 0, i < length(items), i + 1) {
                 id = items[i,0];
                 score = items[i,1];
                 if (map[id] == null) {
                     map[id] = {};
                 }
                 map[id] = map[id] + score;
             }
             for (i = 0, i < length(map), i + 1) {
                 if (map[i] != null) {
                     result = result + average(map[i]);
                 }
             }
             return result;
         }
         main: function void () {
             items : array [10,10] of integer = {{1, 91}, {1, 92}, {2, 93}, {2, 97}, {1, 60}, {2, 77}, {1, 65}, {1, 87}, {1, 100}, {2, 100}, {2, 76}};
             printString(highFive(items));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input, expected, 299))
