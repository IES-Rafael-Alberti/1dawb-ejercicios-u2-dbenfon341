import pytest
from src.Ejercicio_2_1_9 import comprobar_edad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (4, "¡Entras gratis!"),
        (18, "10 €"),
        (100, "10 €"),
        (5, "5 €"),
        (17, "5 €"),
        (125, "10 €")
    ]
)
def test_comprobar_edad_params(input_n, expected):
    assert comprobar_edad(input_n) == expected