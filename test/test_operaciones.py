import pytest
import operaciones

@pytest.mark.parametrize("a, b, resultado", [
    (2, 4, 6), #numeros positivos
    (-5,-1,-6), #numeros negativos
    (0,0,0) #numeros ceros
    ])
@pytest.mark.smoke

def test_sumar_smoke(a, b, resultado):
    assert operaciones.sumar(a,b) == resultado

def test_restar_con_fixture(numeros_positivos, numeros_negativos):
    a,b = numeros_positivos
    c,d = numeros_negativos
    assert operaciones.restar(a,b) == 0
    assert operaciones.restar(c,d) == -10

def test_restar():
    assert operaciones.restar(22,11) == 11
    assert operaciones.restar(50,15) == 45

def test_multiplicar():
    assert operaciones.multiplicar(2,4) == 8
    assert operaciones.multiplicar(5,1) == 6

def test_division_por_cero():
    with pytest.raises(ValueError):
        operaciones.dividir(1,0)


