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
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\5\tY\n\t\3\n\3\n\3\n\3\n\7\n")
        buf.write("_\n\n\f\n\16\nb\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\7\rn\n\r\f\r\16\rq\13\r\2\2\16\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\2\23\n\25\13\27\f\31\r\3\2\6\4\2")
        buf.write("\f\f\17\17\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\"")
        buf.write("\3\2\2\2\7+\3\2\2\2\t\60\3\2\2\2\13;\3\2\2\2\rE\3\2\2")
        buf.write("\2\17O\3\2\2\2\21X\3\2\2\2\23Z\3\2\2\2\25e\3\2\2\2\27")
        buf.write("i\3\2\2\2\31k\3\2\2\2\33\34\7c\2\2\34\35\7i\2\2\35\36")
        buf.write("\7g\2\2\36\37\7p\2\2\37 \7v\2\2 !\7g\2\2!\4\3\2\2\2\"")
        buf.write("#\7u\2\2#$\7k\2\2$%\7p\2\2%&\7g\2\2&\'\7t\2\2\'(\7i\2")
        buf.write("\2()\7k\2\2)*\7c\2\2*\6\3\2\2\2+,\7o\2\2,-\7c\2\2-.\7")
        buf.write("r\2\2./\7c\2\2/\b\3\2\2\2\60\61\7e\2\2\61\62\7q\2\2\62")
        buf.write("\63\7o\2\2\63\64\7r\2\2\64\65\7q\2\2\65\66\7u\2\2\66\67")
        buf.write("\7k\2\2\678\7e\2\289\7c\2\29:\7q\2\2:\n\3\2\2\2;<\7g\2")
        buf.write("\2<=\7p\2\2=>\7e\2\2>?\7q\2\2?@\7p\2\2@A\7v\2\2AB\7t\2")
        buf.write("\2BC\7c\2\2CD\7t\2\2D\f\3\2\2\2EF\7u\2\2FG\7k\2\2GH\7")
        buf.write("p\2\2HI\7g\2\2IJ\7t\2\2JK\7i\2\2KL\7k\2\2LM\7c\2\2MN\7")
        buf.write("u\2\2N\16\3\2\2\2OP\7r\2\2PQ\7c\2\2QR\7t\2\2RS\7c\2\2")
        buf.write("S\20\3\2\2\2TU\7^\2\2UY\7$\2\2VW\7^\2\2WY\7p\2\2XT\3\2")
        buf.write("\2\2XV\3\2\2\2Y\22\3\2\2\2Z[\7\61\2\2[\\\7\61\2\2\\`\3")
        buf.write("\2\2\2]_\n\2\2\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2ac\3\2\2\2b`\3\2\2\2cd\b\n\2\2d\24\3\2\2\2ef\t\3\2\2")
        buf.write("fg\3\2\2\2gh\b\13\2\2h\26\3\2\2\2ij\7-\2\2j\30\3\2\2\2")
        buf.write("ko\t\4\2\2ln\t\5\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3")
        buf.write("\2\2\2p\32\3\2\2\2qo\3\2\2\2\6\2X`o\3\b\2\2")
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
            "'agente'", "'sinergia'", "'mapa'", "'composicao'", "'encontrar'", 
            "'sinergias'", "'para'", "'+'" ]

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


