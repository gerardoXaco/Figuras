"""
hola flor
"""
import unittest
from Figuras import Figuras
class TestFiguras(unittest.TestCase):

	def setUp(self):#se ejecuta antes de cada metodo
		self.figura=Figuras()
	
	def test_area_cuadrado_lado_5(self):
		resultado=self.figura.cuadrado(5)
		self.assertEqual(25,resultado)
	def test_area_cuadrado_lado_6(self):
		resultado=self.figura.cuadrado(6)
		self.assertEqual(36,resultado)
	def test_area_cuadrado_lado_g(self):
		resultado=self.figura.cuadrado('g')
		self.assertEqual('dato incorrecto',resultado)
	def test_area_cuadrado_lado_4_5(self):
		resultado=self.figura.cuadrado(4.5)
		self.assertEqual(20.25,resultado)
		#RECTANGULO
	def test_area_rectangulo_lado_5_6(self):
		resultado=self.figura.rectangulo(5,6)
		self.assertEqual(30,resultado)
	def test_area_rectangulo_lado_a_6(self):
		resultado=self.figura.rectangulo('a',6)
		self.assertEqual('dato incorrecto',resultado)
	def test_area_rectangulo_lado_6_a(self):
		resultado=self.figura.rectangulo('a',6)
		self.assertEqual('dato incorrecto',resultado)
	def test_area_rectangulo_lado_a_6(self):
		resultado=self.figura.rectangulo('a','b')
		self.assertEqual('dato incorrecto',resultado)
	def test_area_rectangulo_lado_seispuntoseis_8(self):
		resultado=self.figura.rectangulo(6.6,8)
		self.assertEqual(52.8,resultado)
		#TRIANGULO
	def test_area_triaungulo_lados_4_7(self):
		resultado=self.figura.triangulo(4,7)
		self.assertEqual(14,resultado)
	def test_area_triangulo_lados_a_7(self):
		resultado=self.figura.triangulo('a',7)
		self.assertEqual('dato incorrecto',resultado)
	def test_area_triangulo_lados_4_a(self):
		resultado=self.figura.triangulo(4,'a')
		self.assertEqual('dato incorrecto',resultado)
	def test_area_triangulo_lados_cincopuntodos_7(self):
		resultado=self.figura.triangulo(5.2,7)
		self.assertEqual(18.2,resultado)
		#CIRCULO
		"""
	def test_area_circulo_radio_2(self):
		resultado=self.figura.circulo(2)
		self.assertEqual(12.56,resultado)
	def test_area_circulo_radio_a(self):
		resultado=self.figura.circulo('a')
		self.assertEqual('dato incorrecto',resultado)
	def test_area_circulo_radio_trespuntodos(self):
		resultado=self.figura.circulo(3.2)
		self.assertEqual(32.15,resultado)			
		"""

	#def tearDown(self):#se ejecuta al final

if __name__== '__main__':
	unittest.main()

