"""
5. Suponha que o número de acidentes de trânsito em determinada cidade seja,
em média, de 5 acidentes por dia e que siga uma distribuição Poisson. Calcule
a probabilidade de que, em tal cidade, ocorram 9 acidentes de trânsito em um
dia.
"""

from scipy.stats import poisson

# λ (taxa média de ocorrências) = 5
# k (quantidade de ocorrências de interesse) = 9
# probabilidade (X=k) = 3,627%

resposta = poisson.pmf(9,5)
print(f"{resposta:.3%}")