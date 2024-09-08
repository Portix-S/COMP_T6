import sys
from antlr4 import *

from ValorantLexerErrorListener import ValorantLexerErrorListener
from ValorantParser import ValorantParser
from ValorantParserErrorListener import ValorantParserErrorListener
from ValorantLexer import ValorantLexer
from ValorantSemanticoUtils import ValorantSemanticoUtils
from ValorantSemantico import ValorantSemantico
from Calculadora import Calculadora

# Código responsável por ler os tokens gerados pela analisador léxico e salvar em um arquivo
def main(argv): 
    # Recebendo o arquivo de entrada
    input_stream = FileStream(argv[1], encoding='utf-8')
    # Arquivo de saida
    output_stream = open(argv[2], 'w')
    # Gerando os tokens
    lexer = ValorantLexer(input_stream)
    # teste = lexer.getAllTokens()
    # for t in teste:
    #     token_type = t.type
    #     if token_type < len(lexer.symbolicNames):
    #         token_name = lexer.symbolicNames[token_type]
    #     else:
    #         token_name = "UNKNOWN"  # Caso o token não tenha um nome definido
    #     print(f"Token: {t.text}, Tipo: {token_name}, Linha: {t.line}, Coluna: {t.column}")
    # # Gerando o parser (Analisador sintático)
    tokens = CommonTokenStream(lexer)
    parser = ValorantParser(tokens)

    # arvore = parser.programa()
    # Tratamento de erros em python
    # Alterando os tratadores padrões de erro para os que criamos
    lexer.removeErrorListeners()
    lexer.addErrorListener(ValorantLexerErrorListener())

    parser.removeErrorListeners()
    parser.addErrorListener(ValorantParserErrorListener())

    try:
        arvore = parser.programa()
        # Executa o parser para análise sintática
        valorantSemantico = ValorantSemantico()
        
        valorantSemantico.visitPrograma(arvore)
        # print(arvore.toStringTree(recog=parser))

        for erro in ValorantSemanticoUtils.errosSemanticos:
            output_stream.write(erro + "\n")
        if len(ValorantSemanticoUtils.errosSemanticos) == 0:
            calculadora = Calculadora()
            calculadora.visitPrograma(arvore)
            for resposta in calculadora.respostas:
                output_stream.write(resposta)
        else:
            output_stream.write("\nFim da compilacao\n")
    except Exception as e:
        # Deteccao de erro sintatico e lexico
        # gracas aos listeners que implementamos
        output_stream.write(str(e))
        output_stream.write("\nFim da compilacao\n")
    output_stream.close()

if __name__ == '__main__':
    main(sys.argv)