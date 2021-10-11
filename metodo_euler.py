# METODO DE EULER POR ANDRE UZIEL DRE 119051475 PARA DISCIPLINA CALCULO NUMERICO 2021.1
f = lambda x,y: 0.04*y # DEFINE A FUNCAO Y'
x_inicial= 0 # VALOR INICIAL DE X NO FORMATO
y_inicial = 1000 # VALOR INICIAL DE Y
x_final= 1 # VALOR DE X CUJO Y QUEREMOS DESCOBRIR
delta_x = 0.1 # TAMANHO DO PASSO

y_atual = y_inicial 
n_passos = int(x_final/delta_x) # DEFINE QUANTOS PASSOS SERÃO NECESSÁRIOS

for i in range(n_passos):
  y_atual = y_atual+delta_x*f(x_inicial+i*delta_x,y_atual) # ENCONTRA O Y ATUAL
  print(f"y_{i+1} = {y_atual}")
