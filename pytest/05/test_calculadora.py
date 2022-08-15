import pytest

from calculadora import calculadora


def test_suma_sin_error():
    resultado = calculadora(2, 3, '+')
    esperado = 5
    assert resultado == esperado


def test_resta_sin_error():
    resultado = calculadora(3, 2, '-')
    esperado = 1
    assert resultado == esperado


def test_division_sin_error():
    resultado = calculadora(10, 2, '/')
    esperado = 5
    assert resultado == esperado


def test_multiplicacion_sin_error():
    resultado = calculadora(2, 3, '*')
    esperado = 6
    assert resultado == esperado


def test_operacion_invalida():
    resultado = calculadora(2, 3, 'p')
    esperado = "operacion invalida"
    assert resultado == esperado

