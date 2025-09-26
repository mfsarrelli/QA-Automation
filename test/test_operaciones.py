import pytest
import operaciones

def test_sumar():
    assert operaciones.sumar(2,4) == 7

def test_division_por_cero():
    with pytest.raises()

@pytest.mark.listo
def test_sumar_listo():
    assert operaciones.sumar(1,3) == 4