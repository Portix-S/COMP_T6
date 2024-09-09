from ValorantVisitor import ValorantVisitor
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo
from ValorantSemanticoUtils import ValorantSemanticoUtils
from ValorantParser import ValorantParser
# from compilador.ValorantParser import ValorantParser

# Análise semântica do compilador
# implementamos algumas funções da classe visitor gerada pelo antlr.
class ValorantSemantico(ValorantVisitor) :

    tabela: TabelaDeSimbolos = TabelaDeSimbolos(Tipo.__INTERNAL__)

    # Começo da árvore gerada pela análise sintática
    def visitPrograma(self, ctx: ValorantParser.ProgramaContext):
        return super().visitPrograma(ctx)

    def visitDeclaracao(self, ctx:ValorantParser.DeclaracaoContext):
        return super().visitDeclaracao(ctx)
    
    def visitDeclaracao_mapa(self, ctx:ValorantParser.Declaracao_mapasContext):
        mapa: ValorantParser.MapaContext = ctx.mapa()
        id_mapa = mapa.getText()
        if self.tabela.existe(id_mapa):
            ValorantSemanticoUtils.adicionarErroSemantico(mapa.start, f'identificador {id_mapa} ja declarado anteriormente')
        else:
            self.tabela.adicionar(id_mapa, Tipo.Mapa)
        return super().visitDeclaracao_mapa(ctx)
    
    def visitDeclaracao_sinergia(self, ctx:ValorantParser.Declaracao_sinergiaContext):
        sinergia: ValorantParser.SinergiaContext = ctx.sinergia()
        id_sinergia = sinergia.getText()
        if self.tabela.existe(id_sinergia):
            ValorantSemanticoUtils.adicionarErroSemantico(sinergia.start, f'identificador {id_sinergia} ja declarado anteriormente')
        else:
            caracteristica = ctx.caracteristica().getText()
            if not self.tabela.existe(caracteristica):
                ValorantSemanticoUtils.adicionarErroSemantico(sinergia.start, f'caracteristica {caracteristica} nao declarada')
            else:
                quantidade = int(ctx.NUMERO().getText())
                self.tabela.adicionar(id_sinergia, Tipo.SINERGIA, quantidade=quantidade, caracteristicas=list(caracteristica))
        return super().visitDeclaracao_sinergia(ctx)
    
    def visitDeclaracao_unidade(self, ctx:ValorantParser.Declaracao_unidadeContext):
        unidade: ValorantParser.UnidadeContext = ctx.unidade()
        id_unidade = unidade.getText()
        if self.tabela.existe(id_unidade):
            ValorantSemanticoUtils.adicionarErroSemantico(unidade.start, f'identificador {id_unidade} ja declarado anteriormente')
        else:
            caracteristicas: list[str] = list()
            for caracteristica in ctx.caracteristica():
                id_caracteristica = caracteristica.getText()
                caracteristicas.append(id_caracteristica)
            self.tabela.adicionar(id_unidade, Tipo.UNIDADE, caracteristicas=caracteristicas)
        return super().visitDeclaracao_unidade(ctx)
    
    def visitSaida(self, ctx: ValorantParser.SaidaContext):
        return super().visitSaida(ctx)
    
    def visitSaida_sinergia(self, ctx: ValorantParser.Saida_sinergiaContext):
        for unidade in ctx.unidade():
            tipo = self.tabela.verificar(unidade.getText())
            if not self.tabela.existe(unidade.getText()):
                ValorantSemanticoUtils.adicionarErroSemantico(unidade.start, f'unidade {unidade.getText()} nao declarada')
            elif tipo != Tipo.UNIDADE:
                ValorantSemanticoUtils.adicionarErroSemantico(unidade.start, f'identificador {unidade.getText()} nao representa uma unidade\n  tipo esperado: unidade\n  tipo encontrado: { ValorantSemanticoUtils.getTipoString(tipo) }')
        return super().visitSaida_sinergia(ctx)