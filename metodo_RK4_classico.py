# METODO RK4 CLASSICO POR ANDRE UZIEL
f = lambda x,y: 2*y**2+3*x # DEFINE A FUNCAO Y'
x_inicial= 0 # VALOR INICIAL DE X
y_inicial = .1 # VALOR INICIAL DE Y
x_final= 1 # VALOR DE X CUJO Y QUEREMOS DESCOBRIR
delta_x = .001 # TAMANHO DO PASSO

y_atual = y_inicial
n_passos = int((x_final-x_inicial)/delta_x) # DEFINE QUANTOS PASSOS SERÃO NECESSÁRIOS

for i in range(n_passos):
  k1 = delta_x*f(x_inicial+i*delta_x,y_atual) # ENCONTRA K1
  k2 = delta_x*f(x_inicial+i*delta_x+1/2*delta_x,y_atual+1/2*k1) # ENCONTRA K2
  k3 = delta_x*f(x_inicial+i*delta_x+1/2*delta_x,y_atual+1/2*k2) # ENCONTRA K3
  k4 = delta_x*f(x_inicial+i*delta_x+delta_x,y_atual+k3) # ENCONTRA K4
  y_atual = y_atual+1/6*(k1+2*k2+2*k3+k4) # ENCONTRA O Y ATUAL
  print(f"y_{i+1} = {y_atual}, k1={k1}, k2={k2}, k3={k3}, k4={k4}") #IMPRIME PARA O USUÁRIO
