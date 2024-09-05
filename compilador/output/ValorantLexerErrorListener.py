from antlr4.error.ErrorListener import ErrorListener

# Implementamos a interface ErrorListener para tratamento de erros léxicos
# https://github.com/antlr/antlr4/blob/master/runtime/Python3/src/antlr4/error/ErrorListener.py
# https://www.antlr.org/api/Java/org/antlr/v4/runtime/BaseErrorListener.html#syntaxError(org.antlr.v4.runtime.Recognizer,java.lang.Object,int,int,java.lang.String,org.antlr.v4.runtime.RecognitionException)
class ValorantLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Analisa o tipo de erro e lança a excecao.
        # OffendingSymbol não funciona para erros léxicos.
        # Para resolver esse problema, verificamos o que cada parâmetro imprime na tela
        # daí fizemos um split na string do parâmetro e para verificar o caractere que 
        # acionou essa função. 

        lex_error = str(e).split("(")[1][1]

        if lex_error == '/':
            raise Exception(f'Linha {line}: comentario malformado')
        else:
            raise Exception(f'Linha {line}: {lex_error} - simbolo nao identificado')