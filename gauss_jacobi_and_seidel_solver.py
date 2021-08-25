PRECISAO = 3
MAX_ITER = 20

def gauss_jacobi(entrada,*valores_iniciais):
  tamanho = len(entrada[0])
  variaveis = [*valores_iniciais[:tamanho]]
  variaveism1 = [None] * (tamanho-1)
  for _ in range(0,MAX_ITER):
    print(variaveis)
    for linha in range(tamanho-1):
      soma = 0
      for coluna in range(tamanho-1):
        if(linha!=coluna):
          soma += -entrada[linha][coluna]*variaveis[coluna]
      variaveism1[linha] = round((entrada[linha][tamanho-1]+soma)/entrada[linha][linha],PRECISAO)
    if(all([variaveism1[i]==variaveis[i] for i in range(tamanho-1)])):
      break
    variaveis = [*variaveism1]
  return variaveis

def gauss_seidel(entrada,*valores_iniciais):
  tamanho = len(entrada[0])
  variaveis = [*valores_iniciais[:tamanho]]
  antigo = [None] * (tamanho-1)
  for _ in range(0,MAX_ITER):
    print(variaveis)
    for linha in range(tamanho-1):
      soma = 0
      for coluna in range(tamanho-1):
        if(linha!=coluna):
          soma += -entrada[linha][coluna]*variaveis[coluna]
      variaveis[linha] = round((entrada[linha][tamanho-1]+soma)/entrada[linha][linha],PRECISAO)
    if(all([antigo[i]==variaveis[i] for i in range(tamanho-1)])):
      break
    antigo = [*variaveis]
  return variaveis


def main():
  print()
  entrada = [
  [10,2,1,7],
  [1,5,1,-8],
  [2,3,10,6]
  ]
  saida = gauss_jacobi(entrada,0,0,0)
  print(saida)
  print()
  saida = gauss_seidel(entrada,0,0,0)
  print(saida)

if __name__=="__main__":
  main()