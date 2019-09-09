from sys import stdin
import math

# Suma de numeros complejos
def suma(r, i):
    res1 = r[0] + i[0]
    res2 = r[1] + i[1]
    return (round(res1,4), round(res2,4))

#Multiplicacion de numeros complejos
def producto(r, i):
    res1 = (r[0] * i[0]) - (r[1] * i[1])
    res2 = (r[0] * i[1]) + (r[1] * i[0])
    return (round(res1,4), round(res2,4))

#Resta de numeros complejos
def resta(r, i):
    res1 = r[0] - i[0]
    res2 = r[1] - i[1]
    return (round(res1,4), round(res2,4))

#Division de numeros complejos
def div(r, i):
    res1 = round(((r[0] * i[0]) + (r[1] * i[1])) / ((i[0] ** 2) + (i[1] ** 2)),4)
    res2 = round(((r[1] * i[0]) - (r[0] * i[1])) / ((i[0] ** 2) + (i[1] ** 2)),4)
    return (round(res1,4), round(res2,4))

#modulo
def mod(r):
    res1 = round(((r[0] ** 2) + (r[1] ** 2)) ** (1 / 2),4)
    return (round(res1,4))

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

# Suma de vectores
def sumvec(r, i):
    vec = []
    if len(r) == len(i):
        for y in range(len(r)):
            vec.append(suma(r[y], i[y]))
        return vec

#Inversa de vectores
def invervec(r):
    vec = []
    for y in range(len(r)):
        res=(((r[y])[0]* (-1)), ((r[y])[1]* (-1)))
        vec.append(res)
    return vec

# Multiplicacion de vectores por escalar
def mulvec(r, i):
    vec = []
    for y in i:
        vec.append((y[0]*r,y[1]*r))
    return vec

#Suma de matrices
def sumMat(r,i):
    if len(r)==len(i) and len(r[0])==len(i[0]):
        mat = []
        if len(r)==len(i) and len(r[0])==len(i[0]):
            for y in range(len(r)):
                mat.append([])
                for x in range(len(r[y])):
                    mat[y].append(suma(r[y][x], i[y][x]))
            
        return mat
    else:
        return ValueError
    
#Inversa de matrices
def inverMat(r):
    mat=[]
    for y in range(len(r)):
        mat.append([])
        for x  in range(len(r[y])):
            mat[y].append(((r[y][x])[0]*(-1), (r[y][x])[1]*(-1)))
    return mat

#Multiplicacion de escalar por matriz
    
def Escamat(r,i):
    mat=[]
    if type(r) is int:
        r=(r,0)
    for y in range(len(i)):
        mat.append([])
        for x in range(len(i[0])):
            mat[y].append(producto(r,i[y][x]))
    return mat

#Matriz Transpuesta
def matTrans(r):
    mat=[]
    for y in range(len(r[0])):
        mat.append([])
        for x in range(len(r)):
            mat[y].append(r[x][y])
    return mat

#Matriz conjugada
def matConj(r):
    mat=[]
    for y in range(len(r)):
        mat.append([])
        for x in range(len(r[0])):
            mat[y].append(conj(r[y][x]))
    return mat

#Matriz adjunta
def matAdjun(r):
    mat=matTrans(matConj(r))
    return mat

#Revisar si es Hermitian
def  Hermi(r):
    if r==matAdjun(r):
        return True
    else:
        return False

#Producto tensor
def tensor(r,i):
    mat=[]
    for o in range(len(r)*len(i)):
        mat.append([])
    matsub=[]
    for y in range(len(r)):
        for x in range(len(r[y])):
            matsub=Escamat(r[y][x],i)
            con=0
            for z in range(y*len(i),(y+1)*len(i)):
                b=(matsub[con])
                mat[z].append(b)
                con+=1
    return mat
#print(tensor([[(1,3)]],[[(2,5),(3,5)],[(4,6),(2,9)]]))

#Multiplicacion dr matriz 
def multimat(r,i):
    mat = [[(0,0)]*len(i[0]) for h in range(len(r))]
    for y in range(len(r)):
        for j in range(len(i[0])):
            if len(mat)==1:
                long=2
            else:
                long=len(mat)
            for z in range(long):
                mat[y][j]=suma(mat[y][j],producto(r[y][z],i[z][j]))
    return mat
#print(multimat([[(1,0),(2,0)]],[[(2,0),(3,0)],[(5,0),(6,0)]]))
#accion
def accion(r,i):
    res=multimat(r,i)
    return res
#print(accion([[(2,0),(2,0),(2,0)]],[[(2,0),(2,0),(2,0)],[(2,0),(2,0),(2,0)],[(2,0),(2,0),(2,0)]]))
#Unitaria
def unitaria(r):
    mat=multimat(r,matAdjun(r))
    lis=[[(0,0)]*len(mat) for x in range(len(mat))]
    for y in range(len(lis)):
        for x in range(len(lis[y])):
            lis[y][y]=(1,0)
    if lis == mat:
        return True
    else:
        return False
#print(unitaria([[(1,0),(0,0),(0,0)],[(0,0),(1,0),(0,0)],[(0,0),(0,0),(1,0)]]))
    
    
#Norma de matrices
def norma(r):
    num=0
    for y in range(len(r)):
        for x in range(len(r[y])):
            num+=(r[y][x][0]**2)+(r[y][x][1]**2)
    return round(num**0.5,2)

def eleva(r):
    res=r[0]**2+r[1]**2
    return res

#Distancia entrematrices
def distancia(r,i):
    res=0
    for x in range(len(r)):
        for j in range(len(r[x])):
            res+=eleva(resta(r[x][j], i[x][j]))
    return res**0.5
#print(distancia([[(1,2),(2,1)]],[[(1,2),(2,1)]]))


