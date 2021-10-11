from math import e,exp,sqrt

limite_inferior = 1
limite_superior = 4
f = lambda x:sqrt(x)
divisoes = 6

h = (limite_superior-limite_inferior)/divisoes

valores_x = [limite_inferior+h*x for x in range(1,divisoes)]

Is = h/3 * (f(limite_inferior) + sum([2*f(x) if i&1 else 4*f(x) for i,x in enumerate(valores_x)]) + f(limite_superior))

print(Is)