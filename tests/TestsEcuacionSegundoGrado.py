import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestsEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.caluloRaices =EcuacionSegundoGrado()

    def tearDown(self):
        self.caluloRaices = None

    def tests_calculoESO_dosNumeros_retornaSolucion(self):
        # arrange
        a= 1
        b= 2
        c= 1
        resultadoEsperadoRaiz1= -1
        resultadoEsperadoRaiz2= -1
        # do
        resultadoActualRaiz1, resultadoActualRaiz2 = self.caluloRaices.calculoESO(a, b, c)


        # Assert
        self.assertEqual(resultadoEsperadoRaiz1,resultadoActualRaiz1)
        self.assertEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2)



if __name__ == '__main__':
    unittest.main()
