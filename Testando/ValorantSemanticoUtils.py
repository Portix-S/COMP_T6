from ValorantParser import ValorantParser as LAParser
from TabelaDeSimbolos import TabelaDeSimbolos;
from TabelaDeSimbolos import Tipo;

def debug(string: str, msg_prefix):
    if string.find('&') != -1 and False:
        print(f'{msg_prefix}: {string}')

# Classe responsável por verificação de erros, avaliamos, recursivamente, os principais componentes da gramática LA.
class ValorantSemanticoUtils:
    errosSemanticos: list[str] = []
    
    @staticmethod
    def adicionarErroSemantico(token, mensagem: str):
        linha: int = token.line
        ValorantSemanticoUtils.errosSemanticos.append(f"Linha {linha}: {mensagem}")
    
    @staticmethod
    def getTipoString(tipo: Tipo):
        if tipo == Tipo.MAPA:
            return 'mapa'
        if tipo == Tipo.SINERGIA:
            return 'sinergia'
        if tipo == Tipo.UNIDADE:
            return 'unidade'
        return 'invalido'
