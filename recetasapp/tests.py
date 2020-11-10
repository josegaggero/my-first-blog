
from django.test import TestCase
from .models import Iniciar, Producto


class PorcionesTestCase(TestCase):
     def setUp(self):
        tipo1 = Tipo.objects.createt(id=1,descripcion="Accion")
        Producto.objects.create(id = 3, nombre="Crodds",descripcion ="Peli infantil",url=".",href=".",precio=5000,cod_tipo=tipo1)


def test_Producto_tipo(self):
      Porciones1 = Producto.objects.get(id=1)
      self.assertEqual(Porciones1.cod_tipo.descripcion,"Accion")  

def test_Producto_precio(self):
       Porciones2 = Producto.objects.get(id=1)
       self.assertEqual(Porciones2.precio*3,10000)