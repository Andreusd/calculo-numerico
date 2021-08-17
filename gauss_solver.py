# Feito por Andre Uziel - andreuzielsd@gmail.com

PRECISAO = 10

def imprime_matriz(matriz):
  for linha in matriz:
    print(linha)
  print()

def get_max_posicao(lista):
  max = 0
  pos = 0
  for i in range(len(lista)):
    if (lista[i] > max):
      max = lista[i]
      pos = i
  return pos

def pivoteia(matriz,coluna):
  primeiro_colunas = [abs(linha[coluna]) for linha in matriz[coluna:]]
  pos_maior = get_max_posicao(primeiro_colunas) + coluna
  if(coluna!=pos_maior):
    matriz[coluna], matriz[pos_maior] = matriz[pos_maior], matriz[coluna]
    print(f"T({coluna},{pos_maior})\n")
    imprime_matriz(matriz)


def soluciona(matriz,pivoteamento_parcial):
  imprime_matriz(matriz)

  # SOLUCIONADOR GAUSSIANO
  qtd_linhas = len(matriz)
  qtd_colunas = len(matriz[0])
  for coluna_pivot in range(qtd_colunas-2):
    if pivoteamento_parcial or matriz[coluna_pivot][coluna_pivot]==0:
      pivoteia(matriz,coluna_pivot)
    for linha_atual in range(coluna_pivot+1,qtd_linhas):
      razao = matriz[linha_atual][coluna_pivot]/matriz[coluna_pivot][coluna_pivot]
      if(razao==0): continue
      print(f"M({coluna_pivot},{linha_atual})={razao}\n")
      for coluna_atual in range(coluna_pivot,qtd_colunas):
        matriz[linha_atual][coluna_atual] = round(matriz[linha_atual][coluna_atual] - razao * matriz[coluna_pivot][coluna_atual],PRECISAO)
    imprime_matriz(matriz)
  vetor_x = [0] * (qtd_colunas-1)

  # DESCOBRIDOR DE VARIAVEIS
  for linha in range(qtd_linhas-1,-1,-1):
    soma = 0
    for coluna in range(qtd_colunas-1):
      soma += -matriz[linha][coluna]*vetor_x[coluna]
    vetor_x[linha] = round((matriz[linha][qtd_colunas-1]+soma)/matriz[linha][linha],PRECISAO)
    print(f"x{linha+1} = {vetor_x[linha]}")
  
  return matriz


def main():
  print()
  pivoteamento_parcial=True
  entrada= [
    [2,2,3,1,7],
    [1,-1,3,-1,1],
    [3,2,-3,-2,4],
    [4,3,2,1,12]
  ]
  saida = soluciona(entrada,pivoteamento_parcial)

if (__name__=="__main__"):
  main()