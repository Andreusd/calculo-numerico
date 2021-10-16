# Feito por Andre Uziel - andreuzielsd@gmail.com

from gauss_solver import soluciona, imprime_matriz
from math import cos

PRECISAO = 4

def main():

  entradax = [0.5,1.2,2.3]
  entraday = [3.4,4.5,2.8]

  nelem = len(entradax)
  if(nelem != len(entraday)):
    print("dados inconsistentes")
    return

  sistema = []
  for i in range(nelem):
    sistema.append([entradax[i]**index for index in range(nelem)])
    sistema[i].append(entraday[i])

  imprime_matriz(sistema)

  solucao = soluciona(sistema,log=False,pivoteamento_parcial=False)

  print("solucao")
  print([round(x,PRECISAO) for x in solucao])

  return lambda x:sum([coeficiente*x**index for index,coeficiente in enumerate(solucao)])

if(__name__=="__main__"):
  f = main()
  print(f(0.5))
  print(f(1.2))
  print(f(2.3))
