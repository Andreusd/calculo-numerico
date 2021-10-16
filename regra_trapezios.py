# REGRA DOS TRAPEZIOS POR ANDRE UZIEL
from math import e,exp,sqrt,cos

limite_inferior = 0 # LIMITE INFERIOR DA INTEGRAL
limite_superior = 1 # LIMITE SUPERIOR DA INTEGRAL
f = lambda x:exp(x**2) # FUNCAO DA INTEGRAL
divisoes = 12 # NUMERO DE DIVISOES DO INTERVALO

h = (limite_superior-limite_inferior)/divisoes # CALCULA O TAMANHO DO PASSO
print(f"h={h}")

valores_x = [limite_inferior+h*x for x in range(1,divisoes)] # CALCULA OS PONTOS NO INTERVALO

It = h/2 * (f(limite_inferior) + sum([2*f(x) for x in valores_x]) + f(limite_superior)) # EXECUCAO DA REGRA

print(f"It={It}")