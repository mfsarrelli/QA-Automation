import pytest

@pytest.fixture
def numeros_positivos():
    return 5,5
@pytest.fixture
def numeros_negativos():
    return -2,8

@pytest.fixture
def numeros_flotantes():
    return 0.1,0.2