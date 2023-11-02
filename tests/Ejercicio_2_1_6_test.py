import pytest
from src.Ejercicio_2_1_6 import comprobar_grupos

@pytest.mark.parametrize(
    "input_n, input_m, expected",
    [
        ("F", "M", "B"),
        ("M", "F", "B"),
        ("D", "M", "B"),
        ("P", "F", "B"),
        ("O", "M", "A"),
        ("L", "F", "A")
    ]
)
def test_numeros_division_params(input_n, input_m, expected):
    assert comprobar_grupos(input_n, input_m) == expected