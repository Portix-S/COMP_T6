from enum import Enum


class Tipo(Enum):
    UNIDADE = "unidade"
    SINERGIA = "sinergia"
    MAPA = "mapa"
    __INTERNAL__ = "__internal__"

class InfoTipo:
    def __init__(self, tipo: Tipo, quantidade: int, mapas: list[str]):
        self.tipo = tipo
        self.quantidade = quantidade
        self.mapas = mapas
    
    def __str__(self) -> str:
        return f'tipo={self.tipo} quantidade={self.quantidade} mapas={self.mapas}'

class TabelaDeSimbolos():
    def __init__(self, tipo: Tipo):
        self.tabela: dict[str, InfoTipo] = {}
        self.tipo = tipo

    class EntradaTabelaSimbolos():
        def __init__(self, nome: str, tipo: Tipo, quantidade: int, mapas: list[str]):
            self.nome = nome
            self.infoTipo =  InfoTipo(tipo, quantidade, mapas)

    def adicionar(self, nome: str, tipo: Tipo, quantidade: int = 0, mapas: list[str] = list()):
        entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(nome, tipo, quantidade, mapas)
        self.tabela[entrada.nome] = entrada.infoTipo
    
    def existe(self, nome: str) -> bool:
        return self.tabela.get(nome) != None
    
    def verificar(self, nome : str):
        if not self.tabela.get(nome):
            return None
        return self.tabela.get(nome).tipo
