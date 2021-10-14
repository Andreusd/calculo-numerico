def imprime_tabela(tabela):
  print("Tabela")
  [print(linha) for linha in tabela]
  print()

valores_x = [.5,1.2,2.3,3.4,4.5]
valores_y = [3.4,4.5,2.8,1.1,6.4]

tabela = []
tabela.append(valores_x)
tabela.append(valores_y)

for i in range(2,len(valores_x)+1):
  tabela.append([])
  for j in range(len(tabela[i-1])-1):
    tabela[i].append((tabela[i-1][j+1]-tabela[i-1][j])/(tabela[0][j+i-1]-tabela[0][j]))

imprime_tabela(tabela)