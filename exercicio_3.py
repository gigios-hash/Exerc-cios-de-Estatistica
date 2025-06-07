"""

3. Em certo jogo, probabilidade de vitória (sucesso) a cada nova jogada é 1/6.
Se forem feitas 10 jogadas, quais são as seguintes probabilidades:
a) Ter vitória em 4 jogadas.
b) Ter vitória em pelo menos 7 jogadas.

"""

from scipy.stats import binom 

p = 1/6
n = 10
k = 4

# a) P(X=4) = 5,43%

resposta_a = binom.pmf(k,n,p)
print(f"a) P(k = 4) = {resposta_a:.2%}.")

# 1º Método:
# b) P(X ≥ 7) = P(X=7) + P(X=8) + P(X=9) + P(X=10) = 0,0268%

resposta_b = 0

for k in range(7,n+1):
    k_sucessos= binom.pmf(k,n,p)
    resposta_b += k_sucessos

print(f"Usando Método 1:\nb) P(k=7) + P(k=8) + P(k=9) + P(k=10) = {resposta_b:.4%}.")

# 2º Método:
# P(X >= 7) = 1 - P(X <= 6)

prob_acumulada_ate_6 = binom.cdf(6,n,p)
prob_pelo_menos_7 = 1 - prob_acumulada_ate_6

print(f"Usando Método 2:\nb) P(k=7) + P(k=8) + P(k=9) + P(k=10) = {prob_pelo_menos_7:.4%}.")