from Visitor import Visitor
from StaticError import *
from AST import *

class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
class Symbol(AST):
    def __init__(self, name, return_type, params):
        self.name = name
        self.return_type = return_type
        self.params = params
class GetEnv(Visitor):
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                param = self.visit(decl, param)
        return param

    def visitFuncDecl(self, ast, param):            
        param += [ast]
        return param

class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast
        
        self.isInLoop = False
        self.utl = Utils()
        self.curFunc = None # [curFunc, parentFunc]
        self.curBlock = 0
        self.isFirstReturn = None
        self.isRetOfIfElse = None
        self.global_syms = [Symbol("readInteger",IntegerType(), []),
                            Symbol("printInteger", VoidType(), [ParamDecl('a',IntegerType())]),
                            Symbol("readFloat", FloatType(), []),
                            Symbol("printFloat", VoidType(), [ParamDecl('a',FloatType())]),
                            Symbol("readBoolean", BooleanType(), []),
                            Symbol("printBoolean", VoidType(), [ParamDecl('a',BooleanType())]),
                            Symbol("readString", StringType(), []),
                            Symbol("printString", VoidType(), [ParamDecl('a',StringType())]),
                            Symbol("super", VoidType(), [Expr()]),
                            Symbol("preventDefault", VoidType(), [])
                            ]

        self.g = self.global_syms + GetEnv(self.ast).check()
    
    def check(self):
        return self.visitProgram(self.ast, [self.global_syms])
    
    def visitIntegerType(self, ast, param):
        return IntegerType()
    def visitFloatType(self, ast, param):
        return FloatType()
    def visitBooleanType(self, ast, param): 
        return BooleanType()
    def visitStringType(self, ast, param): 
        return StringType()
    def visitArrayType(self, ast, param): 
        # dimensions: List[int], typ: AtomicType
        return ArrayType(ast.dimensions, ast.typ)
    def visitAutoType(self, ast, param): 
        return AutoType()
    def visitVoidType(self, ast, param): 
        return VoidType()

    def visitBinExpr(self, ast, param):
        # op: str, left: Expr, right: Expr
        op = ast.op
        lType = self.visit(ast.left, param)
        rType = self.visit(ast.right, param)
        # There is no testcase that both sides of expression have auto type.
        if type(lType) is AutoType and type(rType) is not AutoType: # left is func call or Id
            if type(ast.left) is FuncCall:
                func = self.utl.lookup(ast.left.name, self.g, lambda x: x.name)
                func.return_type = rType
                
            if type(ast.left) is Id:
                for env in param:
                    x = self.utl.lookup(ast.left.name, env, lambda x: x.name)
                    if x is None:
                        continue
                    x.typ = rType
            
            lType = rType
        elif type(rType) is AutoType and type(lType) is not AutoType: # right is func call
            func = self.utl.lookup(ast.right.name, self.g, lambda x: x.name)
            func.return_type = lType
            rType = lType
        
        if op in ['+','-','*','/']:
            if type(lType) in [FloatType, IntegerType] and type(rType) in [FloatType, IntegerType]:
                if type(lType) is FloatType or type(rType) is FloatType:
                    return FloatType()
                return IntegerType()
            raise TypeMismatchInExpression(ast)     

        elif op == '%':
            if type(lType) is IntegerType and type(rType) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        elif op in ['&&','||']:
            if type(lType) is BooleanType and type(rType) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        elif op == '::':
            if type(lType) is StringType and type(rType) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        elif op in ['==','!=']:
            if type(lType) in [IntegerType, BooleanType] and type(rType) in [IntegerType, BooleanType]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
            
        elif op in ['<','>','<=','>=']:
            if type(lType) in [IntegerType, FloatType] and type(rType) in [IntegerType, FloatType]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

    def visitUnExpr(self, ast, param):
        # op: str, val: Expr
        op = ast.op
        et = self.visit(ast.val, param)
        
        if op == '-':
            if type(et) is AutoType:
                if type(ast.val) is FuncCall:
                    return FuncCall(ast.name,[])
                elif type(ast.val) is Id:
                    return ParamDecl(ast.name, AutoType())
            if type(et) in [IntegerType, FloatType]:
                return et
            raise TypeMismatchInExpression(ast)
        elif op == '!':
            if type(et) is AutoType: # val is func call or ID 
                if type(ast.val) is FuncCall:
                    func = self.utl.lookup(ast.val.name, self.g, lambda x: x.name)
                    func.return_type = BooleanType()
                elif type(ast.val) is Id:
                    for env in param:
                        x = self.utl.lookup(ast.val.name, param[0], lambda x: x.name)
                        if x is None:
                            continue
                        if type(x) is ParamDecl:
                            x.typ = BooleanType()
                            break

                return BooleanType()
            if type(et) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
    def visitId(self, ast, param):

        for env in param:
            x =  self.utl.lookup(ast.name, env, lambda x: x.name)
            if x is None:
                continue
            if type(x) in [VarDecl, ParamDecl]:
                return x.typ 
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self, ast, param):
        # name: str, cell: List[Expr]
        for env in param:
            x = self.utl.lookup(ast.name, env, lambda x: x.name)
            if x is None:
                continue

            if type(x.typ) is ArrayType:
                if len(ast.cell) > len(x.typ.dimensions) :
                    raise TypeMismatchInExpression(ast)
                for exp in ast.cell:

                    if type(self.visit(exp, param)) is not IntegerType:
                        raise TypeMismatchInExpression(ast)
                    
                typ = None
                if len(ast.cell) == len(x.typ.dimensions) :
                    typ = x.typ.typ
                elif len(ast.cell) < len(x.typ.dimensions) :
                    typ =  ArrayType(x.typ.dimensions[len(ast.cell):],x.typ.typ)
                # print(typ.__str__())
                return typ

        
        raise Undeclared(Identifier(), ast.name)
        

    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    
    def visitFloatLit(self, ast, param): 
        return FloatType()
    
    def visitStringLit(self, ast, param): 
        return StringType()
    
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    
    def visitArrayLit(self, ast, param): 
        # explist: List[Expr]
        # dimensions = [len(ast.explist)]
        # typ = None
        # {1,2}
        def checkElement(ctx,param):
            if type(ctx) is ArrayLit:
                if ctx.explist == []:
                    return [None,0]
                first = ctx.explist[0] # 1
                firstTyp = checkElement(first, param) # (Integer(), 0)
                dim = [len(ctx.explist)]
                for mem in ctx.explist:
                    typMem = checkElement(mem, param)

                    if type(firstTyp[0]) is type(typMem[0]):

                        if len(firstTyp[1]) != len(typMem[1]):
                            raise IllegalArrayLiteral(ast)
                        
                        for i in range(0, len(firstTyp[1])):

                            if firstTyp[1][i] != typMem[1][i]:
                                raise IllegalArrayLiteral(ast)
                    else:
                        raise IllegalArrayLiteral(ast)
                if firstTyp[1] != [0]:
                    dim += firstTyp[1]
                return (firstTyp[0], dim)
            else:
                typLit = self.visit(ctx, param)
                return (typLit, [0])
        tmp = checkElement(ast, param)
        typ = tmp[0]
        dimensions = tmp[1]
        return ArrayType(dimensions, typ)
        

    
    def visitFuncCall(self, ast, param):
        # name: str, args: List[Expr]

        func = self.utl.lookup(ast.name, self.g, lambda x: x.name)
        if func is None:
            raise Undeclared(Function(), ast.name)

        if len(ast.args) != len(func.params):
            raise TypeMismatchInExpression(ast)
                
        for i in range(len(func.params)):
            typParam = func.params[i].typ
            typArg = self.visit(ast.args[i], param)
            if type(typParam) is AutoType:
                func.params[i].typ = typArg
            elif type(typArg) is AutoType: # args[i] is Func Call or Id (param)
                if type(ast.args[i]) is FuncCall:
                    func = self.utl.lookup(ast.args[i].name, self.g, lambda x: x.name)
                    func.return_type = typParam
                elif type(ast.args[i]) is Id:
                    for env in param:
                        x = self.utl.lookup(ast.args[i].name, env, lambda x: x.name)
                        if x is None:
                            continue
                        if type(x) is ParamDecl:
                            x.typ = typParam
                            break
            elif type(typParam) is not type(typArg):
                raise TypeMismatchInExpression(ast)
        return func.return_type



    def visitAssignStmt(self, ast, param):
        # lhs: LHS, rhs: Expr
        typRHS = self.visit(ast.rhs, param)
        typLHS = self.visit(ast.lhs, param)
        

        if type(ast.rhs) is UnExpr:
            if type(typRHS) is FuncCall:
                func = self.utl.lookup(typRHS.name, self.g, lambda x: x.name)
                if type(typLHS) is FloatType:
                    func.return_type = FloatType()
                    return
                if type(typLHS) is IntegerType:
                    func.return_type = IntegerType()
                    return
                
                raise TypeMismatchInStatement(ast)
            elif type(typRHS) is ParamDecl:
                if type(typLHS) is FloatType:
                    for env in param:
                        x = self.utl.lookup(typRHS.name, env, lambda x: x.name)
                        if x is None:
                            continue
                        if type(x) is ParamDecl:
                            x.typ = FloatType()
                            return
                if type(typLHS) is IntegerType:
                    for env in param:
                        x = self.utl.lookup(typRHS.name, env, lambda x: x.name)
                        if x is None:
                            continue
                        if type(x) is ParamDecl:
                            x.typ = IntegerType()
                            return
                raise TypeMismatchInStatement(ast)
        
        if type(typLHS) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ast)
        if type(typLHS) is not type(typRHS):
            if type(typLHS) is FloatType and type(typRHS) is IntegerType:
                return
            raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast, param): 
        # body: List[Stmt or VarDecl]
        self.curBlock +=1
        self.isFirstReturn = True

        if self.curBlock == 1:    # meaning this block belongs to current Function inherit to parent Fucntion
            if self.curFunc[1] is not None: # curFunc has parentFunc
                firstStmt = None if len(ast.body) == 0 else ast.body[0]
                if firstStmt is None and len(self.curFunc[1].params) > 0:
                    raise InvalidStatementInFunction(self.curFunc[0].name)
                
                if type(firstStmt) is not CallStmt:
                    raise InvalidStatementInFunction(self.curFunc[0].name)

                if firstStmt.name not in ["super", "preventDefault"]:
                    raise InvalidStatementInFunction(self.curFunc[0].name)
                
                if firstStmt.name == "super":
                    paramsPar = self.curFunc[1].params
                    if len(firstStmt.args) > len(paramsPar):
                        raise TypeMismatchInExpression(firstStmt.args[len(paramsPar) - 1])
                    if len(firstStmt.args) < len(paramsPar):
                        raise TypeMismatchInExpression("")
                    for i in range(len(paramsPar)):
                        typParam = paramsPar[i].typ
                        typArg = self.visit(firstStmt.args[i], param)
                        
                        if type(typParam) is AutoType:
                            paramsPar[i].typ = typArg
                    
                        elif type(typArg) is AutoType: # args[i] is Func Call or Id (param)
                            if type(firstStmt.args[i]) is FuncCall:
                                func = self.utl.lookup(firstStmt.args[i].name, self.g, lambda x: x.name)
                                func.return_type = typParam

                            elif type(firstStmt.args[i]) is Id:
                                for env in param:
                                    x = self.utl.lookup(firstStmt.args[i].name, env, lambda x: x.name)

                                    if x is None:
                                        continue

                                    if type(x) is ParamDecl:
                                        x.typ = typParam
                                        break
                        
                        elif type(typParam) is not type(typArg):
                            if type(typParam) is FloatType and type(typArg) is IntegerType:
                                continue
                            else:
                                raise TypeMismatchInExpression("")
                            
                    # append params of parent to local Env
                    for paramdecl in self.curFunc[1].params:
                        if paramdecl.inherit == False:
                            continue
                        checkMatch = self.utl.lookup(paramdecl.name, param[0], lambda x: x.name)
                        if checkMatch is not None:
                            raise Invalid(Parameter(), paramdecl.name)    
                        
                        param[0] = [paramdecl] + param[0]
                
                if firstStmt.name == "preventDefault":
                    if len(firstStmt.args) > 0:
                        raise InvalidStatementInFunction(self.curFunc[0])

                    

            listStmts = ast.body if self.curFunc[1] is None else ast.body[1:]
            for stmt in listStmts:
                if type(stmt) is VarDecl:
                    param = self.visit(stmt, param)
                else:
                    self.visit(stmt, param)
        
        # self.curBlock > 1 
        else:        
            localEnv = [[]] + param
            for stmt in ast.body:
                if type(stmt) is VarDecl:
                    localEnv = self.visit(stmt, localEnv)
                else:
                    self.visit(stmt, localEnv)
        
        self.curBlock -=1

    def visitIfStmt(self, ast, param): 
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None

        typCond = self.visit(ast.cond, param)
        if type(typCond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.tstmt) is ReturnStmt:
            self.isRetOfIfElse = True

        self.visit(ast.tstmt, param)
        
        if type(ast.fstmt) is ReturnStmt:
            self.isRetOfIfElse = True
        if ast.fstmt:
            self.visit(ast.fstmt, param)

        

    def visitForStmt(self, ast, param):
        # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
        # Turn in the loop
        self.isInLoop = True

        self.visit(ast.init, param)
        lhsTyp = self.visit(ast.init.lhs, param)
        if type(lhsTyp) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        typCond = self.visit(ast.cond, param)
        if type(typCond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        typUpd = self.visit(ast.upd, param)
        if type(typUpd) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        
        # go out the loop
        self.isInLoop = False
        return

    def visitWhileStmt(self, ast, param):
        # cond: Expr, stmt: Stmt
        # Turn in the loop
        self.isInLoop = True

        typCond = self.visit(ast.cond, param)
        if type(typCond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)

        # Go out the loop
        self.isInLoop = False
        return

    def visitDoWhileStmt(self, ast, param):
        # cond: Expr, stmt: BlockStmt
        # Turn in the loop
        self.isInLoop = True

        typCond = self.visit(ast.cond, param)
        if type(typCond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)

        # Go out the loop
        self.isInLoop = False

    def visitBreakStmt(self, ast, param): 
        if self.isInLoop == False:
            raise MustInLoop(ast)
        return

    def visitContinueStmt(self, ast, param): 
        if self.isInLoop == False:
            raise MustInLoop(ast)
        return

    def visitReturnStmt(self, ast, param):
        # expr: Expr or None = None
        curFunc = self.curFunc[0]
        typReturn = VoidType() if ast.expr is None else self.visit(ast.expr, param)

        # Check type between curFunc and typReturn if this ast is the first return stmt in block else just visit ast.expr
        if self.isFirstReturn == True or self.isRetOfIfElse == True:
            if type(curFunc.return_type) is AutoType:
                curFunc.return_type = typReturn
            elif type(typReturn) is AutoType:
                if type(ast.expr) is FuncCall:
                    func = self.utl.lookup(ast.expr.name, self.g, lambda x: x.name)
                    func.return_type = curFunc.return_type
                if type(ast.expr) is Id:
                    for env in param:
                        x = self.utl.lookup(ast.expr.name, env, lambda x: x.name)
                        if x is None:
                            continue
                        x.typ = curFunc.return_type
            elif type(typReturn) is not type(curFunc.return_type):
                if type(curFunc.return_type) is FloatType and type(typReturn) is IntegerType:
                    pass
                else:
                    raise TypeMismatchInStatement(ast)
            
            if self.isRetOfIfElse == True:
                self.isRetOfIfElse = False
            else:
                self.isFirstReturn = False


    def visitCallStmt(self, ast, param): 
        # name: str, args: List[Expr]
        func = self.utl.lookup(ast.name, self.g, lambda x: x.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        # if type(func.return_type) is AutoType:
        #     func.return_type = VoidType()
        if func.name in ["supper","preventDefault"] and self.curFunc[1] is None:
            raise InvalidStatementInFunction(self.curFunc[0].name)
        if len(func.params) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        for i in range(len(func.params)):
            typParam = func.params[i].typ
            typArg = self.visit(ast.args[i], param)
            # print(type(typParam), type(typArg))
            if type(typParam) is AutoType:
                func.params[i].typ = typArg
            elif type(typArg) is AutoType: # args[i] is Func Call or Id (param)
                if type(ast.args[i]) is FuncCall:
                    func = self.utl.lookup(ast.args[i].name, self.g, lambda x: x.name)
                    func.return_type = typParam
                elif type(ast.args[i]) is Id:
                    for env in param:
                        x = self.utl.lookup(ast.args[i].name, env, lambda x: x.name)
                        if x is None:
                            continue
                        if type(x) is ParamDecl:
                            x.typ = typParam
                            break
                        
            elif type(typParam) is not type(typArg):
                if type(typParam) is FloatType and type(typArg) is IntegerType:
                    return
                raise TypeMismatchInStatement(ast)

    def visitVarDecl(self, ast, param):
        # name: str, typ: Type, init: Expr or None = None
        if self.utl.lookup(ast.name, param[0], lambda x:x.name):
            raise Redeclared(Variable(), ast.name)
            
        param[0] = [ast] + param[0]

        if type(ast.typ) is AutoType:
            if ast.init is None:
                raise Invalid(Variable(), ast.name)
            ast.typ = self.visit(ast.init, param)
        else:
            if ast.init is not None:
                initType = self.visit(ast.init, param)
                if type(initType) is AutoType: # init is Func Call
                    if type(ast.init) is FuncCall:
                        func = self.utl.lookup(ast.init.name, self.g, lambda x: x.name)
                        func.return_type = ast.typ
                        
                    if type(ast.init) is Id:
                        for env in param:
                            x = self.utl.lookup(ast.init.name, env, lambda x: x.name)
                            if x is None:
                                continue
                            x.typ = ast.typ
                    return param

                elif type(initType) is type(ast.typ):
                    if type(ast.typ) is ArrayType:
                        if ast.typ.dimensions != initType.dimensions:
                            raise TypeMismatchInVarDecl(ast) 
                        if type(ast.typ.typ) is not type(initType.typ):
                            raise TypeMismatchInVarDecl(ast) 
                    return param
                elif type(ast.typ) is FloatType and type(initType) is IntegerType:
                    return param
                else:
                    raise TypeMismatchInVarDecl(ast)

        
        return param

    def visitParamDecl(self, ast, param):
        # name: str, typ: Type, out: bool = False, inherit: bool = False

        if self.utl.lookup(ast.name, param[0], lambda x: x.name):
            raise Redeclared(Parameter(), ast.name)

        param[0] = [ast] + param[0]
        return param
    def visitFuncDecl(self, ast, param): 
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        func = self.utl.lookup(ast.name, param[0], lambda x: x.name)
        if func is None:
            param[0] = [self.utl.lookup(ast.name, self.g, lambda x: x.name)] + param[0]
        else:
            raise Redeclared(Function(), ast.name)
        
        self.curFunc = [ast, None]
        self.isFirstReturn = True

        if ast.inherit:
            parent = self.utl.lookup(ast.inherit, self.g, lambda x: x.name)
            if parent is None:
                raise Undeclared(Function(), ast.inherit)
            
            self.curFunc[1] = parent
        
        localEnv = [[]] + param
        for paramDecl in ast.params:
            localEnv = self.visit(paramDecl, localEnv)


        self.visit(ast.body, localEnv)
        
        self.curFunc = None
        self.isFirstReturn = None
        return param

    def visitProgram(self, ast, param):
        param = [[]]

        for decl in ast.decls:
            param = self.visit(decl, param)

        
        main = self.utl.lookup("main", self.g, lambda x: x.name)
        if main:

            if type(main) is FuncDecl and type(main.return_type) is VoidType and len(main.params) == 0:
                return
            raise NoEntryPoint()
        raise NoEntryPoint()
