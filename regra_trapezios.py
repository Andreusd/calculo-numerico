from math import e,exp,sqrt

limite_inferior = 1
limite_superior = 2
f = lambda x:exp(x)
divisoes = 6

h = (limite_superior-limite_inferior)/divisoes

valores_x = [limite_inferior+h*x for x in range(1,divisoes)]

It = h/2 * (f(limite_inferior) + sum([2*f(x) for x in valores_x]) + f(limite_superior))

print(It)