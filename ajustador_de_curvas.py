# Feito por Andre Uziel - andreuzielsd@gmail.com

from gauss_solver import soluciona,imprime_matriz

PRECISAO = 4

def main(entradax,entraday,grau,g):
  print("x:",entradax)
  print("y:",entraday)
  print()

  n = grau+1
  nelem = len(entradax)
  if(nelem != len(entraday)):
    print("dados inconsistentes")
    return
  matriz_l = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      matriz_l[i][j] = sum([g(entradax[I],i+1)*g(entradax[I],j+1) for I in range(nelem)])
  print("L")
  imprime_matriz(matriz_l)

  vetor_r = [0 for _ in range(n)]
  for i in range(n):
    vetor_r[i] = sum([g(entradax[I],i+1)*entraday[I] for I in range(nelem)])
  print("r")
  print(vetor_r)
  print()

  [matriz_l[i].append(vetor_r[i]) for i in range(len(matriz_l))]
  solucao = soluciona(matriz_l)

  print("solucao")
  print([round(x,PRECISAO) for x in solucao])
  print()

  f = lambda x:sum([coeficiente*x**index for index,coeficiente in enumerate(solucao)])

  # COEFICIENTE DE DETERMINACAO
  num_coef = sum([(entraday[j]-f(entradax[j]))**2 for j in range(nelem)])
  y_barra = 1/nelem * sum(entraday)
  den_coef = sum([((y-y_barra)**2) for y in entraday])
  coef_det = 1 - num_coef/den_coef

  print("R**2 (Coeficiente de determinacao)")
  print(round(coef_det,PRECISAO))
  print()

  return f

if(__name__=="__main__"):
  print()
  entradax = (-8,-6,-4,-2,0,2,4)
  entraday = (30,10,9,6,5,4,4)
  grau = 2
  g = lambda x,i:x**(i-1)
  f = main(entradax,entraday,grau,g)
  print([f(x) for x in entradax])
  print(f(2))