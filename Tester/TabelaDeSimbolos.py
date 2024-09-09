from enum import Enum


class Tipo(Enum):
    UNIDADE = "unidade"
    SINERGIA = "sinergia"
    MAPA = "mapa"
    __INTERNAL__ = "__internal__"

class InfoTipo:
    def __init__(self, tipo: Tipo, mapas: list[str]):
        self.tipo = tipo
        self.mapas = mapas
    
    def __str__(self) -> str:
        return f'tipo={self.tipo} mapas={self.mapas}'

class TabelaDeSimbolos():
    def __init__(self, tipo: Tipo):
        self.tabela: dict[str, InfoTipo] = {}
        self.tipo = tipo

    def __str__(self):
        resultado = []
        for id, info in self.tabela.items():
            resultado.append(f"ID: {id}, Tipo: {info.tipo}, Características: {info.mapas}")
        return "\n".join(resultado)

    class EntradaTabelaSimbolos():
        def __init__(self, nome: str, tipo: Tipo, mapas: list[str]):
            self.nome = nome
            self.infoTipo =  InfoTipo(tipo, mapas)

    def atualizar(self, nome: str, mapas: list[str]):
        if nome in self.tabela:
            info = self.tabela[nome]
            
            # Atualizar os mapas, se fornecidos
            if mapas:
                informacao = []
                for mapa in info.mapas:
                    informacao.append(mapa)
                for mapa in mapas:
                    if not mapa == nome:
                        informacao.append(mapa)
                info.mapas = informacao
        else:
            print(f"Erro TAbela: {nome} não encontrado na tabela.")

    def adicionar(self, nome: str, tipo: Tipo, mapas: list[str] = list()):
        if self.existe(nome):
            print(f"Erro Tabela: {nome} já foi declarado anteriormente.")
        else:
            entrada = TabelaDeSimbolos.EntradaTabelaSimbolos(nome, tipo, mapas)
            self.tabela[entrada.nome] = entrada.infoTipo
            print(f"Adicionado Tabela: {nome} com tipo {tipo} e mapas {mapas}")
    
    
    def existe(self, nome: str) -> bool:
        return nome in self.tabela
    
    def verificar(self, nome : str):
        if not self.tabela.get(nome):
            return None
        return self.tabela.get(nome).tipo

