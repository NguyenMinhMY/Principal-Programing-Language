from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
    # program: decls EOF ;
        return Program(self.visit(ctx.decls()))


    def visitDecls(self, ctx:MT22Parser.DeclsContext):
    # decls: decl decls | decl;
        if ctx.getChildCount() == 1:
            return list(self.visit(ctx.decl()))
        else:
            decl = self.visit(ctx.decl())
            decls = self.visit(ctx.decls())
            return list(decl) + decls

    def visitDecl(self, ctx:MT22Parser.DeclContext):
    # decl: (var_decl|func_decl);
        return self.visitChildren(ctx)



    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
    # var_decl: listID COLON var_type SEMI | var_init;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.var_init())
        else:
            listID = self.visit(ctx.listID())
            var_type = self.visit(ctx.var_type())
            return map(lambda x: VarDecl(x, var_type), listID)


    def visitVar_init(self, ctx:MT22Parser.Var_initContext):
    # var_init: ID (COMMA recursive_decl|COLON var_type ASSIGN) expr SEMI;
        if ctx.ASSIGN():
            return [VarDecl(ctx.ID().getText(), self.visit(ctx.var_type()), self.visit(ctx.expr()))]
        else:
            listID, listExpr, var_type = self.visit(ctx.recursive_decl())
            listID = [ctx.ID().getText()] + listID
            listExpr = listExpr + [self.visit(ctx.expr())]
            return map(lambda x,y: VarDecl(x,var_type,y), listID, listExpr)


    def visitRecursive_decl(self, ctx:MT22Parser.Recursive_declContext):
    # recursive_decl: ID (COMMA recursive_decl|COLON var_type ASSIGN) expr COMMA;
        listID = [ctx.ID().getText()]
        listExpr = [self.visit(ctx.expr())]
        if ctx.ASSIGN():
            return listID, listExpr, self.visit(ctx.var_type())
        else:
            fir, sec, typ = self.visit(ctx.recursive_decl())
            return listID + fir, sec + listExpr, typ


    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt 
    # func_decl: ID COLON FUNCTION return_type LB list_para? RB (INHERIT ID)? block_stmt;
        name = ctx.getChild(0).getText()
        return_type = self.visit(ctx.return_type())
        body = self.visit(ctx.block_stmt())
        
        if ctx.getChildCount() % 2 == 0: # exists list_para
            params = self.visit(ctx.list_para())
            if ctx.INHERIT():
                return [FuncDecl(name, return_type, params, ctx.ID(1).getText(), body)]
            else:
                return [FuncDecl(name, return_type, params, None, body)]
        elif ctx.INHERIT():
            return [FuncDecl(name, return_type, [], ctx.ID(1).getText(), body)]
        else:
            return [FuncDecl(name, return_type, [], None, body)]


    def visitList_para(self, ctx:MT22Parser.List_paraContext):
    # list_para: para_decl COMMA list_para | para_decl;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.para_decl())]
        else:
            return [self.visit(ctx.para_decl())] + self.visit(ctx.list_para())


    # CAN XEM LAI
    def visitPara_decl(self, ctx:MT22Parser.Para_declContext):
        # para_decl: INHERIT? OUT? ID COLON var_type;
        if ctx.INHERIT():
            if ctx.OUT():
                return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), True, True)
            else:
                return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), False, True)
        elif ctx.OUT():
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), True)
        else:
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()))
        



    def visitStmt(self, ctx:MT22Parser.StmtContext):
        # stmt: assign_stmt
        #     | if_stmt
        #     | for_stmt
        #     | while_stmt
        #     | do_while_stmt
        #     | break_stmt
        #     | cont_stmt
        #     | return_stmt
        #     | call_stmt
        #     | block_stmt;
        return self.visitChildren(ctx)



    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        # assign_stmt: lhs ASSIGN expr SEMI;

        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    def visitLhs(self, ctx:MT22Parser.LhsContext):
        # lhs : ID LSB list_expr RSB | ID;
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return ArrayCell(ctx.ID().getText(), self.visit(ctx.list_expr()))



    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        # if_stmt : IF LB expr RB stmt (ELSE stmt)?;

        if ctx.getChildCount() == 5:
            expr = self.visit(ctx.expr())
            tstmt = self.visit(ctx.stmt(0))
            return IfStmt(expr,tstmt)
        else:
            expr = self.visit(ctx.expr())
            tstmt = self.visit(ctx.stmt(0))
            fstmt = self.visit(ctx.stmt(1))
            return IfStmt(expr, tstmt, fstmt)


    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        # for_stmt: FOR LB (ID ASSIGN expr ) COMMA expr COMMA expr RB (stmt);
        assignStmt = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        return ForStmt(assignStmt, cond , upd , stmt)


    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        # while_stmt: WHILE LB expr RB stmt;
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(expr, stmt)


    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        # do_while_stmt: DO block_stmt WHILE LB expr RB SEMI;

        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))


    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        # break_stmt: BREAK SEMI;

        return BreakStmt()


    def visitCont_stmt(self, ctx:MT22Parser.Cont_stmtContext):
        # cont_stmt: CONTINUE SEMI;

        return ContinueStmt()


    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        # return_stmt: RETURN expr? SEMI;
        if ctx.getChildCount() == 3:
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt()

    # CAN XEM LAI
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        # call_stmt: func_call SEMI;
        obj = self.visit(ctx.func_call())
        return CallStmt(obj.name, obj.args)

    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        # block_stmt: LP block_list RP;
        block_list = self.visit(ctx.block_list())
        return BlockStmt(block_list)
    
    def visitBlock_list(self, ctx:MT22Parser.Block_listContext):
        # block_list: (stmt|var_decl) block_list |;
        if ctx.getChildCount() == 0:
            return []
        if isinstance(self.visit(ctx.getChild(0)),Stmt):
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.block_list())
        else:
            return list(self.visit(ctx.getChild(0))) + self.visit(ctx.block_list())

    def visitExpr(self, ctx:MT22Parser.ExprContext):
        # expr: expr1 CONCAT expr1 | expr1;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        else:
            op = ctx.getChild(1).getText()
            return BinExpr(op, self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))


    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        # expr1: expr2 (EQ | NOT_EQ | LT | GT | LT_EQ | GT_EQ) expr2 | expr2;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        else:
            op = ctx.getChild(1).getText()
            return BinExpr(op, self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))


    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        # expr2: expr2 (AND | OR) expr3 | expr3;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            op = ctx.getChild(1).getText()
            return BinExpr(op, self.visit(ctx.expr2()), self.visit(ctx.expr3()))


    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        # expr3: expr3 (PLUS | MINUS) expr4 | expr4;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            op = ctx.getChild(1).getText()
            return BinExpr(op, self.visit(ctx.expr3()), self.visit(ctx.expr4()))


    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            op = ctx.getChild(1).getText()
            return BinExpr(op, self.visit(ctx.expr4()), self.visit(ctx.expr5()))


    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        # expr5: NOT expr5 | expr6;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        else:
            return UnExpr(ctx.NOT().getText(),self.visit(ctx.expr5()))


    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        # expr6: MINUS expr6 | expr7;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        else:
            return UnExpr(ctx.MINUS().getText(),self.visit(ctx.expr6()))



    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        # expr7: ID LSB list_expr RSB | expr8;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        else:
            return ArrayCell(ctx.ID().getText(),self.visit(ctx.list_expr()))


    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        # expr8: LB expr RB | ID | func_call | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | array_lit;
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): 
            floatlit = ctx.FLOATLIT().getText()
            if floatlit[0] == '.':
                floatlit = '0' + floatlit
            return FloatLit(float(floatlit))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(True if ctx.BOOLLIT().getText() == 'true' else False)
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else:
            return self.visitChildren(ctx)


    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        # func_call: ID LB list_expr? RB | special_func;
        if ctx.getChildCount() == 1:
            id , listExp = self.visit(ctx.special_func())
            return FuncCall(id,listExp)
        elif ctx.getChildCount() == 3:
            return FuncCall(ctx.ID().getText(), [])
        else:
            return FuncCall(ctx.ID().getText(),self.visit(ctx.list_expr()))


    def visitSpecial_func(self, ctx:MT22Parser.Special_funcContext):
        # special_func: 'readInteger' LB RB
		# 	| 'printInteger' LB expr RB
		# 	| 'readFloat' LB RB
		# 	| 'printBoolean' LB expr RB
		# 	| 'readString' LB RB
		# 	| 'printString' LB expr RB
		# 	| 'super' LB list_expr RB
		# 	| 'preventDefault' LB RB;
        firstChild = ctx.getChild(0).getText()
        if ctx.getChildCount() == 3:
            return firstChild,[]
        else:
            exp = self.visit(ctx.getChild(2))
            if isinstance(exp, list):
                return firstChild, exp
            else:
                return firstChild, [exp]
                
            
        # if firstChild in ['readInteger','readFloat','readString','preventDefault']:
        #     return FuncCall(firstChild, [])
        # else:
        #     return FuncCall(firstChild, self.visit(ctx.list_expr()))



    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        # list_expr: expr COMMA list_expr | expr;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.list_expr())


    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        # array_lit: LP (list_expr|) RP;
        if ctx.getChildCount() == 2:
            return ArrayLit([])
        else:
            return ArrayLit(self.visit(ctx.list_expr()))


    def visitArr_typ_decl(self, ctx:MT22Parser.Arr_typ_declContext):
        # arr_typ_decl: ARRAY LSB listInt RSB OF elementType;
        return ArrayType(self.visit(ctx.listInt()), self.visit(ctx.elementType()))


    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        # return_type: var_type | VOID;
        if ctx.VOID():
            return VoidType()
        else:
            return self.visitChildren(ctx)


    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        # var_type: elementType |arr_typ_decl| AUTO ;
        if ctx.AUTO():
            return AutoType()
        else:
            return self.visitChildren(ctx)


    def visitElementType(self, ctx:MT22Parser.ElementTypeContext):
    # elementType: BOOLEAN | INTEGER | FLOAT | STRING;
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()


    def visitListInt(self, ctx:MT22Parser.ListIntContext):
    # listInt: INTLIT COMMA listInt | INTLIT;
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        else:
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.listInt())


    def visitListID(self, ctx:MT22Parser.ListIDContext):
    # listID: ID COMMA listID | ID;
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.listID())