import pytest
from src.Ejercicio_2_1_3 import numeros_division

@pytest.mark.parametrize(
    "input_n, input_m, expected",
    [
        (1, 2, 0.5),
        (18, 3, 6.0),
        (100, 4, 25.0),
        (5, 5, 1.0),
        (17, 1, 17.0),
        (125, 4, 31.25)
    ]
)
def test_numeros_division_params(input_n, input_m, expected):
    assert numeros_division(input_n, input_m) == expected