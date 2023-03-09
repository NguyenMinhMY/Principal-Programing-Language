# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#val_decl.
    def visitVal_decl(self, ctx:BKOOLParser.Val_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_init.
    def visitVar_init(self, ctx:BKOOLParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#recursive_decl.
    def visitRecursive_decl(self, ctx:BKOOLParser.Recursive_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_typ_decl.
    def visitArr_typ_decl(self, ctx:BKOOLParser.Arr_typ_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_decl.
    def visitFunc_decl(self, ctx:BKOOLParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_para.
    def visitList_para(self, ctx:BKOOLParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_decl.
    def visitPara_decl(self, ctx:BKOOLParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listInt.
    def visitListInt(self, ctx:BKOOLParser.ListIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listID.
    def visitListID(self, ctx:BKOOLParser.ListIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKOOLParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKOOLParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#cont_stmt.
    def visitCont_stmt(self, ctx:BKOOLParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stmt.
    def visitCall_stmt(self, ctx:BKOOLParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_call.
    def visitFunc_call(self, ctx:BKOOLParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#special_func.
    def visitSpecial_func(self, ctx:BKOOLParser.Special_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_expr.
    def visitList_expr(self, ctx:BKOOLParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)



del BKOOLParser