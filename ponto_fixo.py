from math import e,sqrt

def ponto_fixo(f,fi,x,tol):
    k=0
    while True:
        print(k,x,f(x))
        x=fi(x)
        k+=1
        if(abs(f(x))<tol):
            return x

f=lambda x:x**3+4*x**2-9
fi=lambda x:sqrt(9/(4+x))
ponto_fixo(f,fi,1.5,10**-5)

