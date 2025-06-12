"""
6. Nos últimos meses, foram feitas medições do tempo decorrido entre o início
e finalização de uma das etapas do processo de produção de certo produto. O
tempo médio foi calculado em 26,5 minutos e o desvio padrão foi de 4,0
minutos. Sabendo que tal variável segue uma distribuição normal, identifique
as seguintes informações:

a) P(X>37)
b) P(X<20)
c) P(22<X<28)
"""

# média -> 26,5 min
# desvio padrão -> 4 min
# calculo -> (x - média) / devio padrão

from scipy.stats import norm

media = 26.5
desvio_padrao = 4

x = 37

a = (x - media) / desvio_padrao
z1 = 1 - norm.cdf(a)
print(f"a) P(X>37) = {a} -> P(Z>2,625) = {z1}")

x = 20

b = (x - media) / desvio_padrao
z2 = norm.cdf(a)
print(f"b) P(X<20) = {b} -> P(Z<-1,625) = {z2}")

x1 = 22
x2 = 28

c = [(x1 - media) / desvio_padrao, (x2 - media) / desvio_padrao ]
z3 = norm.cdf(c[0])
z4 = norm.cdf(c[1])
print(f"c) P(22<X<28) = {c[0]} e {c[1]} -> P(-1,125<Z<0,375) = {z3} e {z4}")
