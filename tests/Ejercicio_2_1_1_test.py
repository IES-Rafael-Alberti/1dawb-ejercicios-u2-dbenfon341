import pytest
from src.Ejercicio_2_1_1 import comprobar_edad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (20, "Eres mayor de edad."),
        (18, "Eres mayor de edad."),
        (10, "No eres mayor de edad."),
        (5, "No eres mayor de edad."),
        (17, "No eres mayor de edad."),
        (125, "Eres mayor de edad.")
    ]
)
def test_comprobar_edad_params(input_n, expected):
    assert comprobar_edad(input_n) == expected