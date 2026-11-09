import pytest

from .emisiones import calcular_emisiones_carbono


#Camino feliz
def test_calculo_correcto():
    assert calcular_emisiones_carbono(32) == 12.8 #Con assert estoy asegurando que el resultado de la funcion sera 12.8 en caso de no ser asi dara error el test

#Validacion del error
def test_consumo_negativo():
    with pytest.raises(ValueError): #Aqui estoy asegurando que la funcion devolvera un ValueError, en caso de no ser asi el test fallara
        calcular_emisiones_carbono(-50)