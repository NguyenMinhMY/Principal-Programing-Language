import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """ a: integer = 1;
                    main: function void () {
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1(self):
        input = """ a: integer = 1;
                    b: auto = c + 1;
                    main: function void () {

                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """ a: float = 1 + 2.0;
                    b: auto = a + 1;
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """ main1: function integer () {
                    }
                    a: integer = 1;
                    b: auto = a + 1;
                    c: auto = a + main1();
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """ alo: function float () {
                    }
                    a: integer = 1;
                    b: auto = 1.0;
                    c: auto = b + alo();
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """
                    a: array [3] of integer = {1,2,3};
                    b: integer = a[2];
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """ alo: function float (b: string, d: string) {
                        a: integer = c;
                    }
                    a: boolean = true;
                    c: integer = 1;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = (
            """Undeclared Identifier: c"""
        )
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """ alo: function float (b: string, c: string) {
                        a = b;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """ alo: function float (b: string, b: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Redeclared Parameter: b"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }

                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 + 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }

                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(3), IntegerLit(2)), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """ alo: function float (b: string, c: boolean) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Type mismatch in statement: AssignStmt(Id(c), IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c + 3, c + 1){
                           c = c + 1;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1;
                        }
                        break;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {

                    }
                    """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
                    alo: function float (c: integer){

                    }
                    a: float = alo(7.4) + 5;
                    main: function void () {

                    }
                """
        expect = """Type mismatch in expression: FuncCall(alo, [FloatLit(7.4)])"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
                    a: integer = main1(7) + 5;
                    main1: function integer (c: integer){

                    }
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
                    a: float = main1(7) + 5;
                    foo: function integer(c: float){

                    }
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
                    a: float = main1(7) + 5;
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){

                    }
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        boo(6.5);
                    }
                    foo: function integer(c: float){
                    }
                    main: function void () {
                    }
                """
        expect = """Undeclared Function: boo"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){

                    }
                    main2: function integer () inherit main1 {
                        preventDefault();
                        c = c + 1;
                    }
                    main: function void () {

                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
                    main2: function integer () inherit main1 {
                    super(1);
                        c = c + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){

                    }
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
                    main2: function integer () inherit main1 {
                        d = d + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer, d: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){

                    }
                    main: function void () {

                    }
                """
        expect = """Invalid statement in function: main2"""
        input = """
        foo: function integer() inherit foo1 {
            super(1);
        }
        foo1: function integer (inherit a: integer, inherit b: integer) {}"""
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
                    main2: function integer () inherit main1 {
                        d = c + 1;
                    }
                    a: float = main1(7,8) + 5;
                    main1: function float (inherit c: integer, inherit d: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){

                    }
                    main: function void () {

                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
                    foo: function auto (a: integer, b: integer){

                    }
                    a: float = foo(1,2);
                    c: float = a + 2;
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
                    foo: function auto (a: integer, b: integer){

                    }
                    a: float = foo(1,2);
                    b: integer = foo(1,2) + 1;
                    c: float = a + 2;
                    main: function void () {

                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
                    foo: function auto (a: integer, b: integer){

                    }
                    b: integer = foo(1,2) + 1;
                    a: integer = foo(1,2);
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
                    foo: function auto (a: integer, b: integer){

                    }
                    b: float = (foo(1,2) + 1.0) * (foo(1,2) + 1);
                    main: function void () {

                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input ="""
      
      sumNumbers: function integer() {
            sum: integer = 0;
            i: integer = 1;
            n: integer= 20;
            do {
                sum = sum + i;
                i = i + 1;
            } while (i <= n);
            return sum;
        }
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_31(self):
        input ="""
      
       findMax: function integer(a: array[5] of integer) {
           
            max: integer = a[0];
            i: integer;
            for (i=1, i<= 4, i+1)
            {
                z: integer = 0;
                z= 10;



                if (a[i] > max) 
                {
                    
                    return;
                    
                    
                }
                    max = a[i];
               
                
            }
            return max;
                
            
        }
 
        
"""











        expect="Type mismatch in statement: ReturnStmt()"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test32(self):
        input ="""
      
       isEven: function boolean(n: integer) {
            if ((n%2)==0) 
                return true;
            else
                return false;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_33(self):
        input ="""
      
      isEven: function boolean(n: integer) {
            if (n * 2 == 0) 
                return true;
            else
                return false;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_34(self):
        input ="""
      factorial: function integer(n: integer) {
            if (n == 0) 
                return 1;
            else
                return n * factorial(n - 1);
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_35(self):
        input ="""
        gcd: function integer(a: integer, b: integer) {
             r: integer = a % b;
            while (b != 0) {
             
                a = b;
                b = r;
            }
                
            return a;
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input ="""
      
      convertToBinary: function string(n: integer) {
            s: string = "";
            while (n > 0) 
            {
             if (n % 2 == 0) 
                    s = "0" + s;
                else
                    s = "1" + s;
                n = n / 2;
            
            }
               
            return s;
        }
 
        
"""



        expect="Type mismatch in expression: BinExpr(+, StringLit(0), Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input ="""
      
       printMultiplicationTable: function void(i: integer) {
            for (i=1, i<10,i + 1)
             {
                for (j=1, j<10,j + 1)
                    {
                    write(i*j + " ");
                    }
             } 
                
                writeln("");
        }
 
        
"""



        expect="Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_38(self):
        input ="""
      fibonacci: function integer(n: integer) {
            if (n == 0) 
                return 0;
            else
                if (n == 1) 
                    return 1;
                else
                    return fibonacci(n - 1) + fibonacci(n - 2);
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_39(self):
        input ="""
      
       isPrime: function boolean(n: integer) {
            if (n <= 1) 
                return false;
            else
                  for (i=1, i<10,i + 1)
             {
                for (j=1, j<10,j + 1)
                    {
                    write(i*j + " ");
                    }
             }
            return true;
        }
    
 
        
"""



        expect="Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self): # xem lại testcase  này
        input ="""
      
      findMin: function integer(a: array[5] of integer) {
            min: integer = a[0];
            i: float; 
            for (i=1,i<10,i+1)
             {
             if (a[i] < min) 
                    min = a[i];
             
             } 
                
            return min;
        }
 
        
"""



        expect="Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(a, [Id(i)])))]))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_41(self):
        input ="""
      
      foo1: function auto (a: integer, a: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (inherit a: integer, inherit b: integer)
    {
        
    }
 
        
"""



        expect="Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_42(self):
        input ="""
      
      foo1: function auto (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (a: integer, b: integer)
    {
        
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_43(self):
        input ="""
      
      
 foo1: function auto (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (a: integer, b: integer) inherit t
    {
        
    }
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_44(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return true;
    } 
    foo: function void (a: integer, b: integer)
    {
        
    } 
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_45(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return b;
    } 
    foo: function void (a: integer, b: integer)
    {
        c: integer;
        c = foo1(3, 4);
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 445))   
    def test_46(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return b;
    } 
    foo: function void (a: integer, b: integer)
    {
        c: float;
        c = foo1(3, 4);
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_47(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
    super(2, 3);
    if (a == 1) return 1;
    a = 1;
    b = a + b;
     c: float;
    for (b=1, b<=c, b + 2)
    {
     if (a==b) return 1;
     else break;
    }
    return b;
}

foo: function void(a: integer, b: integer) {
    // function body here
}
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 447))    
    def test_48(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_49(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_50(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3.1);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test51(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
            func1(x, y);
            func1(y, x);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_52(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
            x: integer = 1;
             y: float = 2.0;
            func1(x, y);
            func1(y, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test53(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: string = "abc";
            func1(x, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_54(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
             z: boolean = true;
            func1(x, y);
            func1(z, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(z), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_55(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
            func1(x);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_56(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
            func1(x, y, x);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(x), Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
            x: integer = 1;
             y: float = 2.0;
            func1(x);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input ="""
      
       foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
             c: float;
            do
            {
                z: integer= 10;
            }
            while(b==1);
            for (b=1, b<=c, b + 2)
            {
            continue;
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_59(self):
        input ="""
      
      foo: function void() {
            return;
        }
 
        
"""

        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_60(self):
        input = """
      
        foo: function void() {
            x: integer = 1;
            y: float = 2.5;
            return;
        }"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """main: function void (){
                    while(x<9){
                        a = a + 1;
                        _ = !x || (y == 0) && (z > 12.5E-6);
                    }
                }"""
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 461))


    def test_62(self):
        input = """main: function void (){
                    for (i = 0,i<10 ,i+1) {
                        a=a+2;
                    }
                    printInteger(a);
                }"""
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 462))


    def test_63(self):
        input = """main: function void (){
                    for (i = 0, i < 10,i+1) {
                        a=a+2;
                    }
                    printInteger(a);
                }"""
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 463))


    def test_64(self):
        input = """main: function void(){
            if (flag == 0) x = 5;
            else if (flag == 1) x = 6;
            else x = 7;
        }"""
        expect = """Undeclared Identifier: flag"""
        self.assertTrue(TestChecker.test(input, expect, 464))


    def test_65(self):
        input = """main: function void (){
                for (i = 0, i < 10,i+1) printInteger(i);
                }"""
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 465))


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
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 466))


    def test_67(self):
        input = """main: function void (){
                    {a, b:integer = 2,3;
                        {
                            c, d:integer = 2,3;
                        }
                    }
                }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 467))


    def test_68(self):
        input = """swap: function void (a: integer,b:integer){
                temp: integer =a;
                a=b;
                b=temp;
            }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 468))


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
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 469))


    def test_70(self):
        input = """swap: function void (arr: array[5] of integer, i: integer, j: integer) {
            temp: integer;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 470))


    def test_71(self):
        input = """x: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 471))


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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 472))


    def test_73(self):
        input = """main:function void(){
            a : integer;
            a=5;
            writeln(a / 2);
        }
        """
        expect = """Undeclared Function: writeln"""
        self.assertTrue(TestChecker.test(input, expect, 473))


    def test_74(self):
        input = """main:function void(){
            i:integer;
            for (i=0, i < 10, i + 1) {
                writeln(i);
                if (i==5) continue;
            }
        }
        """
        expect = """Undeclared Function: writeln"""
        self.assertTrue(TestChecker.test(input, expect, 474))



    def test_75(self):
        input = """
        a: integer = 134;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_76(self):
        input = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer) {
            return a + b;
        }
        main: function void() {
            printInteger(a);
        }
        """
        except_str = "Type mismatch in statement: CallStmt(printInteger, Id(a))"
        self.assertTrue(TestChecker.test(input, except_str, 476))
        
    def test_77(self):
        input = """
        x : auto={4,5,6};
        y:  auto=x[1,2];
        """
        except_str = "Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, except_str, 477))
        
    def test_78(self):
        input = """
        a: array[2,2] of integer;
        b: array[2] of integer = a[0];
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input, except_str, 478))
        
    def test_79(self):
        input = """
            arr: array [2,2,2,2] of integer = {
                {
                    { {1, 2}, {3, 4} },
                    { {5, 6}, {7, 8} }
                },
                {
                    { {9, 10}, {11, 12} },
                    { {13, 14}, {15, 16} }
                }
            };
            a : array[2] of integer = arr[0,3,1];
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input, except_str, 479))
        
    def test_80(self):
        input = """
        foo: function integer(a:auto, b:auto){
            x:integer = a + 1;
            y:string = b :: "abc";
            return x + 1;
        }
        main:function void(){
            foo(1, 2);
            foo2("abc", "abc");
        }
        foo2: function integer(a:auto, b:auto){
            x:integer = a + 1;
            y:string = b :: "abc";
        }
        """
        except_str = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, except_str, 480))
        
    def test_81(self) :
        input = """
        func: function integer() {
            a: integer = 12;
            return 3;
            a: float = 14;
        }
        """
        except_str = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, except_str, 481))
        
    def test_82(self):
        input = """
        func: function integer(a: integer) {
            if (a < 13) return 16;
            else a = a + 1;
            a: float = 12; 
            return 10;
        }
        """
        except_str = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, except_str, 482))
        
    def test_83(self):
        input = """
        foo: function integer(){}
        main: function void(){
            foo: integer = 3;
            a: integer;
            a = foo(); // line 5
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 483))
        
    def test_84(self):
        input = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
            super(a);
        }
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, except_str, 484))
        
    def test_85(self):
        input = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        """
        except_str = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, except_str, 485))
    
    def test_86(self):
        input = """
        a: float;
        main: function integer (n: integer) {
            a: integer;
            printInteger(a);
            {
                a: boolean;
                printBoolean(a);
                {
                    a: string;
                    printString(a);
                    {
                        printString(a);
                    }
                }
            }
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test_87(self) :
        input = """
            main: function void () {
            a : integer;
            b : integer;
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s : string = "Hello";
                printString(s);
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 487))
        
    def test_88(self):
        input = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
                low : integer = 0;
                high : integer = 9;
                while (low <= high) {
                    mid : integer = (low + high) / 2;
                    if (arr[mid] == target) {
                        return mid;
                    } else if (arr[mid] < target) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                return -1;
            }
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input, except_str, 488))
        
    def test_89(self):
        input = """
        rotate : function void (nums : array[7] of integer, k : integer) {
            n : integer = 7;
            k = k % n;
            if (k == 0) {
                return;
            }
            reverse(nums, 0, n - 1);
            reverse(nums, 0, k - 1);
            reverse(nums, k, n - 1);
        }
        main: function void () {
            nums : array [7] of integer = {1, 2, 3, 4, 5, 6, 7};
            k : integer = 3;
            rotate(nums, k);
        }
        """
        except_str = "Undeclared Function: reverse"
        self.assertTrue(TestChecker.test(input, except_str, 489))
        
    def test_90(self):
        input = """
        main : function void() {
            do {
                printString("Hello");
            }
            while (true);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 490))
        
    def test_91(self) :
        input = """
        strings: array [2,3,2] of string = {{{"1","2"},{"1","2"},{"1","1"}},{{"1","1"},{"1","1"},{"1","1"}}};
        main : function void() {}
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 491))
    
    def test_92(self) :
        input = """
        main : function void() {
            a : integer = foo() + 2;
            b : float = goo() + 2.3;
        }
        foo : function auto() {
            return 1;
        }
        goo : function auto() {
            return "2";
        }
        """
        except_str = "Type mismatch in statement: ReturnStmt(StringLit(2))"
        self.assertTrue(TestChecker.test(input, except_str, 492))

    def test_93(self) :
        input = """
        foo : function auto() {
            return 1;
        }
        goo : function auto() {
            return "2";
        }
        main : function void() {
            a : float = foo() + 2.3;
            b : string = goo() :: "a";
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 493))
        
    def test_94(self) :
        input = """
        foo : function auto() {
            if (true) {
                return 1;
            }
            else return 2;
            return 1;
            return "asfasF";
        }
        goo : function auto() {
            return "2";
        }
        main : function void() {
            a : float = foo() + 2.3;
            b : string = goo() :: "a";
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 494))
        
    def test_95(self) :
        input = """
        x : auto = 2 + 3.4;
        main : function void() {
            {
                x : string = "a";
                printString(x);
            }
            printFloat(x);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 495))
    
    def test_96(self) :
        input = """
        main : function void() {
            i : integer ; 
            for (i = 0 , i < 10 , i +1 ) {
                continue;
            }
            break;
        }
        """
        except_str = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, except_str, 496))
    
    def test_97(self) :
        input = """
        main : function void() {
            i : integer ; 
            for (i = 0 , i < 10 , i +1 ) {
                if (i == 5) {
                    break;
                    if (true) {
                        continue;
                    }
                }
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input, except_str, 497))
        
    def test_98(self) :
        input = """a : array[2] of integer = {1,2,3};"""
        except_str = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, except_str, 498))
        
    def test_99(self) :
        input = """
        a : array[2,3] of integer = {{1,2,3},{4,5,6}};
        b : array[3] of integer = a[1.0];
        """
        except_str = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input, except_str, 499))
        

