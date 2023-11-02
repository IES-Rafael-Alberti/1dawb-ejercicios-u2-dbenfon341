import pytest
from src.Ejercicio_2_1_5 import ingreso_suficiente, mayor_de_edad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (3545245, True),
        (200, False),
        (1233, True),
        (545, False),
        (12322, True),
        (100, False)
    ]
)
def test_ingreso_suficiente_params(input_n, expected):
    assert ingreso_suficiente(input_n) == expected