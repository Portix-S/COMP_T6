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

    # A linguagem TFT contém apenas declarações simples de escopo único
    def visitDeclaracao(self, ctx:ValorantParser.DeclaracaoContext):
        return super().visitDeclaracao(ctx)
    
    ## Agente feito
    
    def visitDeclaracao_unidade(self, ctx:ValorantParser.Declaracao_unidadeContext):
        # Obtendo o identificador de unidade
        unidade: ValorantParser.UnidadeContext = ctx.unidade()
        id_unidade = unidade.getText()
    
    # Verifica se a unidade já existe
        if self.tabela.existe(id_unidade):
            # Adiciona erro semântico se já existir
            ValorantSemanticoUtils.adicionarErroSemantico(unidade.start, f'Agente {id_unidade} já foi declarado anteriormente')
            print(f"Erro: {id_unidade} já foi declarado anteriormente.")  
        else:
            # Se não existir, adiciona a unidade
            self.tabela.adicionar(id_unidade, Tipo.UNIDADE)
            print(f"Adicionado {id_unidade}")

        return super().visitDeclaracao_unidade(ctx)


    # Declaração de sinergia
    def visitDeclaracao_sinergia(self, ctx: ValorantParser.Declaracao_sinergiaContext):
    # Obtendo o identificador de sinergia
        sinergia: ValorantParser.SinergiaContext = ctx.sinergia()
        id_sinergia = sinergia.getText()

        # Verificar se a sinergia já foi declarada
        if self.tabela.existe(id_sinergia):
            ValorantSemanticoUtils.adicionarErroSemantico(sinergia.start, f'Sinergia "{id_sinergia}" já declarada anteriormente')
        else:
            # Obtendo as unidades da sinergia
            unidades = []
            sinergia_dupla = ctx.sinergia_dupla()
            if sinergia_dupla:
                for unidade_ctx in sinergia_dupla.unidade():
                    unidades.append(unidade_ctx.getText())

            # Verificar se há agentes repetidos na sinergia
            unidades_repetidas = set(u for u in unidades if unidades.count(u) > 1)
            if unidades_repetidas:
                ValorantSemanticoUtils.adicionarErroSemantico(sinergia.start, f'Sinergia "{id_sinergia}" contém agentes repetidos: {", ".join(unidades_repetidas)}')

            # Adiciona a sinergia e atualiza a tabela de símbolos
            self.tabela.adicionar(id_sinergia, Tipo.SINERGIA, unidades)
            for unidade in unidades:
                if not self.tabela.existe(unidade):
                    ValorantSemanticoUtils.adicionarErroSemantico(sinergia.start, f'Agente "{unidade}" não declarado')
                self.tabela.atualizar(unidade, unidades)
            
        return super().visitDeclaracao_sinergia(ctx)

    
    def visitDeclaracao_mapa(self, ctx: ValorantParser.Declaracao_mapasContext):
        print(' Declaração mapa\n')
        mapa = ctx.mapa().getText()
        print(f'    Mapa: {mapa}')
        
        # Verificar se o mapa já foi declarado
        if self.tabela.existe(mapa):
            ValorantSemanticoUtils.adicionarErroSemantico(ctx.mapa().start, f'Mapa "{mapa}" já declarado anteriormente')
        else:
            # Verificar se o mapa contém agentes que já estão em outro mapa
            unidades = []
            sinergia_completa = ctx.sinergia_completa()
            if sinergia_completa:
                unidades = [u.getText() for u in sinergia_completa.unidade()]
                print('    Sinergias:')
                for unidade in unidades:
                    print(f'      {unidade}')
                
                # Verificar se algum agente já está associado a outro mapa
                for unidade in unidades:
                    if self.tabela.existe(unidade):
                        info = self.tabela.verificar(unidade)
                        if info.tipo == Tipo.MAPA:
                            ValorantSemanticoUtils.adicionarErroSemantico(ctx.mapa().start, f'Agente "{unidade}" já associado ao mapa "{info.nome}"')
                    else:
                        ValorantSemanticoUtils.adicionarErroSemantico(ctx.mapa().start, f'Agente "{unidade}" não declarado')
            
            # Adiciona o mapa e atualiza a tabela de símbolos
            self.tabela.adicionar(mapa, Tipo.MAPA, unidades)
            informacao = [mapa]
            for unidade in unidades:
                self.tabela.atualizar(unidade, informacao)

        return super().visitDeclaracao_mapa(ctx)


