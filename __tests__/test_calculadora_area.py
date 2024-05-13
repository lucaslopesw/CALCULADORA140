import pytest

from calculadora_area.calculadora_area  import  calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo
from utils.utils import ler_csv

def test_calcular_area_quadrado():
    largura = 10
    comprimento = 20
    resultado_esperado = 200
    
    assert  calcular_area_quadrado(largura, comprimento) == resultado_esperado

def test_calcular_area_retangulo():
    largura = 10
    comprimento = 20
    resultado_esperado = 200

    assert  calcular_area_retangulo(largura, comprimento) == resultado_esperado

def test_calcular_area_triangulo():
    altura = 10
    base = 20
    resultado_esperado = 100

    assert  calcular_area_triangulo(altura, base) == resultado_esperado

@pytest.mark.parametrize('largura, comprimento, resultado_esperado', 
                         [
                            (10, 2, 20),
                            (30, 6, 180),
                            (800, 30, 24000),
                            (500, 25, 12500)
                         ]
                         )
def test_calcular_area_quadrado_lista(largura, comprimento, resultado_esperado):
    assert  resultado_esperado == calcular_area_quadrado(largura, comprimento)

@pytest.mark.parametrize('largura, comprimento, resultado_esperado',
                            ler_csv('./fixtures/massa_area_quadrado.csv')
                         )

def test_calcular_area_quadrado_csv(largura, comprimento, resultado_esperado):
    assert float(resultado_esperado) == calcular_area_quadrado(float(largura), float(comprimento))