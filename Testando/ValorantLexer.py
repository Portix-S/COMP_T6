# Generated from Valorant.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("r\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\5\2 \n\2\3\3\3\3\3\3\3\3\7\3&\n\3\f\3\16")
        buf.write("\3)\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\7\rn\n\r\f\r\16\rq\13\r\2\2\16\3\2")
        buf.write("\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\3")
        buf.write("\2\6\4\2\f\f\17\17\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\2s\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\37\3\2\2")
        buf.write("\2\5!\3\2\2\2\7,\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r")
        buf.write("9\3\2\2\2\17B\3\2\2\2\21G\3\2\2\2\23Q\3\2\2\2\25\\\3\2")
        buf.write("\2\2\27f\3\2\2\2\31k\3\2\2\2\33\34\7^\2\2\34 \7$\2\2\35")
        buf.write("\36\7^\2\2\36 \7p\2\2\37\33\3\2\2\2\37\35\3\2\2\2 \4\3")
        buf.write("\2\2\2!\"\7\61\2\2\"#\7\61\2\2#\'\3\2\2\2$&\n\2\2\2%$")
        buf.write("\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'")
        buf.write("\3\2\2\2*+\b\3\2\2+\6\3\2\2\2,-\t\3\2\2-.\3\2\2\2./\b")
        buf.write("\4\2\2/\b\3\2\2\2\60\61\7-\2\2\61\n\3\2\2\2\62\63\7c\2")
        buf.write("\2\63\64\7i\2\2\64\65\7g\2\2\65\66\7p\2\2\66\67\7v\2\2")
        buf.write("\678\7g\2\28\f\3\2\2\29:\7u\2\2:;\7k\2\2;<\7p\2\2<=\7")
        buf.write("g\2\2=>\7t\2\2>?\7i\2\2?@\7k\2\2@A\7c\2\2A\16\3\2\2\2")
        buf.write("BC\7o\2\2CD\7c\2\2DE\7r\2\2EF\7c\2\2F\20\3\2\2\2GH\7g")
        buf.write("\2\2HI\7p\2\2IJ\7e\2\2JK\7q\2\2KL\7p\2\2LM\7v\2\2MN\7")
        buf.write("t\2\2NO\7c\2\2OP\7t\2\2P\22\3\2\2\2QR\7e\2\2RS\7q\2\2")
        buf.write("ST\7o\2\2TU\7r\2\2UV\7q\2\2VW\7u\2\2WX\7k\2\2XY\7e\2\2")
        buf.write("YZ\7c\2\2Z[\7q\2\2[\24\3\2\2\2\\]\7u\2\2]^\7k\2\2^_\7")
        buf.write("p\2\2_`\7g\2\2`a\7t\2\2ab\7i\2\2bc\7k\2\2cd\7c\2\2de\7")
        buf.write("u\2\2e\26\3\2\2\2fg\7r\2\2gh\7c\2\2hi\7t\2\2ij\7c\2\2")
        buf.write("j\30\3\2\2\2ko\t\4\2\2ln\t\5\2\2ml\3\2\2\2nq\3\2\2\2o")
        buf.write("m\3\2\2\2op\3\2\2\2p\32\3\2\2\2qo\3\2\2\2\6\2\37\'o\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class ValorantLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMENTARIO = 1
    WS = 2
    OP = 3
    AGENTE = 4
    SINERGIA = 5
    MAPA = 6
    ENCONTRAR = 7
    COMPOSICAO = 8
    SINERGIAS = 9
    PARA = 10
    IDENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'agente'", "'sinergia'", "'mapa'", "'encontrar'", "'composicao'", 
            "'sinergias'", "'para'" ]

    symbolicNames = [ "<INVALID>",
            "COMENTARIO", "WS", "OP", "AGENTE", "SINERGIA", "MAPA", "ENCONTRAR", 
            "COMPOSICAO", "SINERGIAS", "PARA", "IDENT" ]

    ruleNames = [ "ESC_SEQ", "COMENTARIO", "WS", "OP", "AGENTE", "SINERGIA", 
                  "MAPA", "ENCONTRAR", "COMPOSICAO", "SINERGIAS", "PARA", 
                  "IDENT" ]

    grammarFileName = "Valorant.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


