grammar Valorant;

// Comentarios e espacos em branco
fragment
ESC_SEQ	: '\\"' | '\\n';

// Comentários são iniciados por '//' e se estendem por uma linha
COMENTARIO: ('//' ~('\n' | '\r')*) -> skip;

// Espaços em branco são ignorados.
WS: ( ' ' | '\t' | '\r' | '\n') -> skip;

// Detecção de operação
OP: '+';

// Palavras reservadas
AGENTE : 'agente';
SINERGIA : 'sinergia';
MAPA : 'mapa';
ENCONTRAR : 'encontrar';
COMPOSICAO : 'composicao';
SINERGIAS : 'sinergias';
PARA : 'para';

// Variáveis
IDENT : ('a'..'z'|'A'..'Z' | '_') ('_' | 'a'..'z'|'A'..'Z'|'0'..'9')* ;
unidade: IDENT;
sinergia: IDENT;
mapa: IDENT;

// Regras de produção da gramática Valorant.
sinergia_dupla: unidade unidade;
sinergia_completa: unidade OP unidade OP unidade OP unidade OP unidade OP unidade;

declaracao_unidade: 'agente' unidade;
declaracao_sinergia: 'sinergia' sinergia sinergia_dupla;
declaracao_mapas: 'mapa' mapa 'composicao' sinergia_completa;

declaracao: declaracao_unidade | declaracao_sinergia | declaracao_mapas;
declaracoes: (declaracao)*;

saida: 'encontrar' saida_sinergia;
saida_sinergia: 'sinergias' 'para' unidade;

programa: declaracoes saida EOF;
