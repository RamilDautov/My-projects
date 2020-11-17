import numpy as np
import math


lam_0 = 6154.23
d_lam = 0.123
c = 300000000
I_0 = 1 / (1 + math.exp(d_lam / lam_0))


def Ak(x, n):
    y = np.zeros(n)
    y[-1] = 1
    h = np.polynomial.Hermite(y) #H2
    ak = (2**(n+1)*math.factorial(n)*math.sqrt(math.pi)) / (4*n**2*(h(x))**2)
    return ak


def Xk(n):
    y = np.zeros(n+1)
    y[n] = 1
    a = np.polynomial.hermite.herm2poly(y)
    xk = np.polynomial.polynomial.polyroots(a)
    return xk


def func(x):
    a = (c/d_lam)*(np.exp(x**2) - I_0) # *10^10
    return a

n = 3
lam = np.zeros(n)
x = Xk(n)

lam = (lam_0 * d_lam) / (lam_0 * x + d_lam)

A = Ak(x, n)
f = func(x)

equiv_width = np.sum(A * f)
equiv_width_A = c / equiv_width  # /10^10

print('Equivalent width: {} Hz'.format(equiv_width))
print('Equivalent width: {} A'.format(equiv_width_A))



