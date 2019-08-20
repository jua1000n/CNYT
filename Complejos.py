from sys import stdin
import math
# Suma de numeros complejos
def suma(r, i):
    res1 = float(r[0]) + float(i[0])
    res2 = float(r[1]) + float(i[1])
    return (res1, res2)

#Multiplicacion de numeros complejos
def producto(r, i):
    res1 = (r[0] * i[0]) - (r[1] * i[1])
    res2 = (r[0] * i[1]) + (r[1] * i[0])
    return (res1, res2)

#Resta de numeros complejos
def res(r, i):
    res1 = r[0] - i[0]
    res2 = r[1] - i[1]
    return (res1, res2)

#Division de numeros complejos
def div(r, i):
    res1 = round(((r[0] * i[0]) + (r[1] * i[1])) / ((i[0] ** 2) + (i[1] ** 2)),4)
    res2 = round(((r[1] * i[0]) - (r[0] * i[1])) / ((i[0] ** 2) + (i[1] ** 2)),4)
    return (res1, res2)

#modulo
def mod(r):
    res1 = round(((r[0] ** 2) + (r[1] ** 2)) ** (1 / 2),4)
    return (res1)

#Conjugado
def conj(i):
    r = [i[0], i[1]]
    res1 = -1 * r[1]
    r[1] = res1
    p=(r[0],r[1])
    return p

#De cartesiano a polar
def convercarpol(r):
    p = mod(r)
    teta = fase(r)
    return (p, teta)

#Retornar la fase de un numero complejo
def fase(r):
    fa = math.atan(abs(r[1] / r[0]))
    fa = fa * (180 / math.pi)
    return round(fa,4)
