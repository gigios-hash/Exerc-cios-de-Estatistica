"""
2. Um analista do mercado acionário coletou os retornos mensais de duas
ações que pretende indicar aos seus clientes. Calcule as estatísticas
descritivas para as duas variáveis. O banco de dados com os retornos
percentuais mensais está na planilha Lista de Exercício Complementares: aba
Exercício 2. Posteriormente, analise o coeficiente de correlação de Pearson
entre os retornos.
"""

import pandas as pd

tabela = pd.read_excel('exercicio_2.xlsx')

print(tabela)

tabela_descritiva = pd.DataFrame(columns=['Descritivas','Ação 1','Ação 2'])
tabela_descritiva['Descritivas'] = [
    'Nº Observações',
    'Média',
    'Mediana',
    'Moda',
    '1º Quartil',
    '3º Quartil',
    '8º Decil',
    '9º Decil',
    '27º Percentil',
    '64º Percentil',
    'Valor Mínimo',
    'Valor Máximo',
    'Amplitude',
    'Variância',
    'Desvio Padrão',
    'Erro Padrão',
    'Coeficiente de Variação'
]

colunas = ['Ação 1', 'Ação 2']
for col in colunas:
    tabela_descritiva[col][0] = tabela[col].count()
    tabela_descritiva[col][1] = tabela[col].mean()
    tabela_descritiva[col][2] = tabela[col].median()
    tabela_descritiva[col][3] = tabela[col].mode()[0]
    tabela_descritiva[col][4] = tabela[col].quantile(0.25)
    tabela_descritiva[col][5] = tabela[col].quantile(0.75)
    tabela_descritiva[col][6] = tabela[col].quantile(0.8)
    tabela_descritiva[col][7] = tabela[col].quantile(0.9)
    tabela_descritiva[col][8] = tabela[col].quantile(0.27)
    tabela_descritiva[col][9] = tabela[col].quantile(0.64)
    tabela_descritiva[col][10] = tabela[col].min()
    tabela_descritiva[col][11] = tabela[col].max()
    tabela_descritiva[col][12] = tabela_descritiva[col][11] - tabela_descritiva[col][10]
    tabela_descritiva[col][13] = tabela[col].var()
    tabela_descritiva[col][14] = tabela[col].std()
    tabela_descritiva[col][15] = tabela[col].sem()
    tabela_descritiva[col][16] = tabela_descritiva[col][14] / tabela_descritiva[col][1]

tabela_descritiva = tabela_descritiva.set_index('Descritivas')

print(tabela_descritiva)