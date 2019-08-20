import unittest
import ComplejosVector

class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(ComplejosVector.suma((2, 6), (4, 9)), (6, 15))

    def test_res(self):
        self.assertEqual(ComplejosVector.res((2, 6), (4, 9)), (-2, -3))

    def test_producto(self):
        self.assertEqual(ComplejosVector.producto((2, 6), (4, 9)), (-46, 42))

    def test_div(self):
        self.assertEqual(ComplejosVector.div((2, 6), (4, 9)), (0.6392, 0.0619))

    def test_mod(self):
        self.assertEqual(ComplejosVector.mod((2, 6)), 6.3246)

    def test_conj(self):
        self.assertEqual(ComplejosVector.conj((2, 6)), (2, -6))

    def test_convercarpol(self):
        self.assertEqual(ComplejosVector.convercarpol((2, 6)), (6.3246, 71.5651))

    def test_fase(self):
        self.assertEqual(ComplejosVector.fase((2, 6)), (71.5651))


if __name__ == '__main__':
    unittest.main()
