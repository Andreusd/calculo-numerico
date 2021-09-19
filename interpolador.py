# Feito por Andre Uziel - andreuzielsd@gmail.com

from gauss_solver import soluciona, imprime_matriz

PRECISAO = 4

def main():

  entradax = (3.0,3.2,3.4)
  entraday = (20.08,24.53,29.96)

  nelem = len(entradax)
  if(nelem != len(entraday)):
    print("dados inconsistentes")
    return

  sistema = []
  for i in range(nelem):
    sistema.append([entradax[i]**index for index in range(nelem)])
    sistema[i].append(entraday[i])

  imprime_matriz(sistema)

  solucao = soluciona(sistema,log=False)

  print("solucao")
  print([round(x,PRECISAO) for x in solucao])

  return lambda x:sum([coeficiente*x**index for index,coeficiente in enumerate(solucao)])

if(__name__=="__main__"):
  f = main()
  print(f(3.4))
