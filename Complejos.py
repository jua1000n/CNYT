from sys import stdin
import math
def prue():
    r = [2, 3]
    s = [1, 1]
    print(prod(r, s))
    print(suma(r, s))
    print(prod(r, s))
    print(res(r, s))
    print(div(r, s))
    print(mod(r))
    print(convercarpol(r))
    print(fase(r))


def suma(r, i):
    res1 = r[0] + i[0]
    res2 = r[1] + i[1]
    return "{}+{}i".format(res1, res2)


def prod(r, i):
    if len(r) == 1:
        res1 = r[0] * i[0]
        res2 = r[0] * i[1]
    elif len(i) == 1:
        res1 = i[0] * r[0]
        res2 = i[0] * r[1]
    elif len(i) == 2 and len(r) == 2:
        res1 = (r[0] * i[0]) - (r[1] * i[1])
        res2 = (r[0] * i[1]) + (r[1] * i[0])
    return "{}+{}i".format(res1, res2)


def res(r, i):
    res1 = r[0] - i[0]
    res2 = r[1] - i[1]
    return "{}+{}i".format(res1, res2)


def div(r, i):
    res1 = ((r[0] * i[0]) + (r[1] * i[1])) / ((i[0] ** 2) + (i[1] ** 2))
    res2 = ((r[0] * i[1]) - (r[1] * i[0])) / ((i[0] ** 2) + (i[1] ** 2))
    return "{}+{}i".format(res1, res2)


def mod(r):
    res1 = ((r[0] ** 2) + (r[1] ** 2)) ** (1 / 2)   
    return "{}".format(res1)


def conj(i):
    r = [i[0], i[1]]
    res1 = -1 * r[1]
    r[1] = res1
    return "{}".format(r)


def convercarpol(r):
    p = mod(r)
    teta = fase(r)
    return "{}, {}".format(p,teta)

def fase(r):
    fa = math.atan(abs(r[1] / r[0]))
    fa = fa * (180 / math.pi)
    return "{}".format(fa)


    
prue()
