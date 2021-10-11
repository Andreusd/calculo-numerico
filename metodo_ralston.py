
f = lambda x,y: 0.04*y
x_inicial= 0
y_inicial = 1000
x_final= 1
delta_x = 0.1

y_atual = y_inicial
n_passos = int(x_final/delta_x)

for i in range(n_passos):
  k1 = delta_x*f(x_inicial+i*delta_x,y_atual)
  k2 = delta_x*f(x_inicial+1/2*delta_x,y_atual+1/2*k1)
  k3 = delta_x*f(x_inicial+3/4*delta_x,y_atual+3/4*k2)
  y_atual = y_atual+1/9*(2*k1+3*k2+4*k3)
  print(f"y_{i+1} = {y_atual}")
