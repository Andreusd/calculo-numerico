from math import cos,log,sin

def newton(e,x,f,fl):
  k=0
  while(True):
    fx=f(x)
    flx=fl(x)
    print(k,x,fx,flx)
    if(abs(fx)<e):
      return x,k
    x=x-fx/flx
    k+=1

f=lambda x:sin(x)
fl=lambda x:cos(x)

print(newton(10**-10,3,f,fl))

