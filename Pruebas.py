import unittest
import ComplejosVector

class MyTestCase(unittest.TestCase):
    #Suma
    def test_suma(self):
        self.assertEqual(ComplejosVector.suma((2, 6), (4, 9)), (6, 15))
    #Producto
    def test_producto(self):
        self.assertEqual(ComplejosVector.producto((2, 6), (4, 9)), (-46, 42))
    #Resta    
    def test_resta(self):
        self.assertEqual(ComplejosVector.resta((2, 6), (4, 9)), (-2, -3))
    #División
    def test_div(self):
        self.assertEqual(ComplejosVector.div((2, 6), (4, 9)), (0.6392, 0.0619))
    #Módulo
    def test_mod(self):
        self.assertEqual(ComplejosVector.mod((2, 6)), 6.3246)
    #Conjugado
    def test_conj(self):
        self.assertEqual(ComplejosVector.conj((2, 6)), (2, -6))
    #Conversión entre representaciones polar y cartesiano
    def test_convercarpol(self):
        self.assertEqual(ComplejosVector.convercarpol((2, 6)), (6.3246, 71.5651))
    #Retornar la fase de un número complejo
    def test_fase(self):
        self.assertEqual(ComplejosVector.fase((2, 6)), (71.5651))
    #Adición de vectores complejos
    def test_sumvec(self):
        a = [(1,2),(2,1)]
        b = [(1,3),(3,1)]
        c = [(2,5),(5,2)]
        self.assertEqual(ComplejosVector.sumvec(a,b), c)
    #Inversa de vectores complejos.
    def test_invervec(self):
        a = [(1,2),(2,1)]
        c = [(-1,-2),(-2,-1)]
        self.assertEqual(ComplejosVector.invervec(a), c)
    #Multiplicación escalar de vectores complejos.
    def test_mulvec(self):
        a = 3
        b = [(1,2),(3,1)]
        c = [(3,6),(9,3)]
        self.assertEqual(ComplejosVector.mulvec(a,b), c)
    #Adición de matrices complejos.
    def test_sumMat(self):
        a = [[(1,2)],[(2,1)]]
        b = [[(3,1)],[(1,3)]]
        c = [[(4,3)], [(3,4)]]
        self.assertEqual(ComplejosVector.sumMat(a,b), c)    
    #Inversa de matrices complejos.
    def test_inverMat(self):
        a = [[(1,2)],[(3,3)],[(1,1)]]
        c = [[(-1, -2)], [(-3, -3)], [(-1, -1)]]
        self.assertEqual(ComplejosVector.inverMat(a), c)    
    #Multiplicación escalar de matrices complejas.
    def test_Escamat(self):
        a = 3
        b = [[(1,2)],[(3,3)],[(1,1)]]
        c = [[(3,6)], [(9,9)], [(3,3)]]
        self.assertEqual(ComplejosVector.Escamat(a,b), c)    
    #Matriz transpuesta
    def test_matTrans(self):
        a=[[(2,3),(1,9),(4,6)],[(2,5),(1,2),(3,6)],[(4,7),(4,9),(7,2)]]
        b=[[(2,3),(2,5),(4,7)],[(1,9),(1,2),(4,9)],[(4,6),(3,6),(7,2)]]
        self.assertEqual(ComplejosVector.matTrans(a), b)
    #Matriz conjugada
    def test_matConj(self):
        a=[[(2,3),(1,9),(4,6)],[(2,5),(1,2),(3,6)],[(4,7),(4,9),(7,2)]]
        b=[[(2,-3),(1,-9),(4,-6)],[(2,-5),(1,-2),(3,-6)],[(4,-7),(4,-9),(7,-2)]]
        self.assertEqual(ComplejosVector.matConj(a), b)
    #Matriz adjunta
    def test_matAdjun(self):
        a=[[(1,-1),(0,0)],
           [(3,4),(-1,0)]]
        b=[[(1,1),(3,-4)],
           [(0,0),(-1,0)]]
        self.assertEqual(ComplejosVector.matAdjun(a), b)
    #Función para calcular la "acción" de una matriz sobre un vector.    
    def test_accion(self):
        a=[[(2,0),(2,0),(2,0)]]
        b=[[(2,0),(2,0),(2,0)],
           [(2,0),(2,0),(2,0)],
           [(2,0),(2,0),(2,0)]]
        c=[[(8, 0), (8, 0), (8, 0)]]
        self.assertEqual(ComplejosVector.accion(a,b), c)
    #Norma de matrices
    def test_norma(self):
        a=[[(8,6)],[(6,-8)]]
        c=14.14
        self.assertEqual(ComplejosVector.norma(a), c)
    #Distancia entrematrices
    def test_distancia(self):
        a=[[(1,2)],[(2,1)]]
        b=[[(2,1)],[(3,2)]]
        c=2.0
        self.assertEqual(ComplejosVector.distancia(a,b), c)
    #Revisar si es unitaria
    def test_unitaria(self):
        a=[[(1,0),(0,0)],[(0,0),(1,0)]]
        self.assertEqual(ComplejosVector.unitaria(a), True)    
    #Revisar si es Hermitian
    def test_Hermi(self):
        a=[[(7,0)],[(6,5)],
        [(6,-5)],[(-3,0)]]
        self.assertEqual(ComplejosVector.Hermi(a), False)    
    #Producto tensor.
    def test_tensor(self):
        a=[[(2,0)],
           [(3,0)]]
        b=[[(4,0)],[(6,0)],[(3,0)]]
        c=[[[(8, 0)]], [[(12, 0)]], [[(6, 0)]], [[(12, 0)]], [[(18, 0)]], [[(9, 0)]]]
        self.assertEqual(ComplejosVector.tensor(a,b), c)
    



if __name__ == '__main__':
    unittest.main()
