# Generated from BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#decls.
    def enterDecls(self, ctx:BKITParser.DeclsContext):
        pass

    # Exit a parse tree produced by BKITParser#decls.
    def exitDecls(self, ctx:BKITParser.DeclsContext):
        pass


    # Enter a parse tree produced by BKITParser#decl.
    def enterDecl(self, ctx:BKITParser.DeclContext):
        pass

    # Exit a parse tree produced by BKITParser#decl.
    def exitDecl(self, ctx:BKITParser.DeclContext):
        pass


    # Enter a parse tree produced by BKITParser#val_decl.
    def enterVal_decl(self, ctx:BKITParser.Val_declContext):
        pass

    # Exit a parse tree produced by BKITParser#val_decl.
    def exitVal_decl(self, ctx:BKITParser.Val_declContext):
        pass


    # Enter a parse tree produced by BKITParser#var_init.
    def enterVar_init(self, ctx:BKITParser.Var_initContext):
        pass

    # Exit a parse tree produced by BKITParser#var_init.
    def exitVar_init(self, ctx:BKITParser.Var_initContext):
        pass


    # Enter a parse tree produced by BKITParser#recursive_decl.
    def enterRecursive_decl(self, ctx:BKITParser.Recursive_declContext):
        pass

    # Exit a parse tree produced by BKITParser#recursive_decl.
    def exitRecursive_decl(self, ctx:BKITParser.Recursive_declContext):
        pass


    # Enter a parse tree produced by BKITParser#func_decl.
    def enterFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass

    # Exit a parse tree produced by BKITParser#func_decl.
    def exitFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass


    # Enter a parse tree produced by BKITParser#list_para.
    def enterList_para(self, ctx:BKITParser.List_paraContext):
        pass

    # Exit a parse tree produced by BKITParser#list_para.
    def exitList_para(self, ctx:BKITParser.List_paraContext):
        pass


    # Enter a parse tree produced by BKITParser#para_decl.
    def enterPara_decl(self, ctx:BKITParser.Para_declContext):
        pass

    # Exit a parse tree produced by BKITParser#para_decl.
    def exitPara_decl(self, ctx:BKITParser.Para_declContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt.
    def enterStmt(self, ctx:BKITParser.StmtContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt.
    def exitStmt(self, ctx:BKITParser.StmtContext):
        pass


    # Enter a parse tree produced by BKITParser#assign_stmt.
    def enterAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#assign_stmt.
    def exitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#if_stmt.
    def enterIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#if_stmt.
    def exitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#for_stmt.
    def enterFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#for_stmt.
    def exitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#while_stmt.
    def enterWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#while_stmt.
    def exitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#break_stmt.
    def enterBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#break_stmt.
    def exitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#cont_stmt.
    def enterCont_stmt(self, ctx:BKITParser.Cont_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#cont_stmt.
    def exitCont_stmt(self, ctx:BKITParser.Cont_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#return_stmt.
    def enterReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#return_stmt.
    def exitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#call_stmt.
    def enterCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#call_stmt.
    def exitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#block_stmt.
    def enterBlock_stmt(self, ctx:BKITParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#block_stmt.
    def exitBlock_stmt(self, ctx:BKITParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#expr.
    def enterExpr(self, ctx:BKITParser.ExprContext):
        pass

    # Exit a parse tree produced by BKITParser#expr.
    def exitExpr(self, ctx:BKITParser.ExprContext):
        pass


    # Enter a parse tree produced by BKITParser#expr1.
    def enterExpr1(self, ctx:BKITParser.Expr1Context):
        pass

    # Exit a parse tree produced by BKITParser#expr1.
    def exitExpr1(self, ctx:BKITParser.Expr1Context):
        pass


    # Enter a parse tree produced by BKITParser#expr2.
    def enterExpr2(self, ctx:BKITParser.Expr2Context):
        pass

    # Exit a parse tree produced by BKITParser#expr2.
    def exitExpr2(self, ctx:BKITParser.Expr2Context):
        pass


    # Enter a parse tree produced by BKITParser#expr3.
    def enterExpr3(self, ctx:BKITParser.Expr3Context):
        pass

    # Exit a parse tree produced by BKITParser#expr3.
    def exitExpr3(self, ctx:BKITParser.Expr3Context):
        pass


    # Enter a parse tree produced by BKITParser#expr4.
    def enterExpr4(self, ctx:BKITParser.Expr4Context):
        pass

    # Exit a parse tree produced by BKITParser#expr4.
    def exitExpr4(self, ctx:BKITParser.Expr4Context):
        pass


    # Enter a parse tree produced by BKITParser#expr5.
    def enterExpr5(self, ctx:BKITParser.Expr5Context):
        pass

    # Exit a parse tree produced by BKITParser#expr5.
    def exitExpr5(self, ctx:BKITParser.Expr5Context):
        pass


    # Enter a parse tree produced by BKITParser#expr6.
    def enterExpr6(self, ctx:BKITParser.Expr6Context):
        pass

    # Exit a parse tree produced by BKITParser#expr6.
    def exitExpr6(self, ctx:BKITParser.Expr6Context):
        pass


    # Enter a parse tree produced by BKITParser#expr7.
    def enterExpr7(self, ctx:BKITParser.Expr7Context):
        pass

    # Exit a parse tree produced by BKITParser#expr7.
    def exitExpr7(self, ctx:BKITParser.Expr7Context):
        pass


    # Enter a parse tree produced by BKITParser#expr8.
    def enterExpr8(self, ctx:BKITParser.Expr8Context):
        pass

    # Exit a parse tree produced by BKITParser#expr8.
    def exitExpr8(self, ctx:BKITParser.Expr8Context):
        pass


    # Enter a parse tree produced by BKITParser#func_call.
    def enterFunc_call(self, ctx:BKITParser.Func_callContext):
        pass

    # Exit a parse tree produced by BKITParser#func_call.
    def exitFunc_call(self, ctx:BKITParser.Func_callContext):
        pass


    # Enter a parse tree produced by BKITParser#special_func.
    def enterSpecial_func(self, ctx:BKITParser.Special_funcContext):
        pass

    # Exit a parse tree produced by BKITParser#special_func.
    def exitSpecial_func(self, ctx:BKITParser.Special_funcContext):
        pass


    # Enter a parse tree produced by BKITParser#list_expr.
    def enterList_expr(self, ctx:BKITParser.List_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#list_expr.
    def exitList_expr(self, ctx:BKITParser.List_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#array_lit.
    def enterArray_lit(self, ctx:BKITParser.Array_litContext):
        pass

    # Exit a parse tree produced by BKITParser#array_lit.
    def exitArray_lit(self, ctx:BKITParser.Array_litContext):
        pass


    # Enter a parse tree produced by BKITParser#arr_typ_decl.
    def enterArr_typ_decl(self, ctx:BKITParser.Arr_typ_declContext):
        pass

    # Exit a parse tree produced by BKITParser#arr_typ_decl.
    def exitArr_typ_decl(self, ctx:BKITParser.Arr_typ_declContext):
        pass


    # Enter a parse tree produced by BKITParser#return_type.
    def enterReturn_type(self, ctx:BKITParser.Return_typeContext):
        pass

    # Exit a parse tree produced by BKITParser#return_type.
    def exitReturn_type(self, ctx:BKITParser.Return_typeContext):
        pass


    # Enter a parse tree produced by BKITParser#var_type.
    def enterVar_type(self, ctx:BKITParser.Var_typeContext):
        pass

    # Exit a parse tree produced by BKITParser#var_type.
    def exitVar_type(self, ctx:BKITParser.Var_typeContext):
        pass


    # Enter a parse tree produced by BKITParser#elementType.
    def enterElementType(self, ctx:BKITParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by BKITParser#elementType.
    def exitElementType(self, ctx:BKITParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by BKITParser#listInt.
    def enterListInt(self, ctx:BKITParser.ListIntContext):
        pass

    # Exit a parse tree produced by BKITParser#listInt.
    def exitListInt(self, ctx:BKITParser.ListIntContext):
        pass


    # Enter a parse tree produced by BKITParser#listID.
    def enterListID(self, ctx:BKITParser.ListIDContext):
        pass

    # Exit a parse tree produced by BKITParser#listID.
    def exitListID(self, ctx:BKITParser.ListIDContext):
        pass



del BKITParser