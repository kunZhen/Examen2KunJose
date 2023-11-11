from Examen2 import MiClase
import unittest


class TestMiClase(unittest.TestCase):
    def setUp(self):
        self.objeto = MiClase(5, 120, 12, ["Cancion 1", "Cancion 2", "Cancion 3"], [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        self.assertEqual(self.objeto.ObtieneValencia(9876543), 4)

    def test_DivisibleTempo(self):
        self.assertEqual(self.objeto.DivisibleTempo(15), [1, 3, 5, 15])

    def test_ObtieneMasBailable(self):
        self.assertEqual(self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)

    def test_VerificaListaCanciones_True(self):
        self.assertEqual(self.objeto.VerificaListaCanciones(["Cancion 1", "Cancion 2", "Cancion 3"]), True)

    def test_VerificaListaCanciones_False(self):
        self.assertEqual(self.objeto.VerificaListaCanciones(["Cancion 1", None, "Cancion 3"]), False)

if __name__ == "__main__":
    unittest.main()
