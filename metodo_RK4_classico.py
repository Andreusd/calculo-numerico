
f = lambda x,y: -x/y
x_inicial= 0
y_inicial = 20
x_final= 16
delta_x = 4

y_atual = y_inicial
n_passos = int(x_final/delta_x)

for i in range(n_passos):
  k1 = delta_x*f(x_inicial+i*delta_x,y_atual)
  k2 = delta_x*f(x_inicial+i*delta_x+1/2*delta_x,y_atual+1/2*k1)
  k3 = delta_x*f(x_inicial+i*delta_x+1/2*delta_x,y_atual+1/2*k2)
  k4 = delta_x*f(x_inicial+i*delta_x+delta_x,y_atual+k3)
  y_atual = y_atual+1/6*(k1+2*k2+2*k3+k4)
  print(f"y_{i+1} = {y_atual}")
