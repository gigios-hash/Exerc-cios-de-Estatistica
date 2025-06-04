"""
1. Na análise de concessão de empréstimos, uma variável potencialmente
importante é a renda da pessoa. O gerente de um banco coleta uma base de
dados de seus correntistas e extrai a variável “renda mensal (R$)” para 50
pessoas. Embora se trate de uma variável quantitativa, deseja realizar uma
análise por meio de tabela de frequências. Neste sentido, pede-se:
a) Classifique os correntistas em faixas de renda, sendo: 0-2.000; 2.001-4.000;
4.001-6.000; 6.001-8.000; 8.001-10.000 e 10.001-12.000.
b) Em seguida, elabore a tabela de frequências para as faixas de renda acima.
O banco de dados está na planilha Lista de Exercício Complementares: aba
Exercício 1.

"""


import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel('C:/Users/GiovanniNascimento/OneDrive - ASMODEE GROUP/Área de Trabalho/MBA_USP/1-Semestre/3-Introdução à Programação com Python I/Exercícios de Estatistica/exercicio_1.xlsx')

tabela_organizada = tabela.sort_values(by='Renda (R$)',ascending=True)

faixa_renda = pd.DataFrame(columns=['Faixa de Renda', 'Frequência Absoluta', 'Frequência Relativa', 'Frequência Absoluta Acumulada','Frequência Relativa Acumulada'])
faixa_renda['Faixa de Renda'] = ['0-2.000', '2.001-4.000', '4.001-6.000', '6.001-8.000', '8.001-10.000', '10.001-12.000']
faixa_renda['Frequência Absoluta'] = [0, 0, 0, 0, 0, 0]

for i in range(len(tabela_organizada)):
    if tabela_organizada['Renda (R$)'].iloc[i] <= 2000:
        faixa_renda['Frequência Absoluta'].iloc[0] += 1
    elif tabela_organizada['Renda (R$)'].iloc[i] <= 4000:
        faixa_renda['Frequência Absoluta'].iloc[1] += 1
    elif tabela_organizada['Renda (R$)'].iloc[i] <= 6000:
        faixa_renda['Frequência Absoluta'].iloc[2] += 1
    elif tabela_organizada['Renda (R$)'].iloc[i] <= 8000:
        faixa_renda['Frequência Absoluta'].iloc[3] += 1
    elif tabela_organizada['Renda (R$)'].iloc[i] <= 10000:
        faixa_renda['Frequência Absoluta'].iloc[4] += 1
    else:
        faixa_renda['Frequência Absoluta'].iloc[5] += 1

faixa_renda['Frequência Relativa'] = faixa_renda['Frequência Absoluta'] / faixa_renda['Frequência Absoluta'].sum()
faixa_renda['Frequência Absoluta Acumulada'] = faixa_renda['Frequência Absoluta'].cumsum()
faixa_renda['Frequência Relativa Acumulada'] = faixa_renda['Frequência Relativa'].cumsum()
faixa_renda.sort_values(by='Frequência Absoluta', ascending=False, inplace=True)
print(faixa_renda)

plt.figure(figsize=(10, 6))
plt.bar(faixa_renda['Faixa de Renda'], faixa_renda['Frequência Absoluta'], color='skyblue')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Distribuição da Renda')
plt.xlabel('Faixa de Renda')
plt.ylabel('Frequência Absoluta')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()