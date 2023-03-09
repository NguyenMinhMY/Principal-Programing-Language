// Generated from BKIT.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#vardecls}.
	 * @param ctx the parse tree
	 */
	void enterVardecls(BKITParser.VardeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#vardecls}.
	 * @param ctx the parse tree
	 */
	void exitVardecls(BKITParser.VardeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#vardecltail}.
	 * @param ctx the parse tree
	 */
	void enterVardecltail(BKITParser.VardecltailContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#vardecltail}.
	 * @param ctx the parse tree
	 */
	void exitVardecltail(BKITParser.VardecltailContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#mptype}.
	 * @param ctx the parse tree
	 */
	void enterMptype(BKITParser.MptypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#mptype}.
	 * @param ctx the parse tree
	 */
	void exitMptype(BKITParser.MptypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#ids}.
	 * @param ctx the parse tree
	 */
	void enterIds(BKITParser.IdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#ids}.
	 * @param ctx the parse tree
	 */
	void exitIds(BKITParser.IdsContext ctx);
}