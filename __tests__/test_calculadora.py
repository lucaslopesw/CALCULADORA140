# 1- bibilotecas, framwrosk e referências externas
import pytest

# funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros
from utils.utils import ler_csv

# 2 - Testes

def test_somar_dois_numeros():

    #Padrão / Standard AAA = Arrange, Act e Assert

    #Arrange / Prepara / Configura
    # Dados entrada e saída
    num1= 5
    num2 = 7
    resultado_esperado = 12

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    # Dados entrada e saída
    num1= 10
    num2 = 6
    resultado_esperado = 4

    # Act / Executa
    resultado_obtido = subtrair_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():
    # Dados entrada e saída
    num1= 10
    num2 = 6
    resultado_esperado = 60

    # Act / Executa
    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    # Dados entrada e saída
    num1= 24
    num2 = 6
    resultado_esperado = 4

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():
    # Dados entrada e saída
    num1= 24
    num2 = 0
    resultado_esperado = 'Erro: Não é possível dividir por zero'

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

# Test Baseados em Dados = Data Druveb Tests (DDT)

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [ # array / matriz
                             (5, 7, 12), # tuple / registro
                             (0, 8, 8), # tuple / registro
                             (10, -15, -5), # tuple / registro
                             (6, 0.75, 6.75) # tuple / registro
                         ]
                         )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):

    #Padrão / Standard AAA = Arrange, Act e Assert

    #Arrange / Prepara / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_somar.csv')
                         )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):

    #Padrão / Standard AAA = Arrange, Act e Assert

    #Arrange / Prepara / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido