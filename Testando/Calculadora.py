from ValorantVisitor import ValorantVisitor
from TabelaDeSimbolos import TabelaDeSimbolos, Tipo, InfoTipo
from ValorantSemanticoUtils import ValorantSemanticoUtils
from ValorantParser import ValorantParser
# from compilador.ValorantParser import ValorantParser

# Análise semântica do compilador
# implementamos algumas funções da classe visitor gerada pelo antlr.
class Calculadora(ValorantVisitor) :

    tabela: TabelaDeSimbolos = TabelaDeSimbolos(Tipo.__INTERNAL__)
    respostas: list[str] = []

    # Começo da árvore gerada pela análise sintática
    def visitPrograma(self, ctx: ValorantParser.ProgramaContext):
        print('programa: \n')
        for declaracao in ctx.declaracoes().declaracao():
            self.visitDeclaracao(declaracao)
        
        if ctx.saida():
            self.visitSaida(ctx.saida())

        return super().visitPrograma(ctx)

    # A linguagem Valorant contém apenas declarações simples de escopo único
    def visitDeclaracao(self, ctx:ValorantParser.DeclaracaoContext):
        print('Visitando declaracao\n')

        if ctx.declaracao_unidade():
            return self.visitDeclaracao_unidade(ctx.declaracao_unidade())
        elif ctx.declaracao_sinergia():
            return self.visitDeclaracao_sinergia(ctx.declaracao_sinergia())
        elif ctx.declaracao_mapas():
            return self.visitDeclaracao_mapa(ctx.declaracao_mapas())
    
    def visitDeclaracao_mapa(self, ctx:ValorantParser.Declaracao_mapasContext):
        print(' Declaração mapa\n')
        mapa = ctx.mapa().getText()
        print(f'    Mapa: {mapa}')
        
        if ctx.COMPOSICAO():
            print('    Composição encontrada')
        
        sinergia_completa = ctx.sinergia_completa()
        if sinergia_completa:
            unidades = [u.getText() for u in sinergia_completa.unidade()]
            print('    Sinergias:')
            for unidade in unidades:
                print(f'      {unidade}')
        
        self.tabela.adicionar(mapa, Tipo.MAPA, unidades)
        informacao = []
        informacao.append(mapa)
        for unidade in unidades[1:]:
            self.tabela.atualizar(unidade, informacao)
        return super().visitDeclaracao_mapa(ctx)

    def visitDeclaracao_sinergia(self, ctx:ValorantParser.Declaracao_sinergiaContext):
        # print(ctx.getText())
        print(' Declaração sinergia\n')

        # Obtendo o identificador de sinergia
        sinergia: ValorantParser.SinergiaContext = ctx.sinergia()
        id_sinergia = sinergia.getText()
        print('     ' + id_sinergia)

        # Obtendo as unidades da sinergia
        unidades = []
        sinergia_dupla = ctx.sinergia_dupla()
        if sinergia_dupla:
            for unidade_ctx in sinergia_dupla.unidade():
                unidades.append(unidade_ctx.getText())

        # Printando as unidades da sinergia
        print('     Unidades:')
        for unidade in unidades:
            print('       ' + unidade)

        self.tabela.adicionar(id_sinergia, Tipo.SINERGIA, unidades)
        self.tabela.atualizar(unidades[0], unidades)
        self.tabela.atualizar(unidades[1], unidades)

        return super().visitDeclaracao_sinergia(ctx)
    
    def visitDeclaracao_unidade(self, ctx:ValorantParser.Declaracao_unidadeContext):
        print(' Declaração unidade\n')

        # Obtendo o identificador de unidade
        unidade: ValorantParser.UnidadeContext = ctx.unidade()
        id_unidade = unidade.getText()
        print('     agente: ' + id_unidade)


        self.tabela.adicionar(id_unidade, Tipo.UNIDADE)
        return super().visitDeclaracao_unidade(ctx)
    
    def visitSaida(self, ctx: ValorantParser.SaidaContext):
        print('--' * 30)
        sinergia = ctx.saida_sinergia()
        if ctx.saida_sinergia():
            return self.visitSaida_sinergia(ctx.saida_sinergia())
        return super().visitSaida_sinergia(ctx)
    
    def visitSaida_sinergia(self, ctx: ValorantParser.Saida_sinergiaContext):
        unidade = ctx.unidade().getText()
        
        print('Agente: ' + unidade)

        # Pegando as sinergias com agentes
        agentes = self.tabela.tabela[unidade].mapas
        agentes_string = unidade + ' possui sinergia com: '
        auxiliar = '\n' + unidade + ' participa das seguintes composicoes: '
        mapas = []

        for agente in agentes:
            if self.tabela.tabela[agente].tipo == Tipo.UNIDADE:
                agentes_string += agente + '; '
            else:
                mapas.append(agente)

        # Pegando as composições do agente
        composicoes = []
        for composicao in mapas:
            informacao = self.tabela.tabela[composicao].mapas
            agentes_composicao = ''
            for info in informacao[1:]:
                agentes_composicao += info + ' '
            texto = '\n     ' + informacao[0] + ': ' + agentes_composicao
            composicoes.append(texto)

        self.respostas.append(agentes_string)
        self.respostas.append(auxiliar)

        for a in composicoes:
            self.respostas.append(a)
        
        return super().visitSaida_sinergia(ctx)

    def getCaracteristicasCount(self, infoTipo: InfoTipo):
        quantidades: dict[str, int] = {}
        for caracteristica in infoTipo.caracteristicas:
            if quantidades.get(caracteristica) == None:
                quantidades[caracteristica] = 1
            else:
                quantidades[caracteristica] += 1
        return quantidades