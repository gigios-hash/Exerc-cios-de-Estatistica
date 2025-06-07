"""
4. (Fonte: Fávero e Belfiore, 2024, Cap. 5) Suponha que um aluno acerte três
questões a cada cinco testes. Seja X o número de tentativas até o décimo
segundo acerto. Determine a probabilidade de que o aluno precise fazer 20
questões para acertar 12.
"""

from scipy.stats import nbinom

# P(X=k) = 10,78%

p = 3/5 # p (probabilidade de sucesso)
k = 20 - 12 # x (número de ensaios) - k (quantidade de sucessos de interesse)
n= 12

resposta = nbinom.pmf(k,n,p)
print(f"P(X=k) = {resposta:.2%}")
