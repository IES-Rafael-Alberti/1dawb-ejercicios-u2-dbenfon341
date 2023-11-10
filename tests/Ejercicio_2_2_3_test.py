import pytest
from src.Ejercicio_2_2_3 import bucle_impares

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (5, "1, 3, 5"),
        (4, "1, 3")
    ]
)
def test_bucle_impares_params(input_n, expected):
    assert bucle_impares(input_n) == expected