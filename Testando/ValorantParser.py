# Generated from Valorant.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nA\n\n\3\13")
        buf.write("\7\13D\n\13\f\13\16\13G\13\13\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\2\2\2I\2\34\3\2\2\2\4\36\3\2\2\2\6 \3")
        buf.write("\2\2\2\b\"\3\2\2\2\n%\3\2\2\2\f\61\3\2\2\2\16\64\3\2\2")
        buf.write("\2\208\3\2\2\2\22@\3\2\2\2\24E\3\2\2\2\26H\3\2\2\2\30")
        buf.write("K\3\2\2\2\32O\3\2\2\2\34\35\7\r\2\2\35\3\3\2\2\2\36\37")
        buf.write("\7\r\2\2\37\5\3\2\2\2 !\7\r\2\2!\7\3\2\2\2\"#\5\2\2\2")
        buf.write("#$\5\2\2\2$\t\3\2\2\2%&\5\2\2\2&\'\7\5\2\2\'(\5\2\2\2")
        buf.write("()\7\5\2\2)*\5\2\2\2*+\7\5\2\2+,\5\2\2\2,-\7\5\2\2-.\5")
        buf.write("\2\2\2./\7\5\2\2/\60\5\2\2\2\60\13\3\2\2\2\61\62\7\6\2")
        buf.write("\2\62\63\5\2\2\2\63\r\3\2\2\2\64\65\7\7\2\2\65\66\5\4")
        buf.write("\3\2\66\67\5\b\5\2\67\17\3\2\2\289\7\b\2\29:\5\6\4\2:")
        buf.write(";\7\n\2\2;<\5\n\6\2<\21\3\2\2\2=A\5\f\7\2>A\5\16\b\2?")
        buf.write("A\5\20\t\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\23\3\2\2\2B")
        buf.write("D\5\22\n\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\25")
        buf.write("\3\2\2\2GE\3\2\2\2HI\7\t\2\2IJ\5\30\r\2J\27\3\2\2\2KL")
        buf.write("\7\13\2\2LM\7\f\2\2MN\5\2\2\2N\31\3\2\2\2OP\5\24\13\2")
        buf.write("PQ\5\26\f\2QR\7\2\2\3R\33\3\2\2\2\4@E")
        return buf.getvalue()


