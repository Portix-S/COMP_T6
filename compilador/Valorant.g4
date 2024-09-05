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

// Variáveis
IDENT : ('a'..'z'|'A'..'Z' | '_') ('_' | 'a'..'z'|'A'..'Z'|'0'..'9')* ;
unidade: IDENT;

// Regras de produção da gramática TFT.
sinergia_dupla: unidade OP unidade;
sinergia_completa: unidade OP unidade OP unidade OP unidade OP unidade;

declaracao_unidade: 'agente' unidade;
declaracao_sinergia: 'sinergia' sinergia_dupla;
declaracao_mapas: 'mapa' sinergia_completa;

declaracao: declaracao_unidade | declaracao_sinergia | declaracao_mapas;
declaracoes: (declaracao)*;

saida: 'encontrar' (saida_sinergia);
saida_sinergia: (saida_sinergia_dupla)* '\n' (saida_mapa)*;
saida_sinergia_dupla: 'sinergia' 'com' (sinergia_dupla)* '\n';
saida_mapa: 'mapas:' sinergia_completa '\n';

programa: declaracoes saida EOF;
