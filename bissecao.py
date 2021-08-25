from math import cos

def bissecao(f,a,b,tol):
  k = 1
  fa = f(a)
  while k < 100:
    p = (a + b) / 2
    fp = f(p)
    print(p,fp,a,f(a),b,f(b))
    if(b-a<tol or abs(fp)<tol):
      print(k)
      return p
    if(fa*fp>0):
      a=p
      fa=fp
    else:
      b=p
    k=k+1
  return "o metodo falhou"

def f(x):
  return x**3+4*x**2-9

a = 1
b = 2
tol = 10**(-5)
print(bissecao(f,a,b,tol))