class ValorantParser ( Parser ):

    grammarFileName = "Valorant.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'agente'", 
                     "'sinergia'", "'mapa'", "'encontrar'", "'composicao'", 
                     "'sinergias'", "'para'" ]

    symbolicNames = [ "<INVALID>", "COMENTARIO", "WS", "OP", "AGENTE", "SINERGIA", 
                      "MAPA", "ENCONTRAR", "COMPOSICAO", "SINERGIAS", "PARA", 
                      "IDENT" ]

    RULE_unidade = 0
    RULE_sinergia = 1
    RULE_mapa = 2
    RULE_sinergia_dupla = 3
    RULE_sinergia_completa = 4
    RULE_declaracao_unidade = 5
    RULE_declaracao_sinergia = 6
    RULE_declaracao_mapas = 7
    RULE_declaracao = 8
    RULE_declaracoes = 9
    RULE_saida = 10
    RULE_saida_sinergia = 11
    RULE_programa = 12

    ruleNames =  [ "unidade", "sinergia", "mapa", "sinergia_dupla", "sinergia_completa", 
                   "declaracao_unidade", "declaracao_sinergia", "declaracao_mapas", 
                   "declaracao", "declaracoes", "saida", "saida_sinergia", 
                   "programa" ]

    EOF = Token.EOF
    COMENTARIO=1
    WS=2
    OP=3
    AGENTE=4
    SINERGIA=5
    MAPA=6
    ENCONTRAR=7
    COMPOSICAO=8
    SINERGIAS=9
    PARA=10
    IDENT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class UnidadeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ValorantParser.IDENT, 0)

        def getRuleIndex(self):
            return ValorantParser.RULE_unidade

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnidade" ):
                return visitor.visitUnidade(self)
            else:
                return visitor.visitChildren(self)




    def unidade(self):

        localctx = ValorantParser.UnidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_unidade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ValorantParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SinergiaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ValorantParser.IDENT, 0)

        def getRuleIndex(self):
            return ValorantParser.RULE_sinergia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinergia" ):
                return visitor.visitSinergia(self)
            else:
                return visitor.visitChildren(self)




    def sinergia(self):

        localctx = ValorantParser.SinergiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sinergia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ValorantParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MapaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ValorantParser.IDENT, 0)

        def getRuleIndex(self):
            return ValorantParser.RULE_mapa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapa" ):
                return visitor.visitMapa(self)
            else:
                return visitor.visitChildren(self)




    def mapa(self):

        localctx = ValorantParser.MapaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ValorantParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sinergia_duplaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unidade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.UnidadeContext)
            else:
                return self.getTypedRuleContext(ValorantParser.UnidadeContext,i)


        def getRuleIndex(self):
            return ValorantParser.RULE_sinergia_dupla

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinergia_dupla" ):
                return visitor.visitSinergia_dupla(self)
            else:
                return visitor.visitChildren(self)




    def sinergia_dupla(self):

        localctx = ValorantParser.Sinergia_duplaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sinergia_dupla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.unidade()
            self.state = 33
            self.unidade()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sinergia_completaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unidade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.UnidadeContext)
            else:
                return self.getTypedRuleContext(ValorantParser.UnidadeContext,i)


        def OP(self, i:int=None):
            if i is None:
                return self.getTokens(ValorantParser.OP)
            else:
                return self.getToken(ValorantParser.OP, i)

        def getRuleIndex(self):
            return ValorantParser.RULE_sinergia_completa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinergia_completa" ):
                return visitor.visitSinergia_completa(self)
            else:
                return visitor.visitChildren(self)




    def sinergia_completa(self):

        localctx = ValorantParser.Sinergia_completaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sinergia_completa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.unidade()
            self.state = 36
            self.match(ValorantParser.OP)
            self.state = 37
            self.unidade()
            self.state = 38
            self.match(ValorantParser.OP)
            self.state = 39
            self.unidade()
            self.state = 40
            self.match(ValorantParser.OP)
            self.state = 41
            self.unidade()
            self.state = 42
            self.match(ValorantParser.OP)
            self.state = 43
            self.unidade()
            self.state = 44
            self.match(ValorantParser.OP)
            self.state = 45
            self.unidade()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracao_unidadeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENTE(self):
            return self.getToken(ValorantParser.AGENTE, 0)

        def unidade(self):
            return self.getTypedRuleContext(ValorantParser.UnidadeContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_declaracao_unidade

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_unidade" ):
                return visitor.visitDeclaracao_unidade(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_unidade(self):

        localctx = ValorantParser.Declaracao_unidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracao_unidade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ValorantParser.AGENTE)
            self.state = 48
            self.unidade()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracao_sinergiaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINERGIA(self):
            return self.getToken(ValorantParser.SINERGIA, 0)

        def sinergia(self):
            return self.getTypedRuleContext(ValorantParser.SinergiaContext,0)


        def sinergia_dupla(self):
            return self.getTypedRuleContext(ValorantParser.Sinergia_duplaContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_declaracao_sinergia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_sinergia" ):
                return visitor.visitDeclaracao_sinergia(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_sinergia(self):

        localctx = ValorantParser.Declaracao_sinergiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracao_sinergia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ValorantParser.SINERGIA)
            self.state = 51
            self.sinergia()
            self.state = 52
            self.sinergia_dupla()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracao_mapasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAPA(self):
            return self.getToken(ValorantParser.MAPA, 0)

        def mapa(self):
            return self.getTypedRuleContext(ValorantParser.MapaContext,0)


        def COMPOSICAO(self):
            return self.getToken(ValorantParser.COMPOSICAO, 0)

        def sinergia_completa(self):
            return self.getTypedRuleContext(ValorantParser.Sinergia_completaContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_declaracao_mapas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_mapas" ):
                return visitor.visitDeclaracao_mapas(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_mapas(self):

        localctx = ValorantParser.Declaracao_mapasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracao_mapas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ValorantParser.MAPA)
            self.state = 55
            self.mapa()
            self.state = 56
            self.match(ValorantParser.COMPOSICAO)
            self.state = 57
            self.sinergia_completa()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_unidade(self):
            return self.getTypedRuleContext(ValorantParser.Declaracao_unidadeContext,0)


        def declaracao_sinergia(self):
            return self.getTypedRuleContext(ValorantParser.Declaracao_sinergiaContext,0)


        def declaracao_mapas(self):
            return self.getTypedRuleContext(ValorantParser.Declaracao_mapasContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_declaracao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = ValorantParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaracao)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ValorantParser.AGENTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.declaracao_unidade()
                pass
            elif token in [ValorantParser.SINERGIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.declaracao_sinergia()
                pass
            elif token in [ValorantParser.MAPA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.declaracao_mapas()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracoesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(ValorantParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return ValorantParser.RULE_declaracoes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = ValorantParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ValorantParser.AGENTE) | (1 << ValorantParser.SINERGIA) | (1 << ValorantParser.MAPA))) != 0):
                self.state = 64
                self.declaracao()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SaidaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENCONTRAR(self):
            return self.getToken(ValorantParser.ENCONTRAR, 0)

        def saida_sinergia(self):
            return self.getTypedRuleContext(ValorantParser.Saida_sinergiaContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_saida

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida" ):
                return visitor.visitSaida(self)
            else:
                return visitor.visitChildren(self)




    def saida(self):

        localctx = ValorantParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ValorantParser.ENCONTRAR)
            self.state = 71
            self.saida_sinergia()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Saida_sinergiaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINERGIAS(self):
            return self.getToken(ValorantParser.SINERGIAS, 0)

        def PARA(self):
            return self.getToken(ValorantParser.PARA, 0)

        def unidade(self):
            return self.getTypedRuleContext(ValorantParser.UnidadeContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_saida_sinergia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida_sinergia" ):
                return visitor.visitSaida_sinergia(self)
            else:
                return visitor.visitChildren(self)




    def saida_sinergia(self):

        localctx = ValorantParser.Saida_sinergiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_saida_sinergia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ValorantParser.SINERGIAS)
            self.state = 74
            self.match(ValorantParser.PARA)
            self.state = 75
            self.unidade()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(ValorantParser.DeclaracoesContext,0)


        def saida(self):
            return self.getTypedRuleContext(ValorantParser.SaidaContext,0)


        def EOF(self):
            return self.getToken(ValorantParser.EOF, 0)

        def getRuleIndex(self):
            return ValorantParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ValorantParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.declaracoes()
            self.state = 78
            self.saida()
            self.state = 79
            self.match(ValorantParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





