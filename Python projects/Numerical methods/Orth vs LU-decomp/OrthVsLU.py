import math
import numpy as np
import matplotlib.pyplot as plt


def ort_method(a, b):
    n = np.size(a, 0)
    a = np.c_[a, -b]
    c = np.zeros(n+1)
    c[-1] = 1
    a = np.r_[a, [c]]
    x = np.zeros(n)
    r = np.zeros((n+1, n+1))
    s = np.zeros((n+1, n+1))
    sa = np.zeros((n+1, n+1))
    r[0, :] = a[0, :]
    s[0, :] = r[0, :] / np.linalg.norm(r[0, :])

    for k in range(1, n+1):
        for i in range(0, k):
            sp = np.dot(a[k, :], s[i, :])
            for p in range(0, n+1):
                sa[i, p] = sp*s[i, p]

        for j in range(0, n+1):
            ss = 0
            for i in range(0, k):
                ss += sa[i, j]
            r[k, j] = a[k, j] - ss

        sp = round(np.linalg.norm(r[k, :]), 3)
        for p in range(0, n+1):
            s[k, p] = r[k, p] / sp

    for j in range(0, n):
        x[j] = r[n, j] / r[n, n]
    return x


def triangle_method(a, b):
    n = np.size(a, axis=0)
    u = np.zeros(np.shape(a))
    l = np.zeros(np.shape(a))
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(0, n):
        u[i, i] = 1

    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            if i >= j:
                for s in range(0, j):
                    sum += (l[i, s]) * (u[s, j])
                l[i, j] = a[i, j] - sum
            else:
                for s in range(0, i):
                    sum += l[i, s] * u[s, j]
                u[i, j] = (a[i, j]-sum) / l[i, i]

    y[0] = b[0] / l[0, 0]
    for i in range(1, n):
        s = 0
        for j in range(0, i):
            s += l[i, j] * y[j]
        y[i] = (b[i] - s) / l[i, i]

        x[n-1] = y[n-1]

        for i in range(n-2, -1, -1):
            s = 0
            for j in range(n-1, i, -1):
                s += x[j] * u[i, j]
            x[i] = y[i] - s

    return x


n = 10

a = np.random.rand(n, n)*10
b = np.random.rand(n)*10
#a = np.array([[4, -1, 1], [-1, 3, 1], [1, 1, 5]])
#b = np.array([8, 2, 8])
x = np.zeros(n)
y = np.zeros(n)

if np.linalg.det(a) == 0:
    print('det = 0 !!!')
    exit()

x = ort_method(a, b)
y = triangle_method(a, b)
print('        Accuracy of orth. method:                Accuracy of triangle method:')
for i in range(n):
    print('Dx[{2}]           {0:.5f}                                     {1:.5f}'.format(abs(np.dot(a,x)[i] - b[i]), abs(np.dot(a, y)[i] - b[i]), i))



