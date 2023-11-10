import pytest
from src.Ejercicio_2_2_2 import bucle_edad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "1 2 3 4 5 6 7 8 9 10 "),
        (15, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 "),
    ]
)
def test_bucle_edad_params(input_n, expected):
    assert bucle_edad(input_n) == expected