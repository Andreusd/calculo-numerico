def mais_proximos(lista:list[float], q:int, n:float) -> list[float]:
  '''
  dada uma lista ordenada, retorna os q numeros consecutivos mais proximos de n
  '''
  consecutivos=[]
  for elemento in lista:
    if (len(consecutivos)<q):
      consecutivos.append(elemento)
    elif (abs(elemento-n)<=abs(consecutivos[0]-n)):
      consecutivos.pop(0)
      consecutivos.append(elemento)
    else: break
  return consecutivos


if __name__=="__main__":
  lista=[0.5,1.2,2.3,3.4,4.5]
  q=3
  n=1.8
  m = mais_proximos(lista,q,n)
  print(m)