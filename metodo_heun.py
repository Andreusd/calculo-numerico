# METODO DE HEUN POR ANDRE UZIEL DRE 119051475 PARA DISCIPLINA CALCULO NUMERICO 2021.1
f = lambda x,y: -x/y # DEFINE A FUNCAO Y'
x_inicial= 0 # VALOR INICIAL DE X NO FORMATO
y_inicial = 20 # VALOR INICIAL DE Y
x_final= 16 # VALOR DE X CUJO Y QUEREMOS DESCOBRIR
delta_x = 4 # TAMANHO DO PASSO

y_atual = y_inicial 
n_passos = int(x_final/delta_x) # DEFINE QUANTOS PASSOS SERÃO NECESSÁRIOS

for i in range(n_passos):
  k1 = delta_x*f(x_inicial+i*delta_x,y_atual) # ENCONTRA K1
  k2 = delta_x*f(x_inicial+(i+1)*delta_x,y_atual+k1) # ENCONTRA K2
  y_atual = y_atual+1/2*(k1+k2) # ENCONTRA O Y ATUAL
  print(f"y_{i+1} = {y_atual}, k1={k1}, k2={k2}")
