import pytest
from exercicio1 import calcula_desconto

def test_quantidade_menor_que_10():
    assert calcula_desconto(valor_unitario = 10, quantidade = 9) == (90, 90)

def test_quantidade_entre_10_e_99():
    assert calcula_desconto(10, 10) == (100, 95) # sem desconto/com desconto

def test_quantidade_entre_100_e_999():
    assert calcula_desconto(10, 100) == (1000, 900)

def test_quantidade_maior_ou_igual_a_1000():
    assert calcula_desconto(10, 1000) == (10000, 8500)



