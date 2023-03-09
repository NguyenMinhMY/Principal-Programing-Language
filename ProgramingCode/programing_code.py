from abc import ABC
class Exp(ABC): 
    pass

class BinExp(Exp):
    def __init__(self, op1,op,op2):
        self.op1 = op1
        self.op = op
        self.op2 = op2
    def eval(self):
        left = self.op1.eval()
        right = self.op2.eval()
        if self.op == "+":
            return left + right
        elif self.op == "-":
            return left - right
        elif self.op == "/":
            return left / right
        elif self.op == "*":    
            return left * right
    def printPrefix(self):
        symbol = '.' if self.op != '*' else ''
        return self.op + symbol + ' ' + self.op1.printPrefix() + ' ' + self.op2.printPrefix()
        
class UnExp(Exp):
    def __init__(self,op,o):
        self.op = op
        self.o = o
    def eval(self):
        val = self.o.eval()
        if self.op == "-":
            return -val
        elif self.op == "+":
            return +val
    def printPrefix(self):
        symbol = '.' if self.op == '-' else ''
        return self.op + symbol + ' ' + self.o.printPrefix()
        
class IntLit(Exp):
    def __init__(self,x):
        self.x = x
    def eval(self):
        return self.x
    def printPrefix(self):
        return str(self.x)
        
class FloatLit(Exp):
    def __init__(self,x):
        self.x = x
        
    def eval(self):
        return self.x
    def printPrefix(self):
        return str(self.x)