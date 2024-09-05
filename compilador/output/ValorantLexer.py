# Generated from Valorant.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tL\n\t\3\n\3\n\3\n\3\n\7")
        buf.write("\nR\n\n\f\n\16\nU\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\7\ra\n\r\f\r\16\rd\13\r\2\2\16\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\2\23\n\25\13\27\f\31\r\3\2\6\4")
        buf.write("\2\f\f\17\17\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\2f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5")
        buf.write("\"\3\2\2\2\7+\3\2\2\2\t\60\3\2\2\2\13:\3\2\2\2\r<\3\2")
        buf.write("\2\2\17@\3\2\2\2\21K\3\2\2\2\23M\3\2\2\2\25X\3\2\2\2\27")
        buf.write("\\\3\2\2\2\31^\3\2\2\2\33\34\7c\2\2\34\35\7i\2\2\35\36")
        buf.write("\7g\2\2\36\37\7p\2\2\37 \7v\2\2 !\7g\2\2!\4\3\2\2\2\"")
        buf.write("#\7u\2\2#$\7k\2\2$%\7p\2\2%&\7g\2\2&\'\7t\2\2\'(\7i\2")
        buf.write("\2()\7k\2\2)*\7c\2\2*\6\3\2\2\2+,\7o\2\2,-\7c\2\2-.\7")
        buf.write("r\2\2./\7c\2\2/\b\3\2\2\2\60\61\7g\2\2\61\62\7p\2\2\62")
        buf.write("\63\7e\2\2\63\64\7q\2\2\64\65\7p\2\2\65\66\7v\2\2\66\67")
        buf.write("\7t\2\2\678\7c\2\289\7t\2\29\n\3\2\2\2:;\7\f\2\2;\f\3")
        buf.write("\2\2\2<=\7e\2\2=>\7q\2\2>?\7o\2\2?\16\3\2\2\2@A\7o\2\2")
        buf.write("AB\7c\2\2BC\7r\2\2CD\7c\2\2DE\7u\2\2EF\7<\2\2F\20\3\2")
        buf.write("\2\2GH\7^\2\2HL\7$\2\2IJ\7^\2\2JL\7p\2\2KG\3\2\2\2KI\3")
        buf.write("\2\2\2L\22\3\2\2\2MN\7\61\2\2NO\7\61\2\2OS\3\2\2\2PR\n")
        buf.write("\2\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2")
        buf.write("\2US\3\2\2\2VW\b\n\2\2W\24\3\2\2\2XY\t\3\2\2YZ\3\2\2\2")
        buf.write("Z[\b\13\2\2[\26\3\2\2\2\\]\7-\2\2]\30\3\2\2\2^b\t\4\2")
        buf.write("\2_a\t\5\2\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c")
        buf.write("\32\3\2\2\2db\3\2\2\2\6\2KSb\3\b\2\2")
        return buf.getvalue()


class ValorantLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    COMENTARIO = 8
    WS = 9
    OP = 10
    IDENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'agente'", "'sinergia'", "'mapa'", "'encontrar'", "'\n'", "'com'", 
            "'mapas:'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "COMENTARIO", "WS", "OP", "IDENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "ESC_SEQ", "COMENTARIO", "WS", "OP", "IDENT" ]

    grammarFileName = "Valorant.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


