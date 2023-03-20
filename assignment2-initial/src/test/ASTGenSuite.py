import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_1(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """isPerfect : function boolean(n: integer) {
    sum = 0;
    for (i = 1, i < n, i + 1) {
        if (n % i == 0) {
            sum = sum + i;
        }
    }
    return sum == n;
}

main: function void() {
    printBool(isPerfect(6));
    printBool(isPerfect(10));
}"""
        expect = """Program([
	FuncDecl(isPerfect, BooleanType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))])), ReturnStmt(BinExpr(==, Id(sum), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBool, FuncCall(isPerfect, [IntegerLit(6)])), CallStmt(printBool, FuncCall(isPerfect, [IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test_7(self):
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
        }"""""""""
        expect = """Program([
	VarDecl(xa, IntegerType, IntegerLit(6523))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(323)])), CallStmt(inc, Id(xyx), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))


    def test_8(self):
        input = """varr : string = "hello world";
            main: function boolean(){
                do{
                    return false;
                }while(n == 0);
            }"""
        expect = """Program([
	VarDecl(varr, StringType, StringLit(hello world))
	FuncDecl(main, BooleanType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_9(self):
        input = """a, b, c, d: integer = 3, 4, 6,7;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
	VarDecl(d, IntegerType, IntegerLit(7))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))


    def test_10(self):
        input = """fibonacci: function integer (n: integer){
                if (n== -1 || (n == 0)) return 1;
                return fibonacci(n-1)+ fibonacci(n+1);
            }"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), BinExpr(||, UnExpr(-, IntegerLit(1)), BinExpr(==, Id(n), IntegerLit(0)))), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(+, Id(n), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))


    def test_11(self):
        input = """// this is comment
                // declaration
                x: float = 6.7;
                sum: function void() {
                
                }"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(6.7))
	FuncDecl(sum, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))


    def test_12(self):
        input = """// // // main function */
            ac : float = 0.12;
            str : auto = "ac";
            main: function float () {
                a = "it's dark inside" :: "it's where my demon hide";
            }"""
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(0.12))
	VarDecl(str, AutoType, StringLit(ac))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(it's dark inside), StringLit(it's where my demon hide)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))


    def test_13(self):
        input = """func_: function integer () {
                if ("a") 
                    while("b")
                        return 345;
            }"""
        expect = """Program([
	FuncDecl(func_, IntegerType, [], None, BlockStmt([IfStmt(StringLit(a), WhileStmt(StringLit(b), ReturnStmt(IntegerLit(345))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))


    def test_14(self):
        input = """main: function float () {
                a = 1_23.40E+156;
            }"""
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.234e+158))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))


    def test_15(self):
        input = """f : array [1] of integer = {1214, 123};"""
        expect = """Program([
	VarDecl(f, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1214), IntegerLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))


    def test_16(self):
        input = """abc : auto = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "ATHFT" :: var;
                for(x=3,x==4,x+8) break;
                if ( i < 1) return 1 + foo(2);
                test();
            }"""
        expect = """Program([
	VarDecl(abc, AutoType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(ATHFT), Id(var))), ForStmt(AssignStmt(Id(x), IntegerLit(3)), BinExpr(==, Id(x), IntegerLit(4)), BinExpr(+, Id(x), IntegerLit(8)), BreakStmt()), IfStmt(BinExpr(<, Id(i), IntegerLit(1)), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)])))), CallStmt(test, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))


    def test_17(self):
        input = """topKFrequent : function array [10] of integer (nums : array[10] of integer, k : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(topKFrequent, ArrayType([10], IntegerType), [Param(nums, ArrayType([10], IntegerType)), Param(k, IntegerType)], None, BlockStmt([VarDecl(map, ArrayType([10, 10], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(map, [ArrayCell(nums, [Id(i)])]), Id(null)), BlockStmt([AssignStmt(ArrayCell(map, [ArrayCell(nums, [Id(i)])]), IntegerLit(0))])), AssignStmt(ArrayCell(map, [ArrayCell(nums, [Id(i)])]), BinExpr(+, ArrayCell(map, [ArrayCell(nums, [Id(i)])]), IntegerLit(1)))])), VarDecl(result, ArrayType([10, 10], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(map)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(map, [Id(i)]), Id(null)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), Id(i)))]))])), CallStmt(sort, Id(result), Id(map)), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3)])), AssignStmt(Id(k), IntegerLit(2)), CallStmt(printString, FuncCall(topKFrequent, [Id(nums), Id(k)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))


    def test_18(self):
        input = """canConstruct : function boolean (ransomNote : string, magazine : string) {
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
         }"""
        expect = """Program([
	FuncDecl(canConstruct, BooleanType, [Param(ransomNote, StringType), Param(magazine, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(ransomNote)])), VarDecl(m, IntegerType, FuncCall(length, [Id(magazine)])), IfStmt(BinExpr(>, Id(n), Id(m)), BlockStmt([ReturnStmt(BooleanLit(False))])), VarDecl(count, ArrayType([26], IntegerType), ArrayLit([IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(count, [BinExpr(-, ArrayCell(magazine, [Id(i)]), StringLit(a))]), BinExpr(+, ArrayCell(count, [BinExpr(-, ArrayCell(magazine, [Id(i)]), StringLit(a))]), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(count, [BinExpr(-, ArrayCell(ransomNote, [Id(i)]), StringLit(a))]), BinExpr(-, ArrayCell(count, [BinExpr(-, ArrayCell(ransomNote, [Id(i)]), StringLit(a))]), IntegerLit(1))), IfStmt(BinExpr(<, ArrayCell(count, [BinExpr(-, ArrayCell(ransomNote, [Id(i)]), StringLit(a))]), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(ransomNote), StringLit(aa)), AssignStmt(Id(magazine), StringLit(aab)), CallStmt(printBool, FuncCall(canConstruct, [Id(ransomNote), Id(magazine)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))


    def test_19(self):
        input = """isPowerOfTwo : function boolean (n : integer) {
             if (n <= 0) {
                 return false;
             }
             return (n * (n - 1)) == 0;
         }
         main: function void () {
             n = 16;
             printBool(isPowerOfTwo(n));
         }"""
        expect = """Program([
	FuncDecl(isPowerOfTwo, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ReturnStmt(BinExpr(==, BinExpr(*, Id(n), BinExpr(-, Id(n), IntegerLit(1))), IntegerLit(0)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(16)), CallStmt(printBool, FuncCall(isPowerOfTwo, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))


    def test_20(self):
        input = """isValid : function boolean (s : string) {
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
         }"""
        expect = """Program([
	FuncDecl(isValid, BooleanType, [Param(s, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(s)])), IfStmt(BinExpr(!=, Id(n), IntegerLit(10)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(<, ArrayCell(s, [Id(i)]), StringLit(0)), BinExpr(>, ArrayCell(s, [Id(i)]), StringLit(9))), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(1234567890)), CallStmt(printBool, FuncCall(isValid, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))


    def test_21(self):
        input = """isPowerOfThree : function boolean (n : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(isPowerOfThree, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), WhileStmt(BinExpr(==, BinExpr(%, Id(n), IntegerLit(3)), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(3)))])), ReturnStmt(BinExpr(==, Id(n), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(27)), CallStmt(printBool, FuncCall(isPowerOfThree, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))


    def test_22(self):
        input = """addDigits : function integer (num : integer) {
             while (num >= 10) {
                 num = num / 10 + num % 10;
             }
             return num;
         }
         main: function void () {
             num = 38;
             printInt(addDigits(num));
         }"""
        expect = """Program([
	FuncDecl(addDigits, IntegerType, [Param(num, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>=, Id(num), IntegerLit(10)), BlockStmt([AssignStmt(Id(num), BinExpr(+, BinExpr(/, Id(num), IntegerLit(10)), BinExpr(%, Id(num), IntegerLit(10))))])), ReturnStmt(Id(num))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(num), IntegerLit(38)), CallStmt(printInt, FuncCall(addDigits, [Id(num)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))


    def test_23(self):
        input = """ isUgly : function boolean (num : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(isUgly, BooleanType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(num), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), WhileStmt(BinExpr(==, BinExpr(%, Id(num), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(2)))])), WhileStmt(BinExpr(==, BinExpr(%, Id(num), IntegerLit(3)), IntegerLit(0)), BlockStmt([AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(3)))])), WhileStmt(BinExpr(==, BinExpr(%, Id(num), IntegerLit(5)), IntegerLit(0)), BlockStmt([AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(5)))])), ReturnStmt(BinExpr(==, Id(num), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(num), IntegerLit(14)), CallStmt(printBool, FuncCall(isUgly, [Id(num)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))


    def test_24(self):
        input = """hammingWeight : function integer (n : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(hammingWeight, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1))), AssignStmt(Id(n), BinExpr(-, Id(n), BinExpr(-, Id(n), IntegerLit(1))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(11)), CallStmt(printInt, FuncCall(hammingWeight, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))


    def test_25(self):
        input = """ reverseBits : function integer (n : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(reverseBits, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(32)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, BinExpr(*, Id(result), IntegerLit(2)), BinExpr(%, Id(n), IntegerLit(2)))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(2)))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(43261596)), CallStmt(printInt, FuncCall(reverseBits, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))


    def test_26(self):
        input = """wordPattern : function boolean (pattern : string, str : string) {
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
         }"""
        expect = """Program([
	FuncDecl(wordPattern, BooleanType, [Param(pattern, StringType), Param(str, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(pattern)])), VarDecl(m, IntegerType, FuncCall(length, [Id(str)])), IfStmt(BinExpr(!=, Id(n), Id(m)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(pattern, [Id(i)]), ArrayCell(str, [Id(i)])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(pattern), StringLit(abba)), AssignStmt(Id(str), StringLit(dog cat cat dog)), CallStmt(printBool, FuncCall(wordPattern, [Id(pattern), Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))


    def test_27(self):
        input = """longestCommonPrefix : function string (strs : array[256] of string) {
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
         }"""
        expect = """Program([
	FuncDecl(longestCommonPrefix, StringType, [Param(strs, ArrayType([256], StringType))], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(strs)])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(StringLit())])), VarDecl(result, StringType, ArrayCell(strs, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(!=, ArrayCell(strs, [Id(i)]), Id(result)), BlockStmt([AssignStmt(Id(result), ArrayCell(result, [BinExpr(-, FuncCall(length, [Id(result)]), IntegerLit(1))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(strs), ArrayLit([StringLit(flower), StringLit(flow), StringLit(flight)])), CallStmt(printString, FuncCall(longestCommonPrefix, [Id(strs)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))


    def test_28(self):
        input = """reverseString : function string (s : string) {
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
         }"""
        expect = """Program([
	FuncDecl(reverseString, StringType, [Param(s, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(s)])), VarDecl(result, StringType, StringLit()), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(hello)), CallStmt(printString, FuncCall(reverseString, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))


    def test_29(self):
        input = """findPoisonedDuration : function integer (timeSeries : array[25] of integer, duration : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(findPoisonedDuration, IntegerType, [Param(timeSeries, ArrayType([25], IntegerType)), Param(duration, IntegerType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(timeSeries)])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), VarDecl(result, IntegerType, Id(duration)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), FuncCall(min, [Id(duration), BinExpr(-, ArrayCell(timeSeries, [Id(i)]), ArrayCell(timeSeries, [BinExpr(-, Id(i), IntegerLit(1))]))])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(timeSeries), ArrayLit([IntegerLit(1), IntegerLit(4)])), AssignStmt(Id(duration), IntegerLit(2)), CallStmt(printInt, FuncCall(findPoisonedDuration, [Id(timeSeries), Id(duration)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))


    def test_30(self):
        input = """checkPerfectNumber : function boolean (num : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(checkPerfectNumber, BooleanType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(num), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), VarDecl(result, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(num)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(num), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), Id(i)))]))])), ReturnStmt(BinExpr(==, Id(result), Id(num)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(num), IntegerLit(28)), CallStmt(printBool, FuncCall(checkPerfectNumber, [Id(num)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))


    def test_31(self):
        input = """readBinaryWatch : function array[25] of string (num : integer) {
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
         }"""
        expect = """Program([
	FuncDecl(readBinaryWatch, ArrayType([25], StringType), [Param(num, IntegerType)], None, BlockStmt([VarDecl(result, ArrayType([230], StringType), ArrayLit([])), ForStmt(AssignStmt(Id(h), IntegerLit(0)), BinExpr(<, Id(h), IntegerLit(12)), BinExpr(+, Id(h), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(m), IntegerLit(0)), BinExpr(<, Id(m), IntegerLit(60)), BinExpr(+, Id(m), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, FuncCall(countBits, [Id(h)]), FuncCall(countBits, [Id(m)])), Id(num)), BlockStmt([AssignStmt(Id(result), BinExpr(+, BinExpr(+, BinExpr(+, Id(result), Id(h)), StringLit(:)), Id(m)))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(num), IntegerLit(1)), CallStmt(printString, FuncCall(readBinaryWatch, [Id(num)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))


    def test_32(self):
        input = """toLowerCase : function string (str : string) {
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
         }"""
        expect = """Program([
	FuncDecl(toLowerCase, StringType, [Param(str, StringType)], None, BlockStmt([VarDecl(result, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, ArrayCell(str, [Id(i)]), StringLit(A)), BinExpr(<=, ArrayCell(str, [Id(i)]), StringLit(Z))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), FuncCall(chr, [BinExpr(+, FuncCall(ord, [ArrayCell(str, [Id(i)])]), IntegerLit(32))])))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(str, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello)), CallStmt(printString, FuncCall(toLowerCase, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))


    def test_33(self):
        input = """pivotIndex : function integer (nums : array[10] of integer) {
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
         }"""
        expect = """Program([
	FuncDecl(pivotIndex, IntegerType, [Param(nums, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(nums)])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), VarDecl(leftSum, ArrayType([25], IntegerType), ArrayLit([IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(leftSum), BinExpr(+, BinExpr(+, Id(leftSum), ArrayCell(leftSum, [Id(i)])), ArrayCell(nums, [Id(i)])))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(leftSum, [Id(i)]), BinExpr(-, ArrayCell(leftSum, [Id(n)]), ArrayCell(leftSum, [BinExpr(+, Id(i), IntegerLit(1))]))), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(7), IntegerLit(3), IntegerLit(6), IntegerLit(5), IntegerLit(6)])), CallStmt(printInt, FuncCall(pivotIndex, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))


    def test_34(self):
        input = """rotateString : function boolean (A : string, B : string) {
             return (length(A) == length(B)) && contains(B,(A + A));
         }
         main: function void () {
             A = "abcde";
             B = "cdeab";
             printBool(rotateString(A, B));
         }"""
        expect = """Program([
	FuncDecl(rotateString, BooleanType, [Param(A, StringType), Param(B, StringType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(==, FuncCall(length, [Id(A)]), FuncCall(length, [Id(B)])), FuncCall(contains, [Id(B), BinExpr(+, Id(A), Id(A))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(A), StringLit(abcde)), AssignStmt(Id(B), StringLit(cdeab)), CallStmt(printBool, FuncCall(rotateString, [Id(A), Id(B)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))


    def test_35(self):
        input = """fixedPoint : function integer (a: array[5] of integer) {
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
         }"""
        expect = """Program([
	FuncDecl(fixedPoint, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(a)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [Id(i)]), Id(i)), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([UnExpr(-, IntegerLit(10)), UnExpr(-, IntegerLit(5)), IntegerLit(0), IntegerLit(3), IntegerLit(7)])), CallStmt(printInt, FuncCall(fixedPoint, [Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))


    def test_36(self):
        input = """highFive : function array [10] of integer (items : array[10,10] of integer) {
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
         }"""
        expect = """Program([
	FuncDecl(highFive, ArrayType([10], IntegerType), [Param(items, ArrayType([10, 10], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([10], IntegerType), ArrayLit([])), VarDecl(map, ArrayType([10, 10], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(items)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(id), ArrayCell(items, [Id(i), IntegerLit(0)])), AssignStmt(Id(score), ArrayCell(items, [Id(i), IntegerLit(1)])), IfStmt(BinExpr(==, ArrayCell(map, [Id(id)]), Id(null)), BlockStmt([AssignStmt(ArrayCell(map, [Id(id)]), ArrayLit([]))])), AssignStmt(ArrayCell(map, [Id(id)]), BinExpr(+, ArrayCell(map, [Id(id)]), Id(score)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(map)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(map, [Id(i)]), Id(null)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), FuncCall(average, [ArrayCell(map, [Id(i)])])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(items, ArrayType([10, 10], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(91)]), ArrayLit([IntegerLit(1), IntegerLit(92)]), ArrayLit([IntegerLit(2), IntegerLit(93)]), ArrayLit([IntegerLit(2), IntegerLit(97)]), ArrayLit([IntegerLit(1), IntegerLit(60)]), ArrayLit([IntegerLit(2), IntegerLit(77)]), ArrayLit([IntegerLit(1), IntegerLit(65)]), ArrayLit([IntegerLit(1), IntegerLit(87)]), ArrayLit([IntegerLit(1), IntegerLit(100)]), ArrayLit([IntegerLit(2), IntegerLit(100)]), ArrayLit([IntegerLit(2), IntegerLit(76)])])), CallStmt(printString, FuncCall(highFive, [Id(items)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))


    def test_37(self):
        input = """g: function auto () {while (x < 10){\n\tx = x + 1\n;}}"""
        expect = """Program([
	FuncDecl(g, AutoType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))


    def test_38(self):
        input = """hai : string = "hello world";
            main: function auto(){
                do{
                    return abc;
                }while(n == 0);
                var = "Chung ta la lu quy" :: abc;
                for(x = 2,x == 2,  x+1) continue;
            }"""
        expect = """Program([
	VarDecl(hai, StringType, StringLit(hello world))
	FuncDecl(main, AutoType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(Id(abc))])), AssignStmt(Id(var), BinExpr(::, StringLit(Chung ta la lu quy), Id(abc))), ForStmt(AssignStmt(Id(x), IntegerLit(2)), BinExpr(==, Id(x), IntegerLit(2)), BinExpr(+, Id(x), IntegerLit(1)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))


    def test_39(self):
        input = """abc: function void () {if (x == 5)\n\ty = 2 * x\n;}"""
        expect = """Program([
	FuncDecl(abc, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(5)), AssignStmt(Id(y), BinExpr(*, IntegerLit(2), Id(x))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))


    def test_40(self):
        input = """x : function float () {if (x == 5)\n\ty = 2 * x;\nelse\n\ty = x - 1\n;}"""
        expect = """Program([
	FuncDecl(x, FloatType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(5)), AssignStmt(Id(y), BinExpr(*, IntegerLit(2), Id(x))), AssignStmt(Id(y), BinExpr(-, Id(x), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))


    def test_41(self):
        input = """bg : function integer() {if (x == 5)\n\ty = 2 * x;\nelse\n\ty = x - 1\n;}"""

        expect = """Program([
	FuncDecl(bg, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(5)), AssignStmt(Id(y), BinExpr(*, IntegerLit(2), Id(x))), AssignStmt(Id(y), BinExpr(-, Id(x), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))


    def test_42(self):
        input = """x: function void () {while (x < 10)\n\tx = x + 1\n;}"""
        expect = """Program([
	FuncDecl(x, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(10)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))


    def test_43(self):
        input = """f,x,t : integer = {3,8}, 5 ,jkj;"""
        expect = """Program([
	VarDecl(f, IntegerType, ArrayLit([IntegerLit(3), IntegerLit(8)]))
	VarDecl(x, IntegerType, IntegerLit(5))
	VarDecl(t, IntegerType, Id(jkj))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))


    def test_44(self):
        input = """h : auto = 9 + 2 -3 * 5 /10 + foo(ihf,z,t) ;"""
        expect = """Program([
	VarDecl(h, AutoType, BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(9), IntegerLit(2)), BinExpr(/, BinExpr(*, IntegerLit(3), IntegerLit(5)), IntegerLit(10))), FuncCall(foo, [Id(ihf), Id(z), Id(t)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))


    def test_45(self):
        input = """f : float = 14445_45.41124e-1436 ;"""
        expect = """Program([
	VarDecl(f, FloatType, FloatLit(0.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))


    def test_46(self):
        input = """f : array [4,5,6,7,8,8] of integer;"""
        expect = """Program([
	VarDecl(f, ArrayType([4, 5, 6, 7, 8, 8], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))


    def test_47(self):
        input = """Ho,dem,nam: string = nguyen,minh,my;"""
        expect = """Program([
	VarDecl(Ho, StringType, Id(nguyen))
	VarDecl(dem, StringType, Id(minh))
	VarDecl(nam, StringType, Id(my))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))


    def test_48(self):
        input = """f,y : string = footg(5+2-6*1), a(98 == 16) ;"""
        expect = """Program([
	VarDecl(f, StringType, FuncCall(footg, [BinExpr(-, BinExpr(+, IntegerLit(5), IntegerLit(2)), BinExpr(*, IntegerLit(6), IntegerLit(1)))]))
	VarDecl(y, StringType, FuncCall(a, [BinExpr(==, IntegerLit(98), IntegerLit(16))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))


    def test_49(self):
        input = """a,b: auto = 3.4,6.7;"""
        expect = """Program([
	VarDecl(a, AutoType, FloatLit(3.4))
	VarDecl(b, AutoType, FloatLit(6.7))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_50(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))


    def test_51(self):
        input = """sum:function float(arr: array [2] of float,res: integer){
            i, sum: integer;
            sum = 0;
            for (i = 0, i < n, i + 1) {
                sum = sum + n[i];
            }
            return sum;
        }"""
        expect = """Program([
	FuncDecl(sum, FloatType, [Param(arr, ArrayType([2], FloatType)), Param(res, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(sum, IntegerType), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(n, [Id(i)])))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))


    def test_52(self):
        input = """count: function integer () {
            while (a-3>=12){
                abc : integer = a+4342;}
        }"""
        expect = """Program([
	FuncDecl(count, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), BlockStmt([VarDecl(abc, IntegerType, BinExpr(+, Id(a), IntegerLit(4342)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))


    def test_53(self):
        input = """foo23: function array[13] of boolean () {
            if (i>10) i=i+1;
            x = y+3;
        }"""
        expect = """Program([
	FuncDecl(foo23, ArrayType([13], BooleanType), [], None, BlockStmt([IfStmt(BinExpr(>, Id(i), IntegerLit(10)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), AssignStmt(Id(x), BinExpr(+, Id(y), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))


    def test_54(self):
        input = """foo: function void () {
            a[12,34,45,12,35,53]= "";
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(12), IntegerLit(34), IntegerLit(45), IntegerLit(12), IntegerLit(35), IntegerLit(53)]), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))


    def test_55(self):
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
        expect = """Program([
	VarDecl(xa, IntegerType, IntegerLit(6523))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(323)])), CallStmt(inc, Id(xyx), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))


    def test_56(self):
        input = """// // // main function */
            ac : float = 0.12;
            str : auto = "ac";
            main: function float () {
                a = "it's dark inside" :: "it's where my demon hide";
            }"""
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(0.12))
	VarDecl(str, AutoType, StringLit(ac))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(it's dark inside), StringLit(it's where my demon hide)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))


    def test_57(self):
        input = """find_gcd:function integer(n1: integer,n2: integer)
        {
            if (n2 != 0)
            return find_gcd(n2, n1%n2);
            else return n1;
        }"""
        expect = """Program([
	FuncDecl(find_gcd, IntegerType, [Param(n1, IntegerType), Param(n2, IntegerType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(n2), IntegerLit(0)), ReturnStmt(FuncCall(find_gcd, [Id(n2), BinExpr(%, Id(n1), Id(n2))])), ReturnStmt(Id(n1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))


    def test_58(self):
        input = """a: float;
        b: array [2] of integer;
        main: function void (){
            c : integer;
            a = a * b[0] + (a - 3) * b[1];
        }"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, ArrayType([2], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, IntegerType), AssignStmt(Id(a), BinExpr(+, BinExpr(*, Id(a), ArrayCell(b, [IntegerLit(0)])), BinExpr(*, BinExpr(-, Id(a), IntegerLit(3)), ArrayCell(b, [IntegerLit(1)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))


    def test_59(self):
        input = """main: function void (){
            k,c: integer;
            do{
                do{
                    c: array [3] of integer;
                } while (x < 4);
            } while (k == 0);
            return 0;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(k, IntegerType), VarDecl(c, IntegerType), DoWhileStmt(BinExpr(==, Id(k), IntegerLit(0)), BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(4)), BlockStmt([VarDecl(c, ArrayType([3], IntegerType))]))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))


    def test_60(self):
        input = """main: function void (){
            do {
                x = x + 3;
            } while (true);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(3)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    def test_61(self):
        input = """main: function void (){
                    while(x<9){
                        a = a + 1;
                        _ = !x || (y == 0) && (z > 12.5E-6);
                    }
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(9)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(_), BinExpr(&&, BinExpr(||, UnExpr(!, Id(x)), BinExpr(==, Id(y), IntegerLit(0))), BinExpr(>, Id(z), FloatLit(1.25e-05))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))


    def test_62(self):
        input = """main: function void (){
                    for (i = 0,i<10 ,i+1) {
                        a=a+2;
                    }
                    printInteger(a);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))


    def test_63(self):
        input = """main: function void (){
                    for (i = 0, i < 10,i+1) {
                        a=a+2;
                    }
                    printInteger(a);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2)))])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))


    def test_64(self):
        input = """main: function void(){
            if (flag == 0) x = 5;
            else if (flag == 1) x = 6;
            else x = 7;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(flag), IntegerLit(0)), AssignStmt(Id(x), IntegerLit(5)), IfStmt(BinExpr(==, Id(flag), IntegerLit(1)), AssignStmt(Id(x), IntegerLit(6)), AssignStmt(Id(x), IntegerLit(7))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))


    def test_65(self):
        input = """main: function void (){
                for (i = 0, i < 10,i+1) printInteger(i);
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))


    def test_66(self):
        input = """main: function void (){
           {
                {
                    {
                        {
                            {
                                t:integer;
                                {
                                    return 0;
                                }
                                a = 1+2;
                            }
                        }
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([VarDecl(t, IntegerType), BlockStmt([ReturnStmt(IntegerLit(0))]), AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(2)))])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))


    def test_67(self):
        input = """main: function void (){
                    {a, b:integer = 2,3;
                        {
                            c, d:integer = 2,3;
                        }
                    }
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), VarDecl(b, IntegerType, IntegerLit(3)), BlockStmt([VarDecl(c, IntegerType, IntegerLit(2)), VarDecl(d, IntegerType, IntegerLit(3))])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))


    def test_68(self):
        input = """swap: function void (a: integer,b:integer){
                temp: integer =a;
                a=b;
                b=temp;
            }"""
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))


    def test_69(self):
        input = """
        main: function void(){
            //a:integer;
        }
        func: function void(a:array [1] of integer,arr: string){
            return 0;
        }
        test: function integer(input: array [10] of float,a:integer,c: array [10] of string,d:boolean){
            a, b, c:integer;
            // Comment
            // int c;
            return a;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(func, VoidType, [Param(a, ArrayType([1], IntegerType)), Param(arr, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	FuncDecl(test, IntegerType, [Param(input, ArrayType([10], FloatType)), Param(a, IntegerType), Param(c, ArrayType([10], StringType)), Param(d, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))


    def test_70(self):
        input = """swap: function void (arr: array[5] of integer, i: integer, j: integer) {
            temp: integer;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        """
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(arr, ArrayType([5], IntegerType)), Param(i, IntegerType), Param(j, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType), AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))


    def test_71(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 371))


    def test_72(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))


    def test_73(self):
        input = """main:function void(){
            a : integer;
            a=5;
            writeln(a / 2);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(5)), CallStmt(writeln, BinExpr(/, Id(a), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))


    def test_74(self):
        input = """main:function void(){
            i:integer;
            for (i=0, i < 10, i + 1) {
                writeln(i);
                if (i==5) continue;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeln, Id(i)), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))


    def test_75(self):
        input = """main:function void(){
            if(true) {
                if(true) {
                    if(true) {
                        if(true) {
                            writeBoolean(true);
                        }
                    }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([CallStmt(writeBoolean, BooleanLit(True))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))


    def test_76(self):
        input = """main:function void(){
        i:integer;
        for (i=0, i < 10, i + 2)
            {
                writeln(i);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(writeln, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))


    def test_77(self):
        input = """main:function void(){
            a : integer;
            a = 10;
            while (a < 20) {
                writeln(a);
                a = a+1;
                if(a == 15)
                    break;
            }   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), IntegerLit(10)), WhileStmt(BinExpr(<, Id(a), IntegerLit(20)), BlockStmt([CallStmt(writeln, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(15)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))


    def test_78(self):
        input = """main: function boolean () {
                a = True;
                printBoolean(a);
            }""" 
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([AssignStmt(Id(a), Id(True)), CallStmt(printBoolean, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))


    def test_79(self):
        input = """main: function boolean (k: boolean) {
            sad(k);
            readInteger();
            }""" 
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(k, BooleanType)], None, BlockStmt([CallStmt(sad, Id(k)), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))


    def test_80(self):
        input = """
            a: integer = func(10);
            main: function string () {
                for(i = 3, i <= 10, i + 1) {
                    sum = sum + i;
                }
                print("I Love you");
            }
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(func, [IntegerLit(10)]))
	FuncDecl(main, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))])), CallStmt(print, StringLit(I Love you))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))


    def test_81(self):
        input = """main: function void (a: boolean) {
                    if (isPrime(7))
                        print("7 is prime");
                    else
                        print("7 is not prime");
                }

                func: function boolean (n: integer)  {
                    if (n <= 1)
                        return false;
                    for (i = 2, i <= n / 2, i + 1) {
                        if (n % i == 0)
                            return false;
                    }
                    return true;
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, BooleanType)], None, BlockStmt([IfStmt(FuncCall(isPrime, [IntegerLit(7)]), CallStmt(print, StringLit(7 is prime)), CallStmt(print, StringLit(7 is not prime)))]))
	FuncDecl(func, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))


    def test_82(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
            a : integer = "hello world";
            c : float = 812.123e-10;
        """
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]))
	VarDecl(a, IntegerType, StringLit(hello world))
	VarDecl(c, FloatType, FloatLit(8.12123e-08))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    def test_83(self):
        input = """flot: integer = 10;"""
        expect = """Program([
	VarDecl(flot, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
    def test_84(self):
        input = """
            main : function void (inherit out delta : integer){
                if (n != 0 ) return 1;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(delta, IntegerType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    def test_85(self):
        input = """
            /* main function */
            delta : boolean = true;
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (i = 0, i < 5, i +1 ){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = """Program([
	VarDecl(delta, BooleanType, BooleanLit(True))
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(var, StringType, BinExpr(::, StringLit(hello), StringLit(world)))]), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(&&, Id(n), IntegerLit(0)), BlockStmt([WhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(&&, BinExpr(+, Id(a), IntegerLit(123)), BinExpr(-, BinExpr(-, Id(b), BinExpr(*, IntegerLit(10), IntegerLit(18))), IntegerLit(19))))]))]))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 385))
    def test_86(self):
        input = """diffEq2: function void (a: float, b: float, c: float) {
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        print("The differential equation has no real solutions.");
    } else {
        if (delta == 0) {
            x0 = -b / (2 * a);
            y0 = f(x0);
            print("The differential equation has one real solution: y(x) = ", y0, " for x = ", x0);
        }
        else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            y1 = f(x1);
            y2 = f(x2);
            print("The differential equation has two real solutions: y(x) = ", y1, " for x = ", x1, " and y(x) = ", y2, " for x = ", x2);
        }
    }
}
f: function float (x: float) {
        return exp(x) + exp(-x);
}
main: function void () {
    a = 1;
    b = 0;
    c = -1;
    diffEq2(a, b, c, f);
}"""
        expect = """Program([
	FuncDecl(diffEq2, VoidType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(The differential equation has no real solutions.))]), BlockStmt([IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x0), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(y0), FuncCall(f, [Id(x0)])), CallStmt(print, StringLit(The differential equation has one real solution: y(x) = ), Id(y0), StringLit( for x = ), Id(x0))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(y1), FuncCall(f, [Id(x1)])), AssignStmt(Id(y2), FuncCall(f, [Id(x2)])), CallStmt(print, StringLit(The differential equation has two real solutions: y(x) = ), Id(y1), StringLit( for x = ), Id(x1), StringLit( and y(x) = ), Id(y2), StringLit( for x = ), Id(x2))]))]))]))
	FuncDecl(f, FloatType, [Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(exp, [Id(x)]), FuncCall(exp, [UnExpr(-, Id(x))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(0)), AssignStmt(Id(c), UnExpr(-, IntegerLit(1))), CallStmt(diffEq2, Id(a), Id(b), Id(c), Id(f))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
    def test_87(self):
        input = """
            /* main function */
            main: function float () {}
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    def test_88(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
    def test_89(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
    def test_90(self):
        input = """
coinChange: function void(coins: array[4] of integer, n: integer) {
    dp: array[100] of integer;
    for (i = 1, i <= n, i + 1) {
        dp[i] = INF;
    }
    
    for (i = 1, i <= n, i + 1) {
        for (j = 0, j < 4, j + 1) {
            if ((coins[j] <= i) && ((dp[i - coins[j]] + 1) < dp[i])) {
                dp[i] = dp[i - coins[j]] + 1;
            }
        }
    }
    
    print("Minimum number of coins required to make change for ", n, " is: ", dp[n]);
}

main: function void() {
    coins = {1, 3, 5, 7};
    n = 12;

    coinChange(coins, n);
}"""
        expect = """Program([
	FuncDecl(coinChange, VoidType, [Param(coins, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(dp, ArrayType([100], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), Id(INF))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(<=, ArrayCell(coins, [Id(j)]), Id(i)), BinExpr(<, BinExpr(+, ArrayCell(dp, [BinExpr(-, Id(i), ArrayCell(coins, [Id(j)]))]), IntegerLit(1)), ArrayCell(dp, [Id(i)]))), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), BinExpr(+, ArrayCell(dp, [BinExpr(-, Id(i), ArrayCell(coins, [Id(j)]))]), IntegerLit(1)))]))]))])), CallStmt(print, StringLit(Minimum number of coins required to make change for ), Id(n), StringLit( is: ), ArrayCell(dp, [Id(n)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(coins), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(7)])), AssignStmt(Id(n), IntegerLit(12)), CallStmt(coinChange, Id(coins), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    def test_91(self):
        input = """fibonacciSum: function integer(n: integer) {
    if (n <= 0) {
        return 0;
    } 
    else {
        if (n == 1) {
            return 1;
        }
        else {
            prev1 = 0;
            prev2 = 1;
            sum = 1;
            for (i = 2, i <= n, i+1) {
                current = prev1 + prev2;
                sum = sum + current;
                prev1 = prev2;
                prev2 = current;
            }
            return sum;
        }
    }
}

main: function void() {
    n = 10;
    result = fibonacciSum(n);
    print("The sum of the first " + n + " Fibonacci numbers is " + result);
}"""
        expect = """Program([
	FuncDecl(fibonacciSum, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([AssignStmt(Id(prev1), IntegerLit(0)), AssignStmt(Id(prev2), IntegerLit(1)), AssignStmt(Id(sum), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(current), BinExpr(+, Id(prev1), Id(prev2))), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(current))), AssignStmt(Id(prev1), Id(prev2)), AssignStmt(Id(prev2), Id(current))])), ReturnStmt(Id(sum))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(result), FuncCall(fibonacciSum, [Id(n)])), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(The sum of the first ), Id(n)), StringLit( Fibonacci numbers is )), Id(result)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    def test_92(self):
        input = """insertionSort: function void(arr: array[10] of integer) {
    for (i = 1, i < 10, i+1) {
        key = arr[i];
        j = i - 1;
        while ((j >= 0) && (arr[j] > key)) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

printArray: function void(arr: array[10] of integer) {
    for (i = 0, i < 10, i+1) {
        printInt(arr[i]);
        print(" ");
    }
    print("\\n");
}

main: function void() {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    print("Original array: ");
    printArray(arr);
    insertionSort(arr);
    print("Sorted array: ");
    printArray(arr);
}"""
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
	FuncDecl(printArray, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(arr, [Id(i)])), CallStmt(print, StringLit( ))])), CallStmt(print, StringLit(\\n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), CallStmt(print, StringLit(Original array: )), CallStmt(printArray, Id(arr)), CallStmt(insertionSort, Id(arr)), CallStmt(print, StringLit(Sorted array: )), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    def test_93(self):
        input = """combination: function integer (n: integer, k: integer) {
    if ((k == 0) || (k == n)) {
        return 1;
    } else {
        return combination(n - 1, k - 1) + combination(n - 1, k);
    }
}

main: function void () {
    n = 5;
    k = 3;
    result = combination(n, k);
    printInt(result);
}"""
        expect = """Program([
	FuncDecl(combination, IntegerType, [Param(n, IntegerType), Param(k, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(k), IntegerLit(0)), BinExpr(==, Id(k), Id(n))), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(combination, [BinExpr(-, Id(n), IntegerLit(1)), BinExpr(-, Id(k), IntegerLit(1))]), FuncCall(combination, [BinExpr(-, Id(n), IntegerLit(1)), Id(k)])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(5)), AssignStmt(Id(k), IntegerLit(3)), AssignStmt(Id(result), FuncCall(combination, [Id(n), Id(k)])), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    def test_94(self):
        input = """solveQuadratic: function void (a: float, b: float, c: float) {
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        printString("No real roots");
    } else {
        if (delta == 0) {
            x = -b / (2 * a);
            printString("One real root: ");
            printFloat(x);
        }
        else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            printString("Two real roots: ");
            printFloat(x1);
            printString(", ");
            printFloat(x2);
        }
    }
}

main: function void () {
    a = 2;
    b = -3;
    c = -4;
    solveQuadratic(a, b, c);
}"""
        expect = """Program([
	FuncDecl(solveQuadratic, VoidType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(No real roots))]), BlockStmt([IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(One real root: )), CallStmt(printFloat, Id(x))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(Two real roots: )), CallStmt(printFloat, Id(x1)), CallStmt(printString, StringLit(, )), CallStmt(printFloat, Id(x2))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), UnExpr(-, IntegerLit(3))), AssignStmt(Id(c), UnExpr(-, IntegerLit(4))), CallStmt(solveQuadratic, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_95(self):
        input = """binarySearch: function integer (arr: array [10] of integer, target: integer) {
    left = 0;
    right = 9;
    while (left <= right) {
        mid = (left + right) / 2;
        if (arr[mid] == target) {
            return mid;
        } else {
            if (arr[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
    }
    return -1;
}"""
        expect = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(left), IntegerLit(0)), AssignStmt(Id(right), IntegerLit(9)), WhileStmt(BinExpr(<=, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([ReturnStmt(Id(mid))]), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1)))]))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_96(self):
        input = """complex: array[1,2,3] of integer = CountPP[1,a[2,b[3,c[4],d[5]]]];"""
        expect = """Program([
	VarDecl(complex, ArrayType([1, 2, 3], IntegerType), ArrayCell(CountPP, [IntegerLit(1), ArrayCell(a, [IntegerLit(2), ArrayCell(b, [IntegerLit(3), ArrayCell(c, [IntegerLit(4)]), ArrayCell(d, [IntegerLit(5)])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_97(self):
        input = """a, b, c, d, e,f : integer = a[1], b[2,3,4], c[5], d[12], e[18,22,"haha"], v[2];"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, IntegerType, ArrayCell(b, [IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(c, IntegerType, ArrayCell(c, [IntegerLit(5)]))
	VarDecl(d, IntegerType, ArrayCell(d, [IntegerLit(12)]))
	VarDecl(e, IntegerType, ArrayCell(e, [IntegerLit(18), IntegerLit(22), StringLit(haha)]))
	VarDecl(f, IntegerType, ArrayCell(v, [IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    def test_98(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                /*tran khac chan nam qua xa, */ \n //ve day voi nhau hai dua dap chung men*/ abcxyz
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))


    def test_99(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = 1_23_1414_214;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1231414214))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))




