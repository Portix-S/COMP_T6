# Generated from Valorant.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ValorantParser import ValorantParser
else:
    from ValorantParser import ValorantParser

# This class defines a complete generic visitor for a parse tree produced by ValorantParser.

class ValorantVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ValorantParser#unidade.
    def visitUnidade(self, ctx:ValorantParser.UnidadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#sinergia_dupla.
    def visitSinergia_dupla(self, ctx:ValorantParser.Sinergia_duplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#sinergia_completa.
    def visitSinergia_completa(self, ctx:ValorantParser.Sinergia_completaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#declaracao_unidade.
    def visitDeclaracao_unidade(self, ctx:ValorantParser.Declaracao_unidadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#declaracao_sinergia.
    def visitDeclaracao_sinergia(self, ctx:ValorantParser.Declaracao_sinergiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#declaracao_mapas.
    def visitDeclaracao_mapa(self, ctx:ValorantParser.Declaracao_mapasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#declaracao.
    def visitDeclaracao(self, ctx:ValorantParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#declaracoes.
    def visitDeclaracoes(self, ctx:ValorantParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#saida.
    def visitSaida(self, ctx:ValorantParser.SaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#saida_sinergia.
    def visitSaida_sinergia(self, ctx:ValorantParser.Saida_sinergiaContext):
        return self.visitChildren(ctx)


    # # Visit a parse tree produced by ValorantParser#saida_sinergia_dupla.
    # def visitSaida_sinergia_dupla(self, ctx:ValorantParser.Saida_sinergia_duplaContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by ValorantParser#saida_mapa.
    # def visitSaida_mapa(self, ctx:ValorantParser.Saida_mapaContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by ValorantParser#programa.
    def visitPrograma(self, ctx:ValorantParser.ProgramaContext):
        return self.visitChildren(ctx)



del ValorantParser