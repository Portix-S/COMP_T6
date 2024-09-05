# Generated from Valorant.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\5\b9\n\b\3\t\7\t<\n\t\f\t\16\t?\13\t\3\n\3\n")
        buf.write("\3\n\3\13\7\13E\n\13\f\13\16\13H\13\13\3\13\3\13\7\13")
        buf.write("L\n\13\f\13\16\13O\13\13\3\f\3\f\3\f\7\fT\n\f\f\f\16\f")
        buf.write("W\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2[\2\34\3")
        buf.write("\2\2\2\4\36\3\2\2\2\6\"\3\2\2\2\b,\3\2\2\2\n/\3\2\2\2")
        buf.write("\f\62\3\2\2\2\168\3\2\2\2\20=\3\2\2\2\22@\3\2\2\2\24F")
        buf.write("\3\2\2\2\26P\3\2\2\2\30Z\3\2\2\2\32^\3\2\2\2\34\35\7\r")
        buf.write("\2\2\35\3\3\2\2\2\36\37\5\2\2\2\37 \7\f\2\2 !\5\2\2\2")
        buf.write("!\5\3\2\2\2\"#\5\2\2\2#$\7\f\2\2$%\5\2\2\2%&\7\f\2\2&")
        buf.write("\'\5\2\2\2\'(\7\f\2\2()\5\2\2\2)*\7\f\2\2*+\5\2\2\2+\7")
        buf.write("\3\2\2\2,-\7\3\2\2-.\5\2\2\2.\t\3\2\2\2/\60\7\4\2\2\60")
        buf.write("\61\5\4\3\2\61\13\3\2\2\2\62\63\7\5\2\2\63\64\5\6\4\2")
        buf.write("\64\r\3\2\2\2\659\5\b\5\2\669\5\n\6\2\679\5\f\7\28\65")
        buf.write("\3\2\2\28\66\3\2\2\28\67\3\2\2\29\17\3\2\2\2:<\5\16\b")
        buf.write("\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\21\3\2\2\2")
        buf.write("?=\3\2\2\2@A\7\6\2\2AB\5\24\13\2B\23\3\2\2\2CE\5\26\f")
        buf.write("\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2H")
        buf.write("F\3\2\2\2IM\7\7\2\2JL\5\30\r\2KJ\3\2\2\2LO\3\2\2\2MK\3")
        buf.write("\2\2\2MN\3\2\2\2N\25\3\2\2\2OM\3\2\2\2PQ\7\4\2\2QU\7\b")
        buf.write("\2\2RT\5\4\3\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2")
        buf.write("VX\3\2\2\2WU\3\2\2\2XY\7\7\2\2Y\27\3\2\2\2Z[\7\t\2\2[")
        buf.write("\\\5\6\4\2\\]\7\7\2\2]\31\3\2\2\2^_\5\20\t\2_`\5\22\n")
        buf.write("\2`a\7\2\2\3a\33\3\2\2\2\78=FMU")
        return buf.getvalue()


