# Librería Números Complejos 

Es una librería la cual realiza las operaciones con números complejos por medio de diferentes funciones

# Como instalar la libreria  

Que cosas necesitas para instalar el software y como instalarlas 

Las cosas más básicas para poder usar la librería es tener Python 3.7 instalado en tu ordenador, para poder implementar la librería solo necesita crear una carpeta, guardar la librería con el nombre “ ComplejosVector.py ”, en el programa que quieras usar la librería tienes que poner “ import complejos”. 
 ```python
 import ComplejosVector
 ```

# Ejecución de librería 

Como sabemos los números complejos se basan por un número entero y un número real, “a(entero)+bi(real)".

Para que la librería pueda diferenciar entre el entero y el real se separará por medio de una coma, para una ejecución eficiente vamos a introducir esto en una tupla. 
 ```python
  def test_suma(self):
        self.assertEqual(ComplejosVector.suma((2, 6), (4, 9)), (6, 15))
 ```

Las funciones que vamos a encontrar se encuentra: 

- Suma
- Producto.
- Resta.
- División.
- Módulo.
- Conjugado.
- Conversión entre representaciones polar y cartesiano.
- Retornar la fase de un número complejo. 
- Adición de vectores complejos.
- Inversa de vectores complejos.
- Multiplicación escalar de vectores complejos.
- Adición de matrices complejos.
- Inversa de matrices complejos.
- Multiplicación escalar de matrices complejas.
- Matriz transpuesta
- Matriz conjugada
- Matriz adjunta
- Función para calcular la "acción" de una matriz sobre un vector.
- Norma de matrices
- Distancia entrematrices
- Revisar si es unitaria
- Revisar si es Hermitian
- Producto tensor.

# Que se puede encontrar en la libreria:

```python
def suma(r, i):
    res1 = r[0] + i[0]
    res2 = r[1] + i[1]
    return (round(res1,4), round(res2,4))
```
Como son tuplas tienen posición, en este caso se suman los numeros enteros y los numeros complejos,y por ultimo se retorna los valores dentro de una tupla.

```python
def  Hermi(r):
    if r==matAdjun(r):
        return True
    else:
        return False
```

Hay otras funciones las cuales va a botar un valor Boolean en cual va indicar si es o no es, en este caso al ingresar la funcion va a indicar si es Hermitian o no.

# Pruebas
En estas podremos ver el tipo de entrada que recibe,y las diferentes salidas que puede votar:
```python
import unittest
import ComplejosVector

class MyTestCase(unittest.TestCase):
    #Suma
    def test_suma(self):
        self.assertEqual(ComplejosVector.suma((2, 6), (4, 9)), (6, 15)) 
    #Retornar la fase de un número complejo
    def test_fase(self):
        self.assertEqual(ComplejosVector.fase((2, 6)), (71.5651))
    #Multiplicación escalar de vectores complejos.
    def test_mulvec(self):
        a = 3
        b = [(1,2),(3,1)]
        c = [(3,6),(9,3)]
        self.assertEqual(ComplejosVector.mulvec(a,b), c)
    #Revisar si es unitaria
    def test_unitaria(self):
        a=[[(1,0),(0,0)],
           [(0,0),(1,0)]]
        self.assertEqual(ComplejosVector.unitaria(a), True)    
if __name__ == '__main__':
    unittest.main()
```
# Hecho por
- Juan Sebastian Cadavid P
- Ingeniero de Sistemas
- Escuela Colombiana de Ingeniería Julio Garavito
