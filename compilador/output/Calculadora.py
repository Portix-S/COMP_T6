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
            print(self.visitDeclaracao(declaracao))

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
        
        self.tabela.adicionar(mapa, Tipo.MAPA)
        return super().visitDeclaracao_mapa(ctx)

    def visitDeclaracao_sinergia(self, ctx:ValorantParser.Declaracao_sinergiaContext):
        print(ctx.getText())
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

        print('tabela')

        self.tabela.adicionar(id_sinergia, Tipo.SINERGIA, unidades[0])
        self.tabela.adicionar(id_sinergia, Tipo.SINERGIA, unidades[1])

        return super().visitDeclaracao_sinergia(ctx)
    
    def visitDeclaracao_unidade(self, ctx:ValorantParser.Declaracao_unidadeContext):
        print(' Declaração unidade\n')

        # Obtendo o identificador de unidade
        unidade: ValorantParser.UnidadeContext = ctx.unidade()
        id_unidade = unidade.getText()
        print('     agente: ' + id_unidade)


        self.tabela.adicionar(id_unidade, Tipo.UNIDADE)
        # return super().visitDeclaracao_unidade(ctx)
    
    def visitSaida(self, ctx: ValorantParser.SaidaContext):
        print('teste')
        return super().visitSaida(ctx)
    
    def visitSaida_sinergia(self, ctx: ValorantParser.Saida_sinergiaContext):
        print('teste')
        possibilidades = []
        unidades = []
        # Atualizar a quantidade de unidades disponiveis para cada caracteristica
        for unidade in ctx.unidade():
            unidades.append(unidade.getText())
            infoUnidade = self.tabela.tabela.get(unidade.getText())
            quantidades = self.getCaracteristicasCount(infoUnidade)
            # Inicializar uma entrada no vetor de possibilidades apenas se uma unidade passada na query de saida
            # possuir tal caracteristica
            for chave, entrada in zip(self.tabela.tabela.keys(), self.tabela.tabela.values()):
                for tipoDisponivel in quantidades.keys():
                    if tipoDisponivel in entrada.caracteristicas and entrada.tipo == Tipo.SINERGIA:
                        possibilidades.append({ 'sinergia': chave, 'quantidade': entrada.quantidade, 'tipo': tipoDisponivel })
        # Calcular de modo guloso
        tiposUtilizados = {}
        for possibilidade in possibilidades:
            if tiposUtilizados.get(possibilidade['tipo']) == None:
                tiposUtilizados[possibilidade['tipo']] = { 'sinergia': possibilidade['sinergia'], 'quantidade': possibilidade['quantidade'] }
            elif possibilidade['quantidade'] > tiposUtilizados[possibilidade['tipo']]['quantidade']:
                tiposUtilizados[possibilidade['tipo']] = { 'sinergia': possibilidade['sinergia'], 'quantidade': possibilidade['quantidade'] }
        # Montando a string contendo a lista de unidades
        unidadesString = ''
        for i in range(len(unidades)):
            unidadesString += unidades[i]
            if i < len(unidades) - 2:
                unidadesString += ', '
            elif i < len(unidades) - 1:
                unidadesString += ' e '
        # Montando a string contendo as sinergias ativadas
        sinergiasString = ''
        contador = 0
        for entrada in tiposUtilizados.values():
            sinergiasString += entrada['sinergia']
            if contador < len(tiposUtilizados.values()) - 2:
                sinergiasString += ', '
            elif contador < len(tiposUtilizados.values()) - 1:
                sinergiasString += ' e '
            contador += 1
        self.respostas.append(f'as unidades {unidadesString} ativam as sinergias {sinergiasString}')
        return super().visitSaida_sinergia(ctx)

    def getCaracteristicasCount(self, infoTipo: InfoTipo):
        quantidades: dict[str, int] = {}
        for caracteristica in infoTipo.caracteristicas:
            if quantidades.get(caracteristica) == None:
                quantidades[caracteristica] = 1
            else:
                quantidades[caracteristica] += 1
        return quantidades