class ValorantParser ( Parser ):

    grammarFileName = "Valorant.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agente'", "'sinergia'", "'mapa'", "'encontrar'", 
                     "'\n'", "'com'", "'mapas:'", "<INVALID>", "<INVALID>", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMENTARIO", "WS", "OP", "IDENT" ]

    RULE_unidade = 0
    RULE_sinergia_dupla = 1
    RULE_sinergia_completa = 2
    RULE_declaracao_unidade = 3
    RULE_declaracao_sinergia = 4
    RULE_declaracao_mapas = 5
    RULE_declaracao = 6
    RULE_declaracoes = 7
    RULE_saida = 8
    RULE_saida_sinergia = 9
    RULE_saida_sinergia_dupla = 10
    RULE_saida_mapa = 11
    RULE_programa = 12

    ruleNames =  [ "unidade", "sinergia_dupla", "sinergia_completa", "declaracao_unidade", 
                   "declaracao_sinergia", "declaracao_mapas", "declaracao", 
                   "declaracoes", "saida", "saida_sinergia", "saida_sinergia_dupla", 
                   "saida_mapa", "programa" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    COMENTARIO=8
    WS=9
    OP=10
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

    class Sinergia_duplaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unidade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.UnidadeContext)
            else:
                return self.getTypedRuleContext(ValorantParser.UnidadeContext,i)


        def OP(self):
            return self.getToken(ValorantParser.OP, 0)

        def getRuleIndex(self):
            return ValorantParser.RULE_sinergia_dupla

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinergia_dupla" ):
                return visitor.visitSinergia_dupla(self)
            else:
                return visitor.visitChildren(self)




    def sinergia_dupla(self):

        localctx = ValorantParser.Sinergia_duplaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sinergia_dupla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.unidade()
            self.state = 29
            self.match(ValorantParser.OP)
            self.state = 30
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
        self.enterRule(localctx, 4, self.RULE_sinergia_completa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.unidade()
            self.state = 33
            self.match(ValorantParser.OP)
            self.state = 34
            self.unidade()
            self.state = 35
            self.match(ValorantParser.OP)
            self.state = 36
            self.unidade()
            self.state = 37
            self.match(ValorantParser.OP)
            self.state = 38
            self.unidade()
            self.state = 39
            self.match(ValorantParser.OP)
            self.state = 40
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
        self.enterRule(localctx, 6, self.RULE_declaracao_unidade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ValorantParser.T__0)
            self.state = 43
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
        self.enterRule(localctx, 8, self.RULE_declaracao_sinergia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ValorantParser.T__1)
            self.state = 46
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
        self.enterRule(localctx, 10, self.RULE_declaracao_mapas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ValorantParser.T__2)
            self.state = 49
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
        self.enterRule(localctx, 12, self.RULE_declaracao)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ValorantParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.declaracao_unidade()
                pass
            elif token in [ValorantParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.declaracao_sinergia()
                pass
            elif token in [ValorantParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
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
        self.enterRule(localctx, 14, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ValorantParser.T__0) | (1 << ValorantParser.T__1) | (1 << ValorantParser.T__2))) != 0):
                self.state = 56
                self.declaracao()
                self.state = 61
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
        self.enterRule(localctx, 16, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ValorantParser.T__3)

            self.state = 63
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

        def saida_sinergia_dupla(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.Saida_sinergia_duplaContext)
            else:
                return self.getTypedRuleContext(ValorantParser.Saida_sinergia_duplaContext,i)


        def saida_mapa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.Saida_mapaContext)
            else:
                return self.getTypedRuleContext(ValorantParser.Saida_mapaContext,i)


        def getRuleIndex(self):
            return ValorantParser.RULE_saida_sinergia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida_sinergia" ):
                return visitor.visitSaida_sinergia(self)
            else:
                return visitor.visitChildren(self)




    def saida_sinergia(self):

        localctx = ValorantParser.Saida_sinergiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_saida_sinergia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ValorantParser.T__1:
                self.state = 65
                self.saida_sinergia_dupla()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(ValorantParser.T__4)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ValorantParser.T__6:
                self.state = 72
                self.saida_mapa()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Saida_sinergia_duplaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sinergia_dupla(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ValorantParser.Sinergia_duplaContext)
            else:
                return self.getTypedRuleContext(ValorantParser.Sinergia_duplaContext,i)


        def getRuleIndex(self):
            return ValorantParser.RULE_saida_sinergia_dupla

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida_sinergia_dupla" ):
                return visitor.visitSaida_sinergia_dupla(self)
            else:
                return visitor.visitChildren(self)




    def saida_sinergia_dupla(self):

        localctx = ValorantParser.Saida_sinergia_duplaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_saida_sinergia_dupla)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ValorantParser.T__1)
            self.state = 79
            self.match(ValorantParser.T__5)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ValorantParser.IDENT:
                self.state = 80
                self.sinergia_dupla()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(ValorantParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Saida_mapaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sinergia_completa(self):
            return self.getTypedRuleContext(ValorantParser.Sinergia_completaContext,0)


        def getRuleIndex(self):
            return ValorantParser.RULE_saida_mapa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida_mapa" ):
                return visitor.visitSaida_mapa(self)
            else:
                return visitor.visitChildren(self)




    def saida_mapa(self):

        localctx = ValorantParser.Saida_mapaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_saida_mapa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ValorantParser.T__6)
            self.state = 89
            self.sinergia_completa()
            self.state = 90
            self.match(ValorantParser.T__4)
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
            self.state = 92
            self.declaracoes()
            self.state = 93
            self.saida()
            self.state = 94
            self.match(ValorantParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





